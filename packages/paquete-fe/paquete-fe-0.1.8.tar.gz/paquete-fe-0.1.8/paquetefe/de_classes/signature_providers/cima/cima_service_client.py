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


class CimaServiceClient:

    def __init__(self, url=None, user=None, password=None, max_retry=None, velocity=3, send_wait_time=0, response_wait_time=0):
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
        response = self.send_request(url=self.url,
                                        operation="token",
                                        user=self.user,
                                        password=self.password,
                                        datetime=self.get_current_date_time())

        if response:
            if response.status_code == 200:
                #print(response.content)
                json_response = response.json()
                self.token = json_response['Token']
                return self.token
            else:
                mensaje = f"Error al generar TOKEN CIMA: Código: {response.status_code} Detalle: {response.content}"
                log_register(self.session, self.proceso.id, mensaje, Log.ERROR)
                return None
        else:
            mensaje = f"Error al generar TOKEN CIMA, no se obtuvo respuesta del servicio"
            log_register(self.session, self.proceso.id, mensaje, Log.ERROR)
            return None

        #json_response = response.json()
        #self.token = json_response['Token']
        #return self.token

    # Envio de lote
    def send_lote_signature_service(self, path_zip_file, session, proceso, cant_total_archivos):
        """
            Como este es el primer metodo invocado desde archivo-claro, origenclaro, etc..
            Aqui almacenamos en el objeto la session y el proceso, porque despues los demas metodos
            Se invocan desde files_backend, donde no se maneja el concepto de session (porque se usa el Django ORM
            en lugar de la session de SQLAlchemy!
        """
        self.session = session
        self.proceso = proceso

        id_lote = 0
        cant_intentos = 1
        while cant_intentos <= self.max_retry and id_lote == 0:
            id_lote = self.send_lote_zip(path_zip_file, session, proceso)
            cant_intentos += 1

        if id_lote > 0:
            #print(id_lote)
            proceso.estado = Proceso.PENDIENTE_APROBACION
            log_register(session,
                         proceso.id,
                         f"El lote {proceso.id} cambia del estado {Proceso.PROCESANDO} a {Proceso.PENDIENTE_APROBACION} porque el lote pudo ser enviado al WS",
                         Log.INFO)
            # Ademas, cambiamos el estado de todos los documentos del lote, cambiamos del estado GENERADO a EMITIDO
            session.query(De).filter(De.x_estado == De.GENERADO).update({De.x_estado: De.EMITIDO}, synchronize_session=False)
            session.commit()
            log_register(session, proceso.id, f"Los documentos del lote {proceso.id} cambian del estado {De.GENERADO} a {De.EMITIDO} porque el lote pudo ser enviado al firmador", Log.INFO)
        else:
            proceso.estado = Proceso.PROCESADO
            log_register(session, proceso.id, f"El lote {proceso.id} cambia del estado {Proceso.PROCESANDO} a {Proceso.PROCESADO} porque el lote NO pudo ser enviado al firmador", Log.ERROR)

        #Asignamos la cantidad de archivos enviados (solamente los correctos) y el Id del lote correspondiente
        proceso.cant_documentos = cant_total_archivos
        proceso.id_lote_cima = id_lote

        # Consideramos que en promedio tarda 3 segundos en procesarse un documento, dividimos entre 2 para empezar
        # el checkeo cuando este al menos procesando la mitad del lote
        cant_segundos = cant_total_archivos * self.velocity
        proceso.fecha_minima_revision = datetime.now() + timedelta(seconds=cant_segundos)


    # Envio de lote de instantaneos
    def send_lote_instant_signature_service(self, path_zip_file, session, proceso, cant_total_archivos):
        pass

    def send_lote_zip(self, path_zip_file, session, proceso):
        token = self.get_token()

        with open(path_zip_file, "rb") as xml_file:
            encoded_string = base64.b64encode(xml_file.read())
            encoded_string = encoded_string.decode("utf-8")

            response = self.send_request(url=self.url, token=token, operation="sendZipLote",
                                        user=self.user,
                                        data_zip=encoded_string)

            if response:
                if response.status_code == 200:
                    #print(response.status_code)
                    #print(response.content)
                    json_response = response.json()
                    id_lote = json_response['Id Lote']
                    log_register(session, 
                                 proceso.id, 
                                 f"El lote zip fue enviado satisfactoriamente. El identificador devuelto por el WS es: {id_lote}",
                                 Log.INFO)
                    return id_lote
                else:
                    mensaje = f"Error al enviar el zip a CIMA: Código: {response.status_code} Detalle: {response.content}"
                    log_register(session, proceso.id, mensaje, Log.ERROR)
                    return 0
            else:
                mensaje = f"Error al enviar el zip a CIMA: Código: {response.status_code} Detalle: {response.content}"
                log_register(session, proceso.id, mensaje, Log.ERROR)
                return 0

    # Consulta de Envio/Recepcion de archivo zip comprimido (lote)
    # Este metodo en principio no es necesario o prioritario
    def get_zipfile_status(self, uuid):
        return "Metodo aun no implementado"


    # Consulta de firma de documentos del lote enviado (estado de la SIFEN)
    # Actualmente esta en files_backend, se crea ahora como metodo, y faltaria invocar desde alli
    def get_batch_signature_status(self, lote):
        token = self.get_token()
        response = self.send_request(url=self.url,
                                     token=token,
                                     operation="showXmlSignatureStatusLote",
                                     user=self.user,
                                     IdLote=lote.id_lote_cima)
        # print(f"\nServicio: VERIFICACION DE STATUS DE FIRMA DE DOCUMENTOS SIFEN DEL LOTE {lote.id}")
        #print("Código de Respuesta: ", response.status_code)
        #print("Respuesta: ", json.loads(response.content))
        respuesta = response.json()
        result = f"{datetime.now()} VERIFICAR FIRMA DOCUMENTOS SIFEN(operation=status): {response.status_code}, " \
            f"{response.text}"
        # logging.debug(result)

        http_response = response.status_code

        if http_response == 200:
            detalle_completo = response.json()
            print(f"JSON lote {lote.id_lote_cima}")
            print(detalle_completo)
            status = detalle_completo['Status_Lote']
            progreso = detalle_completo['Progreso_Lote']
            resumen = f"Se procesaron {progreso} documentos"
            #print(status, progreso)
            dict_api = {'cdc': 'InvoiceID', 'estado': 'Status', 'mensaje': 'Comentarios', 'error':'error',
                        'codigo_set': 'cod_respuesta', 'nro_lote': 'nro_lote', 'protocolo': 'protocolo'}
            dict_estados = {'Aprobado':'CORRECT', 'Rechazado': 'REJECTED', 'Error':'ERROR', 'Cancelado':'CANCELLED',
                            'Pendiente':'PENDING', 'Procesando':'PROCESSING', 'Enviado':'Enviado'}
            items = None

            # En el caso de cima, necesitamos hacer un triple control por los casos que quedan de repente en "Emitido"
            # Controlamos el estado actual del proceso de firma de la SET (status), tambien obtenemos el progreso
            # y finalmente, tambien contamos la cantidad de items del detalle. Si y solo los tres están OK, estará OK.
            split_progreso = progreso.split()
            cant_procesados = int(split_progreso[0])
            cant_total = int(split_progreso[2])
            items = detalle_completo['Detalle_de_Lote']
            if status == "Finalizado" and (cant_procesados == cant_total) and (len(items) == cant_total):
                return http_response, "OK", resumen, items, dict_api, dict_estados
            else:
                return http_response, "PENDING", resumen, items, dict_api, dict_estados
        else:
            return http_response, "PENDING", str(respuesta), None, None, None

    # Descargar Lote de documentos XML Firmados
    def get_xml_zip(self, lote, RESULTS_PATH):
        print(f"\nServicio: OBTENEMOS EL ZIP DE LOS XML FIRMADOS DEL PROCESO {lote.id}")
        token = self.get_token()
        response = self.send_request(url=self.url,
                                     token=token,
                                     operation="showXmlResponseLoteZip",
                                     user=self.user,
                                     IdLote=lote.id_lote_cima)

        if response.status_code == 200:
            respuesta = response.json()
            base_64_file_content = respuesta['Lote_Response_Zip']

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

                print(f"Se obtuvo el zip del proceso: {lote.id}")
                return True
            else:
                print(f"No se pudo obtener el archivo zip del lote: {lote.id}")
                return False

        else:
            # print(f"ERROR: {response.status_code} al obtener el lote {lote.id}")
            return False

    # Envio de documento XML Individual
    def send_xml(self, file, xml_file):
        # logging.debug(f"Archivo XML: {file}")
        print("\nServicio: ENVIO DE XML INDIVIDUAL")
        encoded_string = base64.b64encode(xml_file.read())
        encoded_string = encoded_string.decode("utf-8")

        token = self.get_token()
        response = self.send_request(url = self.url,
                                     token=token,
                                     operation="post",
                                     user=self.user,
                                     data=encoded_string,
                                     filename=os.path.basename(xml_file.name))
        # print("Código de Respuesta: ", response.status_code)
        #print("Respuesta: ", response.content)
        result = f"{datetime.now()} ENVIO DE ARCHIVO(operation=post): {response.status_code}, {response.content}"
        # logging.debug(result)

        # Le damos segundos para no verificar al toque el status...
        # print(f"Esperando {self.send_wait_time} segundos")
        time.sleep(self.send_wait_time)
        return

    # Consulta de firma de documento XML individual
    def get_xml_signature_status(self, invoice_id):
        print(f"\nServicio: VERIFICACION DE ESTADO DE LA FIRMA {invoice_id}")
        response = self.send_request(url=self.url,
                                        token=self.token,
                                        operation="showXmlSignatureStatus",
                                        user=self.user,
                                        invoice_id=invoice_id)

        # print("Código de Respuesta: ", response.status_code)
        #print("Respuesta: ", response.content)
        result = f"{datetime.now()} VERIFICAR ESTADO DE LA FIRMA(operation=showXmlSignatureStatus): {response.status_code}, {response.content}"
        # logging.debug(result)
        # Le damos segundos...
        print(f"Esperando {self.response_wait_time} segundos")
        time.sleep(self.response_wait_time)
        return result


    # Descargar XML Individual firmado
    def get_xml_signed(self, invoice_id):
        print(f"\nServicio: OBTENEMOS EL XML FIRMADO Y APROBADO {invoice_id}")
        response = self.send_request(url=self.url,
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
        #logging.debug(
        #     f"{datetime.now()} OBTENER XML FIRMADO Y APROBADO(operation=showXmlSigned): {response.status_code}, {response.content}")
        return file_content

    # Este metodo no hay en Code100 como tal, se consulta directamente el estado del documento XML individual Firmado
    def get_xml_status(self, invoice_id, file_name):
        response = self.send_request(url=self.url, 
                                        token=self.token, 
                                        operation="status", 
                                        user=self.user,
                                        invoice_id=invoice_id,
                                        filename=file_name)
        print(f"\nServicio: VERIFICACION DE STATUS DEL XML {invoice_id}")
        # print("Código de Respuesta: ", response.status_code)
        #print("Respuesta: ", json.loads(response.content))
        result = f"{datetime.now()} VERIFICAR ENVIO DE ARCHIVO(operation=status): {response.status_code}, {response.content}"
        # logging.debug(result)

        # Le damos segundos para no verificar al toque el estado de la firma...
        print(f"Esperando {self.response_wait_time} segundos")
        time.sleep(self.response_wait_time)
        return result

    #Este metodo hay que revisar donde/quien utiliza. No se encuentran referencias de uso
    def get_xml_set_status(self, invoice_id):
        print(f"\nServicio: VERIFICACION DE RESPUESTA DE LA SET {invoice_id}")
        response = self.send_request(url=self.url, 
                                        token=self.token, 
                                        operation="showXmlResponse",
                                        user=self.user,
                                        invoice_id=invoice_id)

        # print("Código de Respuesta: ", response.status_code)
        result = f"{datetime.now()} VERIFICAR RESPUESTA DE LA SET(operation=showXmlResponse): {response.status_code}, {response.content}"
        # logging.debug(result)

        # Le damos segundos...
        print(f"Esperando {self.response_wait_time} segundos")
        time.sleep(self.response_wait_time)
        return result

    def send_request(self, url, token=None, **kwargs):
        try:
            payload = {}
            for key, value in kwargs.items():
                payload[key] = value

            json_payload = json.dumps(payload)

            if token:
                headers = {'Content-Type': 'application/json', 
                           'Accept': 'application/json', 
                           'X-Auth-Token': token}
            else:
                headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

            response = requests.post(url=url, data=json_payload, headers=headers, timeout=None)
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
