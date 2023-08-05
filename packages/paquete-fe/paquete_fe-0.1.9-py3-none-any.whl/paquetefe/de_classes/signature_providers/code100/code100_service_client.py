import ast
from datetime import datetime, timedelta
from lxml import etree
import json
import os
import pytz
import requests
import sys
import traceback
import logging
import base64
import time
import zipfile
import decimal
from pathlib import Path
from zipfile import ZipFile
from de_classes.mysql_db_admin import Proceso, Log, De
from de_classes.process_mysql import log_register
#from .settings import URL, USER, PASSWORD, MAX_RETRY


class Code100ServiceClient:

    def __init__(self, url=None, user=None, password=None, max_retry=None, velocity=0.4, send_wait_time=0, response_wait_time=0):
        ex = ""
        # LOG_FILENAME = 'result.log'
        # logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG, filemode='a')

        self.url = url
        self.user = user
        self.password = password
        self.send_wait_time = send_wait_time
        self.response_wait_time = response_wait_time
        self.max_retry = int(max_retry)
        self.velocity = float(velocity)
        self.session = None
        self.proceso = None

    # Autenticacion
    def get_token(self):
        endpoint = "/login"
        response = self.send_request(url=f"{self.url}{endpoint}",
                                        ruc=self.user,
                                        password=self.password)

        if response:
            if response.status_code == 200:
                #print(response.content)
                json_response = response.json()
                self.token = json_response['token']
                return self.token
            else:
                mensaje = f"Error al generar TOKEN code100: Código: {response.status_code} Detalle: {response.content}"
                log_register(self.session, self.proceso.id, mensaje, Log.ERROR)
                return None
        else:
            mensaje = f"Error al generar TOKEN code100, no se obtuvo respuesta del servicio"
            log_register(self.session, self.proceso.id, mensaje, Log.ERROR)
            return None


        #print(response)
        #json_response = response.json()
        #self.token = json_response['token']
        #return self.token

    #Envio de lote
    def send_lote_signature_service(self, path_zip_file, session, proceso, cant_total_archivos):
        try:
            """
                Como este es el primer metodo invocado desde archivo-claro, origenclaro, etc..
                Aqui almacenamos en el objeto la session y el proceso, porque despues los demas metodos
                Se invocan desde files_backend, donde no se maneja el concepto de session (porque se usa el Django ORM
                en lugar de la session de SQLAlchemy!
            """
            self.session = session
            self.proceso = proceso

            id_lote = None
            cant_intentos = 1
            while cant_intentos <= self.max_retry and not id_lote:
                id_lote = self.send_lote_zip(path_zip_file, session, proceso)
                cant_intentos += 1

            if id_lote:
                #print(id_lote)
                proceso.estado = Proceso.PENDIENTE_APROBACION
                mensaje = (f"El lote {proceso.id} cambia del estado {Proceso.PROCESANDO} a {Proceso.PENDIENTE_APROBACION}"
                           " porque el lote pudo ser enviado al WS")
                log_register(session,
                             proceso.id,
                             mensaje,
                             Log.INFO)
                # Ademas, cambiamos el estado de todos los documentos del lote, cambiamos del estado GENERADO a EMITIDO
                session.query(De).filter(De.x_estado == De.GENERADO).update({De.x_estado: De.EMITIDO}, synchronize_session=False)
                session.commit()
                mensaje = f"Los documentos del lote {proceso.id} cambian del estado {De.GENERADO} a {De.EMITIDO} porque el lote pudo ser enviado al firmador"
                log_register(session, proceso.id, mensaje, Log.INFO)
            else:
                proceso.estado = Proceso.PROCESADO
                mensaje = f"El lote {proceso.id} cambia del estado {Proceso.PROCESANDO} a {Proceso.PROCESADO} porque el lote NO pudo ser enviado al firmador"
                log_register(session, proceso.id, mensaje, Log.ERROR)

            #Asignamos la cantidad de archivos enviados (solamente los correctos) y el Id del lote correspondiente
            proceso.cant_documentos = cant_total_archivos
            proceso.uuid_lote = id_lote

            # Consideramos que en promedio tarda 0,7 segundos en procesarse un documento, empezamos con 0,4 s
            # el checkeo cuando este al menos procesando casi al final
            cant_segundos = cant_total_archivos * self.velocity
            proceso.fecha_minima_revision = datetime.now() + timedelta(seconds=cant_segundos)
        except Exception as ex:
            print(f"Error: {ex}")
            raise


    # Envio de lote de instantaneos
    def send_lote_instant_signature_service(self, path_zip_file, session, proceso, cant_total_archivos):
        pass

    def send_lote_zip(self, path_zip_file, session, proceso):
        token = self.get_token()

        with open(path_zip_file, "rb") as xml_file:
            encoded_string = base64.b64encode(xml_file.read())
            encoded_string = encoded_string.decode("utf-8")

            endpoint = "/receive_batch"
            response = self.send_request(url=f"{self.url}{endpoint}", token=token, zip_base64=encoded_string)

            if response:
                if response.status_code == 200:
                    # print(response.status_code)
                    # print(response.content)
                    json_response = response.json()
                    status = json_response['status']
                    identificador = json_response['identificador']
                    log_register(session, proceso.id, f"El lote fue enviado satisfactoriamente. "
                    f"Respuesta del WS: Status {status}, identificador: {identificador}", Log.INFO)
                    return identificador

            mensaje = f"Error al enviar el zip. Código de error: {response.status_code}"
            print(response)
            print(response.content)
            log_register(session, proceso.id, mensaje, Log.ERROR)
            return 0

    # Consulta de Envio/Recepcion de archivo zip comprimido (lote). Esto no esta implementado en CIMA
    def get_zipfile_status(self, uuid):
        endpoint = "/batch_status"
        token = self.get_token()
        response = self.send_request(method="GET", url=f"{self.url}{endpoint}", token=token, identificador_lote=uuid)
        print(f"\nServicio: VERIFICACION DE STATUS DEL ARCHIVO ZIP {uuid}")
        #print("Código de Respuesta: ", response.status_code)
        #print("Respuesta: ", json.loads(response.content))
        result = f"{datetime.now()} VERIFICAR ENVIO DE ARCHIVO ZIP(operation=status): {response.status_code}, {response.content}"
        #logging.debug(result)

        # Le damos segundos para no verificar al toque el estado de la firma...
        print(f"Esperando {self.response_wait_time} segundos")
        time.sleep(self.response_wait_time)
        return response

    # Consulta de firma de documentos del lote enviado (estado de la SIFEN)
    def get_batch_signature_status(self, lote):
        endpoint = "/batch_status_sifen"
        token = self.get_token()
        print(f"\Inicia VERIFICACIÓN DE STATUS DE FIRMA DE DOCUMENTOS SIFEN DEL LOTE: {lote.uuid_lote}")
        response = self.send_request(method="GET", 
                                     url=f"{self.url}{endpoint}/{lote.uuid_lote}", 
                                     token=token)
        print(f"\Fin VERIFICACIÓN DE STATUS DE FIRMA DE DOCUMENTOS SIFEN DEL LOTE: {lote.uuid_lote}")
        print("Codigo de Respuesta: ", response.status_code)
        print("Respuesta: ", json.loads(response.content))
        result = f"{datetime.now()} VERIFICAR FIRMADO DE DOCUMENTOS (operation=status): {response.status_code}, " \
            f"{response.content}"
        # logging.debug(result)
        http_response = response.status_code

        if http_response == 200:
            detalle_completo = response.json()
            #Veamos que devuelve completo en JSON
            #print("ESTO DEVUELVE CODE 100 COMO RESPUESTA EN BRUTO:")
            #print(detalle_completo)
            #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            status = detalle_completo['estado']
            tamanho = detalle_completo['tamaño']
            progreso = detalle_completo['progreso']
            resumen = f"Se procesaron {progreso} de {tamanho} documentos"
            #print(status, tamanho, progreso)
            dict_api = {'cdc':'cdc', 'estado': 'estado', 'mensaje':'mensaje', 'error':'error',
                        'codigo_set': 'cod_respuesta', 'nro_lote': 'nro_lote', 'protocolo': 'protocolo'}
            dict_estados = {'Aprobado':'Aprobado', 'Rechazado': 'Rechazado', 'Error':'Error', 'Cancelado':'Cancelado',
                            'Pendiente':'Pendiente', 'Procesando':'Procesando', 'Enviado':'Enviado'}
            items = None
            if ((status == f"Lote enviado {tamanho}/{tamanho}" 
                        or int(tamanho) == int(progreso)
                    ) and int(tamanho) != 0):
                items = detalle_completo['Detalles']
                return http_response, "OK", resumen, items, dict_api, dict_estados
            else:
                return http_response, "PENDING", resumen, items, dict_api, dict_estados
        else:
            return http_response, response.content, None, None, None, None

    # Descargar Lote de documentos XML Firmados
    def get_xml_zip(self, lote, RESULTS_PATH):
        print(f"\nServicio: OBTENEMOS EL ZIP DE LOS XML FIRMADOS DEL PROCESO {lote.id}")

        token = self.get_token()
        endpoint = "/download_batch"
        response = self.send_request(method="GET", url=f"{self.url}{endpoint}/{lote.uuid_lote}",
                                     token=token,
                                     identificador_lote=lote.uuid_lote)

        if response.status_code == 200:
            respuesta = response.json()
            base_64_file_content = respuesta['zip_base64']

            if base_64_file_content and base_64_file_content != "Documentos del Lote no tienen XML Response":
                # convertimos del string base 64 a archivo .zip :D
                base64_zip_bytes = base_64_file_content.encode('utf-8')
                results_path = RESULTS_PATH
                Path(results_path).mkdir(parents=True, exist_ok=True)
                # Path(OUTPUT_PATH).mkdir(parents=True, exist_ok=True)

                file_signed = os.path.join(results_path, 'signed.zip')
                with open(file_signed, 'wb') as file_to_save:
                    # with open(f'{OUTPUT_PATH}/signed.zip', 'wb') as file_to_save:
                    decoded_zip_data = base64.decodebytes(base64_zip_bytes)
                    file_to_save.write(decoded_zip_data)
                    file_to_save.close()

                # Descomprimimos el archivo
                print("Unzipeamos el archivo zip obtenido")

                # path_to_zip_file = f'{OUTPUT_PATH}/results/signed.zip'
                # path_to_zip_file = f'{OUTPUT_PATH}/signed.zip'
                with zipfile.ZipFile(file_signed, 'r') as zip_ref:
                    zip_ref.extractall(results_path)
                    # zip_ref.extractall(f'{OUTPUT_PATH}/')

                mensaje = (f"Se obtuvo el zip del proceso: {lote.id}")
                return True, mensaje
            else:
                mensaje = (f"No se pudo obtener el archivo zip del lote: {lote.id}")
                return False, mensaje

        else:
            mensaje = (f"ERROR: {response.status_code}, Detalles: {response.content} al obtener el zip del lote {lote.id}")
            return False, mensaje

    #Envio de documento XML Individual
    #def send_xml(self, file, xml_file):
    def send_xml(self, xml_file, session=None, proceso=None):
        # logging.debug(f"Archivo XML: {file}")
        print("\nServicio: ENVIO DE XML INDIVIDUAL")
        file = open(xml_file, "rb").read()
        encoded_string = base64.b64encode(file)
        encoded_string = encoded_string.decode("utf-8")

        token = self.get_token()
        endpoint = "/receive_xml"
        response = self.send_request(url=f"{self.url}{endpoint}",
                                     token=token,
                                     xml_base64=encoded_string)
        # print("Código de Respuesta: ", response.status_code)
        #print("Respuesta: ", response.content)
        result = f"{datetime.now()} ENVIO DE ARCHIVO(operation=post): {response.status_code}, {response.content}"
        # logging.debug(result)

        # Le damos segundos para no verificar al toque el status...
        print(f"Esperando {self.send_wait_time} segundos")
        time.sleep(self.send_wait_time)
        return

    # Consulta de firma de documento XML individual
    def get_xml_signature_status(self, invoice_id):
        print(f"\nServicio: VERIFICACION DE ESTADO DE LA FIRMA {invoice_id}")

        token = self.get_token()
        endpoint = "/xml_status"
        response = self.send_request(method="GET", url=f"{self.url}{endpoint}/{invoice_id}", token=token, cdc=invoice_id)

        # print("Código de Respuesta: ", response.status_code)
        #print("Respuesta: ", response.content)
        result = f"{datetime.now()} VERIFICAR ESTADO DE LA FIRMA(operation=showXmlSignatureStatus): " \
            f"{response.status_code}, {response.content}"
        # logging.debug(result)
        # Le damos segundos...
        print(f"Esperando {self.response_wait_time} segundos")
        time.sleep(self.response_wait_time)
        return result

    # Descargar XML Individual firmado
    def get_xml_signed(self, invoice_id):
        print(f"\nServicio: OBTENEMOS EL XML FIRMADO Y APROBADO {invoice_id}")
        response = self.send_request(method="GET",
                                     url=self.url,
                                     token=self.token,
                                     operation="showXmlSigned",
                                     user=self.user,
                                     invoice_id=invoice_id)
        # print("Código de Respuesta: ", response.status_code)
        content = response.content.decode("UTF-8")
        try:
            content = ast.literal_eval(content)
            file_content = base64.b64decode(content['XML_Signed_Body'])
        except Exception as e:
            print(str(e))
            return ''

        # print("Respuesta: ", response.content)
        # logging.debug(
        #     f"{datetime.now()} OBTENER XML FIRMADO Y APROBADO(operation=showXmlSigned): {response.status_code}, {response.content}")
        return file_content

    def send_event(self, dict_parameters):
        pass
    
    def get_ruc(self, ruc):
        pass

    '''
    def get_xml_set_status(self, invoice_id):
        print(f"\nServicio: VERIFICACION DE RESPUESTA DE LA SET {invoice_id}")
        response = self.send_request(url=self.url, 
                                        token=self.token, 
                                        operation="showXmlResponse",
                                        user=self.user,
                                        invoice_id=invoice_id)

        print("Código de Respuesta: ", response.status_code)
        result = f"{datetime.now()} VERIFICAR RESPUESTA DE LA SET(operation=showXmlResponse): {response.status_code}, {response.content}"
        logging.debug(result)

        # Le damos segundos...
        print(f"Esperando {self.response_wait_time} segundos")
        time.sleep(self.response_wait_time)
        return result

    '''

    def send_request(self, method="POST", url=None, token=None, **kwargs):
        try:
            payload = {}
            for key, value in kwargs.items():
                payload[key] = value

            json_payload = json.dumps(payload)

            if token:
                headers = {'Content-Type': 'application/json', 
                           'Accept': 'application/json', 
                           'Authorization':  f'Bearer {token}'}
            else:
                headers = {'Content-Type': 'application/json', 
                           'Accept': 'application/json'}

            if method == "POST":
                response = requests.post(url=url, data=json_payload, headers=headers, timeout=None)
            elif method == "GET":
                response = requests.get(url=url, data=json_payload, headers=headers, timeout=None)
            return response

        except requests.exceptions.Timeout:
            error = "Tiempo de espera agotado para la solicitud"
            response_custom = RequestCustom(0, error)
            return response_custom
        except requests.exceptions.RequestException as e:
            error = str(e)
            response_custom = RequestCustom(0, error)
            return response_custom
        except Exception as e:
            error = f"Error no controlado: {e}"
            response_custom = RequestCustom(0, error)
            return response_custom

    def get_current_date_time(self):
        utc_now = pytz.utc.localize(datetime.utcnow())
        pst_now = utc_now.astimezone(pytz.timezone("America/Asuncion"))
        current_date_time = utc_now.isoformat()
        return current_date_time

    def get_invoice_id(self, full_file_name):
        tree = etree.parse(full_file_name)
        xmlstr = etree.tostring(tree.getroot()).decode('utf-8')
        tag_de_id = xmlstr.find('Id')
        invoice_id = xmlstr[tag_de_id + 4:tag_de_id + 48]
        return invoice_id


def write_zip_file(proceso, list_xml_files,session, OUTPUT_PATH):
    #path_zip_file = f'{OUTPUT_PATH}/{proceso.id}/lote.zip'
    path_zip_file = os.path.join(OUTPUT_PATH, 'lote.zip')
    with ZipFile(path_zip_file,'w') as zip:
        for file_path in list_xml_files:
            file = open(file_path, "rb").read()
            file_name = os.path.split(file_path)[-1]
            zip.writestr(file_name,file)
    log_register(session, proceso.id, f"Fue creado el archivo zip satisfactoriamente: {path_zip_file}", Log.INFO)
    return path_zip_file


class RequestCustom:
    def __init__(self, status_code, content) -> None:
        self.status_code = status_code
        self.content = content
        self.text = str(content)
