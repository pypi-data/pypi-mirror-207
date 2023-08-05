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
import shutil
from de_classes.mysql_db_admin import Proceso, Log, De
from de_classes.process_mysql import log_register


class FacturyServiceClient:

    def __init__(self, url=None, api_token=None, max_retry=None, velocity=1,
                 send_wait_time=0, response_wait_time=0):
        self.url = url
        self.api_token = api_token

        self.send_wait_time = send_wait_time
        self.response_wait_time = response_wait_time
        self.max_retry = int(max_retry)
        self.velocity = float(velocity)
        self.session = None
        self.proceso = None

    # El token viene en la conf, se almacena, obtenemos y usamos..
    def get_token(self):
        pass

    # Envio de lote
    def send_lote_signature_service(self, path_zip_file, session, proceso, cant_total_archivos):
        try:
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
                mensaje = (f"El proceso {proceso.id} cambia del estado {Proceso.PROCESANDO} a {Proceso.PENDIENTE_APROBACION}"
                           " porque los documentos se enviaron al firmador")
                log_register(session,
                             proceso.id,
                             mensaje,
                             Log.INFO)
                # Ademas, cambiamos el estado de todos los documentos del lote, cambiamos del estado GENERADO a EMITIDO
                session.query(De).filter(De.x_estado == De.GENERADO).update({De.x_estado: De.EMITIDO}, synchronize_session=False)
                session.commit()
                mensaje = f"Los documentos sin errores cambian del estado Generado a Emitido"
                log_register(session, proceso.id, mensaje, Log.INFO)
            else:
                proceso.estado = Proceso.PROCESADO
                mensaje = f"El proceso {proceso.id} cambia del estado {Proceso.PROCESANDO} a {Proceso.PROCESADO} porque el lote NO pudo ser enviado al firmador"
                log_register(session, proceso.id, mensaje, Log.ERROR)

            #Asignamos la cantidad de archivos enviados (solamente los correctos) y el Id del lote correspondiente
            proceso.cant_documentos = cant_total_archivos
            proceso.uuid_lote = id_lote

            # Consideramos que en promedio tarda 0,7 segundos en procesarse un documento, empezamos con 0,4 s
            # el checkeo cuando este al menos procesando casi al final
            cant_segundos = cant_total_archivos * self.velocity
            proceso.fecha_minima_revision = datetime.now() + timedelta(seconds=cant_segundos)
            session.commit()
        except Exception as ex:
            print(f"Error: {ex}")
            raise

    
    # Envio de lote de instantaneos
    def send_lote_instant_signature_service(self, path_zip_file, session, proceso, cant_total_archivos):
        try:
            # Checkear si hace falta guardar esto realmente en la clase (la sesion y el proceso)
            self.session = session
            self.proceso = proceso

            id_lote = None
            cant_intentos = 1
            # Vamos a mantener esto? Misma cantidad de intentos?
            while cant_intentos <= self.max_retry and not id_lote:
                id_lote = self.send_lote_inst_zip(path_zip_file, session, proceso)
                cant_intentos += 1
            
            if id_lote:                
                proceso.estado = Proceso.PENDIENTE_OBTENER_ZIP
                mensaje = (f"El lote {proceso.id} cambia del estado {Proceso.PROCESANDO} a {proceso.estado}")
                log_register(session,
                             proceso.id,
                             mensaje,
                             Log.INFO)
                # Mantenemos este estado EMITIDO/PROCESADO?
                (session.query(De)
                    .filter(De.x_estado == De.GENERADO)
                    .update({De.x_estado: De.EMITIDO}, 
                            synchronize_session=False))
                mensaje = (f"Los documentos del lote {proceso.id} cambian del estado " 
                           f"{De.GENERADO} a {De.EMITIDO} porque el lote pudo ser enviado al firmador")
                log_register(session, proceso.id, mensaje, Log.INFO)
            else:
                proceso.estado = Proceso.PROCESADO
                mensaje = (f"El lote {proceso.id} cambia del estado {Proceso.PROCESANDO} a "
                           f"{Proceso.PROCESADO} porque el lote NO pudo ser enviado al firmador")
                log_register(session, proceso.id, mensaje, Log.ERROR)

            #Asignamos la cantidad de archivos enviados (solamente los correctos) y el Id del lote correspondiente
            proceso.cant_documentos = cant_total_archivos
            proceso.uuid_lote = id_lote

            # ESTE TEMA DEL CALCULO PARA EL CHECKEO POSTERIOR NO APLICA.. SE HACE SINCRONICO TODITO.
            # Consideramos que en promedio tarda 0,7 segundos en procesarse un documento, empezamos con 0,4 s
            # el checkeo cuando este al menos procesando casi al final
            # cant_segundos = cant_total_archivos * self.velocity
            proceso.fecha_minima_revision = datetime.now()
            session.commit()

            # A DIFERENCIA DEL LOTE NORMAL, AQUI SI DEBEMOS RETORNAR LO QUE NOS DEVUELVE METROPOLIS! Capaz la cantidad de docs firmados OK
            return id_lote 

        except Exception as ex:
            print(f"Error: {ex}")
            raise

    def send_lote_zip(self, path_zip_file, session, proceso):
        token = self.api_token

        with open(path_zip_file, "rb") as xml_file:
            encoded_string = base64.b64encode(xml_file.read())
            encoded_string = encoded_string.decode("utf-8")
            endpoint = "/receive-batch/"
            response = self.send_request(url=f"{self.url}{endpoint}", token=token, zip_base64=encoded_string)
            response.encoding = 'utf-8'
            
            if response.status_code == 200:
                # print(response.status_code)
                # print(response.content)
                json_response = response.json()
                status = json_response['estado']
                identificador = json_response['id_lote_provider']
                log_register(session, proceso.id, f"El lote fue enviado satisfactoriamente. "
                f"Respuesta del firmador: Status {status}, identificador: {identificador}", Log.INFO)
                return identificador

            mensaje = f"Error al enviar el zip. Código de error: {response.status_code} Detalle: {response.text}"
            print(response)
            print(response.content)
            log_register(session, proceso.id, mensaje, Log.ERROR)
            return 0

    def send_lote_inst_zip(self, path_zip_file, session, proceso):
        token = self.api_token

        with open(path_zip_file, "rb") as xml_file:
            encoded_string = base64.b64encode(xml_file.read())
            encoded_string = encoded_string.decode("utf-8")
            endpoint = "/receive-batch-instants/"            
            response = self.send_request(url=f"{self.url}{endpoint}", token=token, zip_base64=encoded_string)

            if response:
                if response.status_code == 200:
                    # print(response.status_code)
                    # print(response.content)
                    json_response = response.json()
                    status = json_response['estado']
                    identificador = json_response['id_lote_provider']
                    mensaje = f"El lote instantáneo fue enviado satisfactoriamente al firmador. Identificador: {identificador}"
                    log_register(session, 
                                 proceso.id, 
                                 mensaje, 
                                 Log.INFO)
                    return identificador

            mensaje = f"Error al enviar el zip de instantaneos. Código de error: {response.status_code} Detalle: {response.text}"
            # print(response)
            # print(response.content)
            log_register(session, proceso.id, mensaje, Log.ERROR)
            return 0

    def get_zipfile_status(self, uuid):
        pass

    def get_batch_signature_status(self, lote):
        endpoint = "/batch-status/"
        token = self.api_token
        response = self.send_request(method="GET",
                                     url=f"{self.url}{endpoint}{lote.uuid_lote}",
                                     token=token)
        # print(f"\nServicio: VERIFICACION DE STATUS DE FIRMA DE DOCUMENTOS SIFEN DEL LOTE: {lote.uuid_lote}")
        # print("Codigo de Respuesta: ", response.status_code)
        # print("Respuesta: ", response.text)

        # result = f"{datetime.now()} VERIFICAR FIRMADO DE DOCUMENTOS (operation=status): {response.status_code}, " \
        #     f"{response.text}"
        # logging.debug(result)
        http_response = response.status_code

        if http_response == 200:
            detalle_completo = response.json()
            status = detalle_completo['estado']
            tamanho = detalle_completo['tamaño']
            progreso = detalle_completo['progreso']
            resumen = f"Se validaron {progreso} de {tamanho} documentos en la SET"

            dict_api = {'cdc': 'cdc', 'estado': 'estado', 'mensaje': 'observaciones', 'error': 'error',
                        'codigo_set': 'cod_respuesta', 'nro_lote': 'nro_lote', 'protocolo': 'protocolo'}
            dict_estados = {'Aprobado': 'Aprobado', 'Aprobado con observaciones': 'Aprobado con observaciones', 
                            'Rechazado': 'Rechazado', 'Error': 'Error',
                            'Cancelado': 'Cancelado',
                            'Pendiente': 'Pendiente', 'Procesando': 'Procesando', 'Enviado': 'Enviado'}
            items = None
            if ((status == f"Lote enviado {tamanho}/{tamanho}" or int(tamanho) == int(progreso))
                    and int(tamanho) != 0):
                items = detalle_completo['detalles']
                return http_response, "OK", resumen, items, dict_api, dict_estados
            else:
                return http_response, "PENDING", resumen, items, dict_api, dict_estados
        else:
            return http_response, response.content, None, None, None, None

    def get_xml_zip(self, lote, RESULTS_PATH, zip_format=''):
        print(f"\nServicio: OBTENEMOS EL ZIP DE LOS XML FIRMADOS DEL PROCESO {lote.uuid_lote}")

        token = self.api_token
        endpoint = "/download-batch/"
        url = f"{self.url}{endpoint}{lote.uuid_lote}"
        if zip_format:
            url = f'{url}?zip_format={zip_format}'
        response = self.send_request(method="GET", url=url,
                                     token=token,
                                     identificador_lote=lote.uuid_lote)
        response.encoding = 'utf-8'

        if response.status_code == 200:
            respuesta = response.json()

            results_path = RESULTS_PATH
            Path(results_path).mkdir(parents=True, exist_ok=True)
            signed_zip_path = os.path.join(results_path, 'signed.zip')
            zip_ok = False

            if respuesta.get('path'):
                # Recibimos el path del zip que debería ser accesible (mismo equipo probablemente)
                # y lo copiamos a la carpeta respectiva
                metropolis_zip_path = respuesta.get('path')
                if not os.path.exists(metropolis_zip_path):
                    mensaje = f'No se encontró el zip en {metropolis_zip_path}'
                    return False, mensaje
                shutil.copyfile(metropolis_zip_path, signed_zip_path)
                zip_ok = True
            
            elif respuesta.get('zip_base64') and respuesta.get('zip_base64') != "Documentos del Lote no tienen XML Response":
                # convertimos del string base 64 a archivo .zip :D
                base64_zip_bytes = respuesta['zip_base64'].encode('utf-8')
                
                with open(signed_zip_path, 'wb') as file_to_save:
                    base64_zip_bytes = base64.decodebytes(base64_zip_bytes)
                    file_to_save.write(base64_zip_bytes)
                    file_to_save.close()
                zip_ok = True
                del respuesta; del response ; del base64_zip_bytes; del file_to_save
                
            else:
                mensaje = (f"No se pudo obtener el archivo zip del proceso: {lote.id}")
                return False, mensaje
            
            if zip_ok:
                # Descomprimimos el archivo
                print("Unzipeamos el archivo zip obtenido")

                with zipfile.ZipFile(signed_zip_path, 'r') as zip_ref:
                    zip_ref.extractall(results_path)
                    
                mensaje = (f"Se obtuvo el zip del proceso: {lote.id}")
                del zip_ref
                return True, mensaje
        else:
            mensaje = (f"ERROR: {response.status_code}, Detalles: {response.text} al obtener el zip del proceso {lote.id}")
            return False, mensaje
    # Envio de documento XML Individual
    def send_xml(self, xml_file, session=None, proceso=None):
        print("\nServicio: ENVIO DE XML INDIVIDUAL")
        status_codes_accepted = [200, 400, 500, 503]

        cant_intentos = 1
        response = None
        while cant_intentos <= self.max_retry:
            file = open(xml_file, "rb").read()
            encoded_string = base64.b64encode(file)
            encoded_string = encoded_string.decode("utf-8")
            
            endpoint = "/receive-xml/"
            response = self.send_request(url=f"{self.url}{endpoint}", xml=encoded_string)
            if response.status_code in status_codes_accepted:
                break
            cant_intentos += 1
        return response

    # Consulta de firma de documento XML individual
    def get_xml_signature_status(self, invoice_id):
        print(f"\nServicio: VERIFICACION DE ESTADO DE XML INDIVIDUAL {invoice_id}")

        endpoint = "/xml-status/"
        response = self.send_request(method="GET", 
                                     url=f"{self.url}{endpoint}{invoice_id}", 
                                     cdc=invoice_id)

        # print("Código de Respuesta: ", response.status_code)

        # result = f"{datetime.now()} VERIFICAR ESTADO DE XML INDIVIDUAL " \
        #    f"{response.status_code}, {response.content}"

        return response

    # Descargar XML Individual firmado
    def get_xml_signed(self, invoice_id):
        pass

    # Envio de evento
    def send_event(self, dict_parameters):
        print("\nServicio: ENVIO DE EVENTO")
        status_codes_accepted = [200, 400, 500, 503]

        cant_intentos = 1
        response = None
        while cant_intentos <= self.max_retry:
            endpoint = "/receive-event/"
            response = self.send_request(url=f"{self.url}{endpoint}", kwargs=dict_parameters)
            if response.status_code in status_codes_accepted:
                break
            cant_intentos += 1
        return response
    
    # Consulta RUC
    def get_ruc(self, ruc):
        print(f"\nServicio: OBTENEMOS EL RUC CONSULTANDO A LA SET: {ruc}")

        token = self.api_token
        endpoint = "/query-ruc/"
        response = self.send_request(method="GET", url=f"{self.url}{endpoint}{ruc}")

        return response

    def send_request(self, method="POST", url=None, token=None, **kwargs):
        try:
            payload = {}
            for key, value in kwargs.items():
                payload[key] = value

            json_payload = json.dumps(payload)

            headers = {'Content-Type': 'application/json',
                       'Accept': 'application/json', 
                       'Authorization':  f'token {self.api_token}'}

            if method == "POST":
                response = requests.post(url=url, data=json_payload, 
                                         headers=headers, timeout=None)
            elif method == "GET":
                response = requests.get(url=url, data=json_payload, 
                                        headers=headers, timeout=None)
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


def write_zip_file(proceso, list_xml_files, session, OUTPUT_PATH):
    
    path_zip_file = os.path.join(OUTPUT_PATH, 'lote.zip')
    with ZipFile(path_zip_file, 'w') as zip:
        for file_path in list_xml_files:
            file = open(file_path, "rb")
            file_content = file.read()
            file_name = os.path.split(file_path)[-1]
            zip.writestr(file_name, file_content)
            file.close()
    mensaje = f"Fue creado el archivo zip satisfactoriamente: {path_zip_file}"
    log_register(session, proceso.id, mensaje, Log.INFO)
    return path_zip_file


class RequestCustom:
    def __init__(self, status_code, content) -> None:
        self.status_code = status_code
        self.content = content
        self.text = str(content)

