import zeep
from zeep import xsd, Settings
from requests import Session
from zeep.transports import Transport
from zeep.cache import SqliteCache
from zeep.plugins import HistoryPlugin
from .cert_manager import PKCS12Manager
from lxml import etree
import base64


class SetService:
    def __init__(self, url, certificate, password):
        """
        Constructor que recibe la configuración en variables separadas
        """
        self.url_base = url
        session = Session()
        pkcs12 = PKCS12Manager(certificate, password)
        session.cert = (pkcs12.getCert(), pkcs12.getKey())
        self.transport = Transport(
                            session=session, 
                            cache=SqliteCache(), 
                            timeout=60, 
                            operation_timeout=180)
        self.history = HistoryPlugin()

    @classmethod
    def set_config(cls, set_config):
        """
        Emula constructor que recibe la configuración en un diccionario
        """
        url = set_config['URL']
        certificate = set_config['CERTIFICATE']
        password = set_config['PASSWORD']
        return cls(url, certificate, password)

    def consulta_de(self, cdc):
        wsdl = f'{self.url_base}/de/ws/consultas/consulta.wsdl?wsdl'
        client = zeep.Client(wsdl=wsdl, transport=self.transport)
        response = client.service.rEnviConsDe(dId=1, dCDC=cdc)        
        return response

    def envio_de(self, xml, id):                
        # Directamente recibimos un xml, cocinado. listo para enviarse..
        try:
            wsdl = f'{self.url_base}/de/ws/sync/recibe.wsdl?wsdl'
            client = zeep.Client(wsdl=wsdl, transport=self.transport, 
                                 plugins=[self.history])
            client.set_ns_prefix(None, "http://ekuatia.set.gov.py/sifen/xsd")
            client.wsdl.dump()
            response = client.service.rEnviDe(dId=id, xDE=xml)   
        except Exception as error:
            details = str(error)
            response = SetResponseCustom(details)
            
        return response

    def envio_lote(self, id, archivo):
        """
        Para consumir este servicio, el cliente deberá construir la estructura en XML, según el Schema siguiente y 
        comprimir dicho archivo. Cabe aclarar que el lote podrá contener hasta 50 DE del mismo tipo (ejemplo: 
        Facturas Electrónicas), cada uno de ellos debe estar firmado.

        PARÁMETROS: 
        id: Identificador de control de envío. 
            Número secuencial autoincremental, para identificación del mensaje enviado. La responsabilidad de 
            generar y controlar este número es exclusiva del contribuyente.
        archivo: Archivo de Lote comprimido. 
            Campo comprimido en formato Base64 según el esquema del Protocolo de procesamiento del Lote

        RESPUESTA:
        dFecProc: Fecha y hora de recepción. Formato: "AAAA-MM-DD-hh:mm:ss" 
        dCodRes: Código del resultado de recepción. Definido en el tópico correspondiente del capítulo 12
        dMsgRes: Mensaje del resultado de recepción. Definido en el tópico correspondiente del capítulo 12
        dProtConsLote: Número de Lote. Generado solamente si dCodRes=0300, Definido en el tópico correspondiente 
            del capítulo 12
        dTpoProces: Tiempo medio de procesamiento en segundos. Conforme a la sección correspondiente 
            en el presente manual
        """

        wsdl = f'{self.url_base}/de/ws/async/recibe-lote.wsdl?wsdl'        
        client = zeep.Client(wsdl=wsdl, transport=self.transport, plugins=[self.history])
        client.set_ns_prefix(None, "http://ekuatia.set.gov.py/sifen/xsd")
        response = client.service.rEnvioLote(dId=id, xDE=archivo)
        #req_sended = etree.tostring(self.history.last_sent["envelope"], encoding="unicode", pretty_print=True)
        #req_response = etree.tostring(self.history.last_received["envelope"], encoding="unicode", pretty_print=True)        
        return response

    def consulta_lote(self, id, nro_lote):
        wsdl = f'{self.url_base}/de/ws/consultas/consulta-lote.wsdl?wsdl'
        client = zeep.Client(wsdl=wsdl, transport=self.transport)
        response = client.service.rEnviConsLoteDe(dId=id, dProtConsLote=nro_lote)        
        return response

    def consulta_ruc(self, ruc):
        wsdl = f'{self.url_base}/de/ws/consultas/consulta-ruc.wsdl?wsdl'
        client = zeep.Client(wsdl=wsdl,transport=self.transport)
        response = client.service.rEnviConsRUC(dId=1, dRUCCons=ruc)
        return response

    def envio_evento(self, xml, id):
        # Directamente recibimos el xml del evento, cocinado. listo para enviarse..
        #path_wsdl = 'D:\\Factura Electronica\\repositorios\\paquete-fe\\set\\wsdl\\evento.wsdl'
        wsdl = f'{self.url_base}/de/ws/eventos/evento.wsdl?wsdl'
        settings = Settings(strict=False, xml_huge_tree=True)
        client = zeep.Client(wsdl=wsdl, transport=self.transport, plugins=[self.history], settings=settings)

        #client.service.rEnviEventoDe()

        #with client.settings(raw_response=True):
        #    response = client.service.rEnviEventoDe(dId=id, dEvReg=xml)
        #    # response is now a regular requests.Response object
        #    assert response.status_code == 200
        #    assert response.content

        #client = zeep.Client(wsdl=path_wsdl, transport=self.transport, settings=settings)
        #client.set_ns_prefix(None, "http://ekuatia.set.gov.py/sifen/xsd")
        #client.wsdl.dump()
        #ignorar = 'rGesEve'

        #request_data = {
        #    'dId': id,
        #    'dEvReg': xsd.SkipValue}

        #request_data = {
        #    'dId': id,
        #    'dEvReg': xml}


        #node = client.create_message(client.service, 'rEnviEventoDe', **request_data)
        #tree = etree.ElementTree(node)
        #tree.write('testxlxlxlx.xml',pretty_print=True)

        try:
            response = client.service.rEnviEventoDe(dId=id, dEvReg=xml)
        except Fault as fault:
            children = list(fault.detail)
            if len(children) == 1:
                node = children[0]
                name = etree.QName(node.tag).localname
                if hasattr(client.service.exceptions, name):
                    exception_cls = getattr(client.service.exceptions, name)
                    content = client.wsdl.types.deserialize(node)
                    raise exception_cls(content) from fault



        #xml_sended = etree.tostring(self.history.last_sent["envelope"], encoding="utf-8", pretty_print=True)
        #xml_response = etree.tostring(self.history.last_received["envelope"], encoding="utf-8", pretty_print=True)
        #root = etree.fromstring(xml_sended)
        #tree = etree.ElementTree(root)
        #tree.write("sended.xml", encoding="utf-8", pretty_print=True)
        #root = etree.fromstring(xml_response)
        #tree = etree.ElementTree(root)
        #tree.write("response.xml", encoding="utf-8", pretty_print=True)

        return response

"""
Esto seria para guardar lo enviado o tambien aplicaria para la respuesta en archivo
xml_sended = etree.tostring(self.history.last_sent["envelope"], encoding="utf-8", pretty_print=True)
xml_response = etree.tostring(self.history.last_received["envelope"], encoding="utf-8", pretty_print=True)
root = etree.fromstring(xml_sended)
tree = etree.ElementTree(root)
tree.write("sended.xml", encoding="utf-8", pretty_print=True)
root = etree.fromstring(xml_response)
tree = etree.ElementTree(root)
tree.write("response.xml", encoding="utf-8", pretty_print=True)
"""


class SetResponseCustom:
    def __init__(self, details) -> None:
        self.Id = 0
        self.details = details
        
