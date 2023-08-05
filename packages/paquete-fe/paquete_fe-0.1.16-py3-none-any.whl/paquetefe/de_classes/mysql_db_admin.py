import os
import random
import binascii
from datetime import datetime, date
import dateutil.parser
from decimal import *
import json
from lxml import etree
import sys
import traceback
import csv

from sqlalchemy import create_engine, Column, ForeignKey, String, Integer, \
                       Date, DateTime, Numeric, SmallInteger, Boolean, BigInteger
from sqlalchemy.pool import NullPool
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import desc
from .globals import isEmpty, pad_zeros, get_digito_verificador
from .utils import try_int, decimal_or_zero, try_str, int_or_same, int_or_zero, int_or_empty
from .validate import isXmlValid
from .gen_xml import CrearNodoRaiz, AgregarNodoHijo, ReemplazarNodoRaiz
from .geography_reference import (get_dict_geography, get_dict_currency, 
                                  get_dict_countries, filter_referencia_geografica)
from .settings import REUTILIZAR_CDC

getcontext().prec = 8

# Con estas lineas, se imprimen las sentencias SQL que genera y ejecuta 
# SQLALchemy por detras. Util para debug
# import logging
# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

version = "2.11.7"


class MysqlConnection:
    Base = declarative_base()

    def __init__(self, DATABASE):
        self.engine = create_engine(
            f'mysql+mysqlconnector://'
            f'{DATABASE["USER"]}:{DATABASE["PASSWORD"]}@'
            f'{DATABASE["HOST"]}:{DATABASE["PORT"]}/'
            f'{DATABASE["NAME"]}',
            pool_recycle=3600,
            pool_size=100, max_overflow=20
            #poolclass=NullPool
        )

    def connect(self):
        Session = sessionmaker()
        Session.configure(bind=self.engine)
        session = Session()
        # self.create_tables(session)
        return session

    def create_tables(self, session):
        self.Base.metadata.create_all(self.engine)
        session.commit()


class Proceso(MysqlConnection.Base):
    __tablename__ = 'proc_proceso'

    id = Column(Integer, primary_key=True)
    fecha_hora_inicio = Column(DateTime, nullable=True)
    fecha_hora_fin = Column(DateTime, nullable=True)
    estado = Column(String(50), nullable=True)
    cant_documentos = Column(Integer, nullable=True)
    id_lote_cima = Column(Integer, nullable=True)
    uuid_lote = Column(String(36), nullable=True)
    fecha_minima_revision = Column(DateTime, nullable=True)
    tipo_proceso = Column(String(30), nullable=True)
    origen = Column(String(100), nullable=True)
    tipo_servicio = Column(String(1), nullable=True)
    notificado = Column(Boolean, nullable=True, default=0)
    publicado = Column(Boolean, nullable=True, default=0)
    documentos = relationship("De")
    logs = relationship("Log")
    archivos = relationship("Archivo")

    PROCESANDO = 'PROCESANDO'
    PROCESADO = 'PROCESADO'
    PENDIENTE_APROBACION = 'PENDIENTE_APROBACION'
    VERIFICANDO_APROBACION = 'VERIFICANDO_APROBACION'
    ACTUALIZANDO_ESTADOS = 'ACTUALIZANDO_ESTADOS'
    PENDIENTE_OBTENER_ZIP = 'PENDIENTE_OBTENER_ZIP'
    PENDIENTE_ACTUALIZAR_QR = 'PENDIENTE_ACTUALIZAR_QR'
    ACTUALIZANDO_QR = 'ACTUALIZANDO_QR'
    QR_ACTUALIZADO = 'QR_ACTUALIZADO'
    CREANDO_DAT = 'CREANDO_DAT'
    FINALIZADO = 'FINALIZADO'
    FINALIZADO_ERROR = 'FINALIZADO_ERROR'
    # NEW_DAT_GENERATED = 'NEW_DAT_GENERATED'


class De(MysqlConnection.Base):

    def __init__(self):
        self.x_error = ''
        self.dSalAnt = 0        
        self.dSubExe = 0
        self.dSubExo = 0
        self.dSub5 = 0
        self.dSub10 = 0
        self.dTotOpe = 0
        self.dTotDesc = 0
        self.dTotDescGlotem = 0
        self.dTotAntItem = 0
        self.dTotAnt = 0
        self.dDescTotal = 0
        self.dAnticipo = 0
        self.dRedon = 0
        self.dTotGralOpe = 0
        self.dIVA5 = 0
        self.dIVA10 = 0
        self.dLiqTotIVA5 = 0
        self.dLiqTotIVA10 = 0
        self.dTotIVA = 0
        self.dBaseGrav5 = 0
        self.dBaseGrav10 = 0
        self.dTBasGraIVA = 0
        self.dTotalGs = 0
        self.dPorcDescTotal = 0        

    dict_geography = get_dict_geography()

    __tablename__ = 'de_documento_electronico'
    id = Column(Integer, primary_key=True)
    proceso_id = Column(Integer, ForeignKey('proc_proceso.id'))
    dVerFor = Column(Numeric(3), nullable=True)
    _Id = Column(String(44), nullable=True)
    dDVId = Column(Integer, nullable=True)
    dFecFirma = Column(DateTime, nullable=True)
    dSisFact = Column(Numeric(1), nullable=True)
    iTipEmi = Column(Numeric(1), nullable=True)
    dDesTipEmi = Column(String(12), nullable=True)
    dCodSeg = Column(Numeric(9), nullable=True)
    dInfoEmi = Column(String(3000), nullable=True)
    dInfoFisc = Column(String(3000), nullable=True)
    iTiDE = Column(Numeric(2), nullable=True)
    dDesTiDE = Column(String(40), nullable=True)
    dNumTim = Column(Numeric(8), nullable=True)
    dEst = Column(String(3), nullable=True)
    dPunExp = Column(String(3), nullable=True)
    dNumDoc = Column(String(7), nullable=True)
    dSerieNum = Column(String(2), nullable=True)
    dFeIniT = Column(Date, nullable=True)
    #dFeFinT = Column(Date, nullable=True)
    dFeEmiDE = Column(DateTime, nullable=True)
    iTipTra = Column(Numeric(2), nullable=True)
    dDesTipTra = Column(String(50), nullable=True)
    iTImp = Column(Numeric(1), nullable=True)
    dDesTImp = Column(String(7), nullable=True)
    cMoneOpe = Column(String(3), nullable=True)
    dDesMoneOpe = Column(String(20), nullable=True)
    dCondTiCam = Column(Numeric(1), nullable=True)
    dTiCam = Column(Numeric(9, 4), nullable=True)
    iCondAnt = Column(Numeric(1), nullable=True)
    dDesCondAnt = Column(String(17), nullable=True)
    dRucEm = Column(String(8), nullable=True)
    dDVEmi = Column(Integer, nullable=True)
    iTipCont = Column(Numeric(1), nullable=True)
    cTipReg = Column(Numeric(2), nullable=True)
    dNomEmi = Column(String(255), nullable=True)
    dNomFanEmi = Column(String(255), nullable=True)
    dDirEmi = Column(String(255), nullable=True)
    dNumCas = Column(Numeric(6), nullable=True)
    dCompDir1 = Column(String(255), nullable=True)
    dCompDir2 = Column(String(255), nullable=True)
    cDepEmi = Column(Numeric(2), nullable=True)
    dDesDepEmi = Column(String(16), nullable=True)
    cDisEmi = Column(Numeric(4), nullable=True)
    dDesDisEmi = Column(String(30), nullable=True)
    cCiuEmi = Column(Numeric(5), nullable=True)
    dDesCiuEmi = Column(String(30), nullable=True)
    dTelEmi = Column(Numeric(15), nullable=True)
    dEmailE = Column(String(80), nullable=True)
    dDenSuc = Column(String(30), nullable=True)
    iNatRec = Column(Numeric(1), nullable=True)
    iTiOpe = Column(Numeric(1), nullable=True)
    cPaisRec = Column(String(3), nullable=True)
    dDesPaisRe = Column(String(50), nullable=True)
    iTiContRec = Column(Numeric(1), nullable=True)
    dRucRec = Column(String(8), nullable=True)
    dDVRec = Column(Integer, nullable=True)
    iTipIDRec = Column(Numeric(1), nullable=True)
    dDTipIDRec = Column(String(42), nullable=True)
    dNumIDRec = Column(String(20), nullable=True)
    dNomRec = Column(String(255), nullable=True)
    dNomFanRec = Column(String(255), nullable=True)
    dDirRec = Column(String(255), nullable=True)
    dNumCasRec = Column(Numeric(6), nullable=True)
    cDepRec = Column(Numeric(2), nullable=True)
    dDesDepRec = Column(String(16), nullable=True)
    cDisRec = Column(Numeric(4), nullable=True)
    dDesDisRec = Column(String(30), nullable=True)
    cCiuRec = Column(Numeric(5), nullable=True)
    dDesCiuRec = Column(String(30), nullable=True)
    dTelRec = Column(String(15), nullable=True)
    dCelRec = Column(String(20), nullable=True)
    dEmailRec = Column(String(80), nullable=True)
    dCodCliente = Column(String(15), nullable=True)
    iIndPres = Column(Numeric(1), nullable=True)
    dDesIndPres = Column(String(30), nullable=True)
    dFecEmNR = Column(DateTime, nullable=True)
    iMotEmi = Column(Numeric(2), nullable=True)
    dDesMotEmi = Column(String(35), nullable=True)
    #dKmR = Column(Numeric(5), nullable=True)
    #dFecEm = Column(Date, nullable=True)
    iCondOpe = Column(Numeric(1), nullable=True)
    dDCondOpe = Column(String(7), nullable=True)
    iCondCred = Column(Numeric(1), nullable=True)
    dDCondCred = Column(String(6), nullable=True)
    dPlazoCre = Column(String(15), nullable=True)
    dCuotas = Column(Integer, nullable=True)
    dMonEnt = Column(Numeric(19, 4), nullable=True)
    dCiclo = Column(String(15), nullable=True)
    dFecIniC = Column(Date, nullable=True)
    dFecFinC = Column(Date, nullable=True)
    dVencPag = Column(Date, nullable=True)
    dContrato = Column(String(30), nullable=True)
    dSalAnt = Column(Numeric(19, 4), nullable=True)
    dSubExe = Column(Numeric(23, 8), nullable=True)
    dSubExo = Column(Numeric(23, 8), nullable=True)
    dSub5 = Column(Numeric(23, 8), nullable=True)
    dSub10 = Column(Numeric(23, 8), nullable=True)
    dTotOpe = Column(Numeric(23, 8), nullable=True)
    dTotDesc = Column(Numeric(23, 8), nullable=True)
    dTotDescGlotem = Column(Numeric(23, 8), nullable=True)
    dTotAntItem = Column(Numeric(23, 8), nullable=True)
    dTotAnt = Column(Numeric(23, 8), nullable=True)
    dPorcDescTotal = Column(Numeric(11, 8), nullable=True)
    dDescTotal = Column(Numeric(23, 8), nullable=True)
    dAnticipo = Column(Numeric(23, 8), nullable=True)
    dRedon = Column(Numeric(7, 4), nullable=True)
    dComi = Column(Numeric(23, 8), nullable=True)
    dTotGralOpe = Column(Numeric(23, 8), nullable=True)
    dIVA5 = Column(Numeric(23, 8), nullable=True)
    dIVA10 = Column(Numeric(23, 8), nullable=True)
    dLiqTotIVA5 = Column(Numeric(23, 8), nullable=True)
    dLiqTotIVA10 = Column(Numeric(23, 8), nullable=True)
    dIVAComi = Column(Numeric(23, 8), nullable=True)
    dTotIVA = Column(Numeric(23, 8), nullable=True)
    dBaseGrav5 = Column(Numeric(23, 8), nullable=True)
    dBaseGrav10 = Column(Numeric(23, 8), nullable=True)
    dTBasGraIVA = Column(Numeric(23, 8), nullable=True)
    dTotalGs = Column(Numeric(23, 8), nullable=True)
    dCarQR = Column(String(600), nullable=True)
    x_nro_cuenta = Column(String(10), nullable=True)
    x_corte = Column(String(8), nullable=True)
    x_estado = Column(String(3), nullable=True)
    x_error = Column(String(1000), nullable=True)
    x_corregido = Column(Boolean, nullable=True, default=0)
    x_tipo_doc = Column(String(3), nullable=True)
    x_codigo_cia = Column(Integer, nullable=True)
    dInfAdic = Column(String(5000), nullable=True)
    xml_file_name = Column(String(255), nullable=True)
    nro_lote_set = Column(BigInteger, nullable=True)
    protocolo_set = Column(BigInteger, nullable=True)
    notificado_receptor = Column(Boolean, nullable=True, default=0)
    input_file_name = Column(String(255), nullable=True)
    items = relationship("Item")
    actividades = relationship("Actividad")
    documentos = relationship("DocumentoAsociado")
    medios_pago = relationship("MedioPago")
    compra_publica = relationship("ComprasPublicas", uselist=False, back_populates="de")
    autofactura = relationship("Autofactura", uselist=False, back_populates="de")
    nota_remision = relationship("NotaRemision", uselist=False, back_populates="de")
    cuotas = relationship("Cuotas")
    transporte_mercaderia = relationship("TransporteMercaderias", uselist=False, back_populates="de")
    # salida_mercaderia = relationship("SalidaMercaderias", uselist=False, back_populates="de")
    # local_entrega_mercaderia = relationship("LocalEntregaMercaderias")
    # vehiculo_mercaderia = relationship("VehiculoMercaderias")
    # transportista = relationship("Transportista", uselist=False, back_populates="de")

    ERROR_PREVALIDACION_INTERNA = 'EPI'
    GENERADO = 'GEN'
    EMITIDO = 'EMI'
    PENDIENTE_APROBACION = 'PEA'
    ERROR_PREVALIDACION_EXTERNA = 'EPE'
    APROBADO = 'APR'
    APROBADO_OBS = 'APO'
    RECHAZADO = 'REC'
    ANULADO = 'ANU'

    dict_geography = get_dict_geography()
    dict_currency = get_dict_currency()
    dict_countries = get_dict_countries()

    def reutilizar_cdc_documento_corregido(self, session):
        '''                       
            CHANGED: Si existe el mismo dNumDoc registrado previamente, reutiliza directamente.
            No se tendra en cuenta el estado en el que se encuentra el documento previo...
            Se toma solo el último

        '''

        #dNumDocs = (session.query(De).filter_by(dNumDoc=self.dNumDoc,
        #                                        iTiDE=self.iTiDE)
        #                            .order_by(desc(De.id))
        #                            .first())

        dNumDocs = (session.query(De).filter_by(
                                        iTiDE=self.iTiDE,
                                        dEst=self.dEst,
                                        dPunExp=self.dPunExp,
                                        dNumDoc=self.dNumDoc)
                                     .order_by(De.id.desc())
                                     .first())
        return dNumDocs
            
                
    def set_constantes(self):
        self.dVerFor = '150'

    def getId(self, session):
        """
        -El atributo Id es el Identificador del DE (atributo del Tag DE) CDC (Código de Control)
        1) Tipo de documento 2)Ruc del emisor 3)DV del emisor 4) Establecimiento 5)Punto de expedición
        6)Numero de Documento 7)Tipo de Contribuyente 8)Fecha de emision 9)Tipo de Emision
        10)Codigo de seguridad 11)Digito Verificador
        Longitud del CDC = 44
        """

        '''
        CHANGED    
            Se definio reutilizar el CDC si existe un dNumDoc ya utilizado, sin importar el estado, solo se debe validar que 
            los campos que conforman la creacion del CDC sigan siendo iguales.. sino, se debe crear OTRO CDC.
                       
        '''

        if REUTILIZAR_CDC:
            documento_previo = self.reutilizar_cdc_documento_corregido(session)
            if documento_previo:
                if (str(self.iTiDE) != str(documento_previo.iTiDE)
                        or str(self.dRucEm) != str(documento_previo.dRucEm)
                        or str(self.dDVEmi) != str(documento_previo.dDVEmi)
                        or self.dEst != documento_previo.dEst
                        or self.dPunExp != documento_previo.dPunExp
                        or self.dNumDoc != documento_previo.dNumDoc
                        or str(self.iTipCont) != str(documento_previo.iTipCont)
                        or datetime.strptime(self.dFeEmiDE, "%Y-%m-%dT%H:%M:%S").date() != documento_previo.dFeEmiDE.date()
                        or str(self.iTipEmi) != str(documento_previo.iTipEmi)
                        or documento_previo._Id == "0" * 44
                        ):                    
                    return self.generar_cdc()
                else:
                    self.dCodSeg = str(documento_previo.dCodSeg)
                    self.dDVId = str(documento_previo.dDVId)
                    self._Id = documento_previo._Id
                    return self._Id
            else:
                return self.generar_cdc()
        else:
            return self.generar_cdc()

    def generar_cdc(self):
        self.dCodSeg = self.getdCodSeg()

        dict_id_fields = {"TipoDocumento": self.iTiDE,
                          "RucEmisor": self.dRucEm,
                          "DVEmisor": self.dDVEmi,
                          "Establecimiento": self.dEst,
                          "PuntoExpedicion": self.dPunExp,
                          "NumeroDocumento": self.dNumDoc,
                          "TipoContribuyente": self.iTipCont,
                          "FechaEmision": self.dFeEmiDE,
                          "TipoEmision": self.iTipEmi,
                          "CodigoSeguridad": self.dCodSeg}

        for k, v in dict_id_fields.items():
            if not v and v != 0:
                print("No puede estar vacio el campo: ", k)
                self.x_estado = self.ERROR_PREVALIDACION_INTERNA
                self.x_error += f"ERROR en getId(): No puede estar vacio el campo: {k} "

        iTiDE = pad_zeros(self.iTiDE, 2)
        dRucEm = try_str(self.dRucEm).zfill(8)
        dDVEmi = int_or_empty(self.dDVEmi)
        dEst = self.dEst
        dPunExp = self.dPunExp
        dNumDoc = self.dNumDoc
        iTipCont = int_or_empty(self.iTipCont)
        dFeEmiDE = self._get_CDC_format_date(self.dFeEmiDE)
        iTipEmi = int_or_empty(self.iTipEmi)
        dCodSeg = self.dCodSeg

        v_cdc = f"{iTiDE}{dRucEm}{dDVEmi}{dEst}{dPunExp}{dNumDoc}{iTipCont}{dFeEmiDE}{iTipEmi}{dCodSeg}"

        v_VDigit = self.getVDigit(v_cdc)  # El digito verificador se obtiene a partir del CDC, y luego se completa
        self.dDVId = v_VDigit
        v_cdc = "{}{}".format(v_cdc, v_VDigit)
        v_len_cdc = len(v_cdc)

        if (v_len_cdc != 44):
            print("La longitud del CDC debe ser de 44 caracteres y la longitud generada es de: ", v_len_cdc)
            self.x_estado = self.ERROR_PREVALIDACION_INTERNA
            self.x_error += f"ERROR en getId(): La longitud del CDC debe ser de 44 caracteres y " \
                f"la longitud generada es de: {v_len_cdc}"
        self._Id = v_cdc
        return v_cdc

    def get_datos_cdc(self):
        self.dCodSeg = self._Id[34:43]
        self.dDVId = self._Id[43]
    
    def _get_CDC_format_date(self, fecha):
        """
        -Recibe una fecha en formato iso 'YYYY-MM-DDTHH:MM:SS.mmmmmm' 
            o una fecha
        -Retorna fecha en formato YYYYMMDD
        """
        if not isinstance(fecha, datetime):
            fecha = dateutil.parser.parse(fecha)
            
        return datetime.strftime(fecha, '%Y%m%d')

    def get_short_iso_format(self, fecha):
        """
        -Recibe una fecha en formato iso 'YYYY-MM-DDTHH:MM:SS.mmmmmm' 
            o una fecha
        -Retorna fecha en formato YYYY-MM-DD
        """
        if not isinstance(fecha, datetime) and not isinstance(fecha, date):
            if not fecha:
                return ''
            try:
                fecha = dateutil.parser.parse(fecha)
            except:
                return fecha
        return datetime.strftime(fecha, '%Y-%m-%d')

    def get_isoformat(self, fecha):
        """
        -Recibe una fecha en formato texto 'YYYY-MM-DDTHH:MM:SS.mmmmmm' 
            o una fecha
        -Retorna fecha en formato fecha 'YYYY-MM-DDTHH:MM:SS.mmmmmm'
        """
        if not fecha:
            return None
        if not isinstance(fecha, datetime) and not isinstance(fecha, date):
            fecha = dateutil.parser.parse(fecha)
        return fecha.isoformat()

    #Dichoso algoritmo 11, que sirve para obtener el digito verificador de varios campos
    def getVDigit(self, numero):
        if isEmpty(numero):
            print("ERROR en getVDigit(): No se puede obtener el digito verificador sin tener el valor del numero")
            self.x_estado = self.ERROR_PREVALIDACION_INTERNA
            self.x_error += f"ERROR en getVDigit(): No se puede obtener el digito verificador sin tener el valor del numero"

        digito_verificador = get_digito_verificador(numero)
        return str(digito_verificador)			

    def getdFecFirma(self):
        """
            Fecha y hora de la firma digital.
        """
        self.dFecFirma = "1970-01-01T00:00:00"
        return self.dFecFirma

    def getdCodSeg(self):
        """
        -Código generado por el emisor de manera aleatoria para asegurar la 
        confidencialidad de la consulta pública del DE
        -Se genera en base a la especificación del Manual Tecnico. Pag. 56
        -Debe ser un número Aleatorio, positivo de 9 dígitos.
        -Debe ser distinto para cada DE y generado por un algoritmo de 
        complejidad suficiente para evitar la reproducción del valor
        -Rango NO SECUENCIAL entre 000000001 y 999999999
        -No tener relación con ninguna información específica o directa 
        del DE o del emisor de manera a garantizar su seguridad
        -No debe ser igual al número de documento campo dNumDoc
        -En caso de ser un número de menos de 9 dígitos completar con 0 a 
        la izquierda
        """
        v_num_valid = False
        v_rand = 0
        while v_num_valid == False:
            v_rand = random.randrange(1, 999999999)
            if(self.dNumDoc != v_rand and len(str(v_rand)) == 9):
                v_num_valid = True
        dCodSeg = pad_zeros(v_rand,9)
        return dCodSeg

    def getdDesTiDE(self):
        dic_des_tip_docu = {"1": "Factura electrónica",
                            "2": "Factura electrónica de exportación",
                            "3": "Factura electrónica de importación",
                            "4": "Autofactura electrónica",
                            "5": "Nota de crédito electrónica",
                            "6": "Nota de débito electrónica",
                            "7": "Nota de remisión electrónica",
                            "8": "Comprobante de retención electrónico"}
                 
        if not self.iTiDE:
            print("ERROR en getdDesTiDE(): No puede estar vacio el campo iTiDE " \
                    f"(Tipo de Documento Electrónico) para obtener su descripcion")
            self.x_estado = self.ERROR_PREVALIDACION_INTERNA
            self.x_error += f"ERROR en getdDesTiDE(): No puede estar vacio el campo iTiDE " \
                f"(Tipo de Documento Electrónico) para obtener su descripcion"
        else:
            # Obtenemos solo si está vacío el campo descripción, 
            # sino dejamos el que vino de la fuente
            if not self.dDesTiDE: 
                self.dDesTiDE = dic_des_tip_docu.get(str(self.iTiDE))
            return self.dDesTiDE
        
    def getdDesTipTra(self):
        dic_des_tip_transac = {1: "Venta de mercadería",
                               2: "Prestación de servicios",
                               3: "Mixto (Venta de mercadería y servicios)",
                               4: "Venta de activo fijo",
                               5: "Venta de divisas",
                               6: "Compra de divisas",
                               7: "Promoción o entrega de muestras",
                               8: "Donación",
                               9: "Anticipo",
                              10: "Compra de productos",
                              11: "Compra de servicios",
                              12: "Venta de crédito fiscal",
                              13: "Muestras médicas (Art. 3 RG 24/2014)"}
    
        if self.iTipTra:
            # Obtenemos solo si está vacío el campo descripción, 
            # sino dejamos el que vino de la fuente
            if not self.dDesTipTra:
                self.dDesTipTra = dic_des_tip_transac.get(try_int(self.iTipTra))
            return self.dDesTipTra
        else:
            """
            Comento esto para probar
            print("ERROR en getdDesTipTra(): Es obligatorio solamente en caso que exista el campo iTipTra")
            self.x_estado = self.ERROR_PREVALIDACION_INTERNA
            self.x_error += f"ERROR en getdDesTipTra(): Es obligatorio solamente en caso que exista el campo iTipTra"
            """
            return ''

    def get_dPlazoCre(self):
        vencimiento = datetime.strptime(self.dVencPag, '%Y-%m-%d')
        emision = datetime.strptime(self.dFeEmiDE, '%Y-%m-%dT%H:%M:%S')
        dias = (vencimiento - emision).days
        return f"{dias} días"

    def getdDTipIDRec(self):
        """
        -Descripción del tipo de documento de identidad. Obligatorio  si  existe  el  campo D208
        -Si D208 = 7 informar el tipo de documento de identidad del receptor. Cómo? DE DÓNDE quitamos ese valor? 
        """
        dic_des_tip_docu = {1: "Cédula paraguaya",
                            2: "Pasaporte",
                            3: "Cédula extranjera",
                            4: "Carnet de residencia",
                            5: "Innominado",
                            6: "Tarjeta Diplomática de exoneración fiscal",
                            7: "Otro"}

        if self.iTipIDRec:
            # Obtenemos solo si está vacío el campo descripción, 
            # sino dejamos el que vino de la fuente
            if not self.dDTipIDRec:
                self.dDTipIDRec = dic_des_tip_docu.get(try_int(self.iTipIDRec))
            return self.dDTipIDRec

    def getdDesIndPres(self):
        """
        -Descripción del indicador de presencia
        -Si iIndPres = 9 informar el indicador de presencia
        """
        dic_dDesIndPres = {
            "1": "Operación presencial",
            "2": "Operación electrónica",
            "3": "Operación telemarketing",
            "4": "Venta a domicilio ",
            "5": "Operación bancaria",
            "6": "Operación cíclica",
        }

        if self.iIndPres:
            # Obtenemos solo si está vacío el campo descripción, 
            # sino dejamos el que vino de la fuente
            if not self.dDesIndPres:
                self.dDesIndPres = dic_dDesIndPres.get(str(self.iIndPres), '')
            return self.dDesIndPres

    def getdDCondOpe(self):
        """
        -Descripción de la condición de operación 
        -Referente al campo iCondOpe
        """
        dic_descripciones = {
            "1": "Contado",
            "2": "Crédito",
        }

        if self.iCondOpe:
            # Obtenemos solo si está vacío el campo descripción, 
            # sino dejamos el que vino de la fuente
            if not self.dDCondOpe:
                self.dDCondOpe = dic_descripciones.get(str(self.iCondOpe), '')
            return self.dDCondOpe
        
        
    def getcDisRec(self):
        """
        -Código del distrito del receptor
        -Según Tabla 2.1 – Distritos Debe corresponder a lo declarado en el RUC
        -Según respuesta, no sé que valor debemos asignar 
        """
        return "1"

    def getdDesDisRec(self):
        """
        -Descripción del distrito del receptor
        -Obligatorio si existe el campo D220. Debe corresponder a lo declarado en el RUC
        -Según respuesta, no sé que valor debemos asignar
        """
        return "1"

    def getcCiuRec(self):
        """
        -Código de la ciudad del receptor
        -Según Tabla 2.2 – Ciudades Debe corresponder a lo declarado en el RUC
        -Según respuesta, no sé que valor debemos asignar
        """
        return "1"

    def getdDesCiuRec(self):
        """
        -Descripción de la ciudad del receptor
        -Referente al campo D222 Debe corresponder a lo declarado en el RUC
        -Según respuesta, no sé que valor debemos asignar
        """
        return "1"

    def getdTelRec(self):
        """
        -Número de teléfono del receptor
        -Debe incluir el prefijo de la ciudad si D203 = PRY
        -No se indica de donde obtener este valor
        """
        return ""

    def get_dDesMotEmi(self):
        """
        Descripción  del  motivo de emisión
        """
        dic_des_iMotEmi = {1: "Devolución y Ajuste de precios",
                           2: "Devolución",
                           3: "Descuento",
                           4: "Bonificación",
                           5: "Crédito incobrable",
                           6: "Recupero de costo",
                           7: "Recupero de gasto",
                           8: "Ajuste de precio"}

        if self.iMotEmi:
            # Obtenemos solo si está vacío el campo descripción, 
            # sino dejamos el que vino de la fuente
            if not self.dDesMotEmi:
                self.dDesMotEmi = dic_des_iMotEmi.get(try_int(self.iMotEmi))
            return self.dDesMotEmi
        else:
            mensaje = "Obligatorio si C002 = 5 o 6 (NCE y NDE) No informar si C002 ≠ 5 o 6"
            # TODO ver si hacemos saltar alguna pre-validación aquí o ya se controla 
            # iMotEmi en otra parte del código

    def getdPlazoCre(self):
        """
        -Plazo del crédito
        -Obligatorio si E641 = 1 Ejemplo: 30 días, 12 meses
        -En este caso iCondCred = 1 (Valor Constante), siempre dara True la condición, pero igual se incluye
        la validación mencionada en el excel.
        """
        if self.iCondCred == 1:
            v_cant_dias = abs(self.dVencPag-self.dFeEmiDE).days
            return "{}{}".format(v_cant_dias, " días")
        else:
            print("Solamente es obligatorio si E641(iCondCred) = 1")
            self.x_estado = self.ERROR_PREVALIDACION_INTERNA
            self.x_error += f"ERROR en getdPlazoCre(): Solamente es obligatorio si E641(iCondCred) = 1"

    def getRoundedValue(self, mount):
        #Obtenemos los dos ultimos digitos (Revisar!)	
        lastDigits = abs(mount) % 100
        if lastDigits < 50:
            return mount - lastDigits
        elif lastDigits > 50 and lastDigits <= 99:
            return mount - (50 - lastDigits) 
        else:
            return mount	

    def getdTotGralOpe(self):
        """
        -Corresponde al cálculo aritmético F008 - F013 + F025 (dTotOpe - dRedon + dComi)
        -Calcular Total Bruto menos redondeo
        """
        if not self.dTotOpe:
            self.dTotOpe = 0
        if not self.dRedon:
            self.dRedon = 0
        if not self.dComi:
            self.dComi = 0

        self.dTotGralOpe = round(float(self.dTotOpe) - float(self.dRedon) + float(self.dComi), 8)
        return self.dTotGralOpe

    def getdNomRec(self):
        """
        Nombre o razón social del receptor del DE
        En  caso  de  DE  innominado, completar con “Sin Nombre”	
        """
        if not self.dNomRec:
            self.dNomRec = "Sin Nombre"
        return self.dNomRec
     
    
    def getdCarQR(self):
        """
        -Caracteres correspondientes al código QR
        -Codigo QR
        -Mientras ponemos el del xml de ejemplo para que pase la revisiónd del XSD
        """

        #dFeEmiDE_hex = self.dFeEmiDE.isoformat().encode("utf-8").hex()
        dFeEmiDE_hex = self.dFeEmiDE.encode("utf-8").hex()

        if self.dRucRec:
            ci_ruc = f"dRucRec={self.dRucRec}"
        #elif self.dNumIDRec or str(self.dNumIDRec) == '0':
        elif self.dNumIDRec or (try_int(self.dNumIDRec) == 0):
            ci_ruc = f"dNumIDRec={self.dNumIDRec}"
        else:
            # En caso de que estos campos no contengan valor completar con un “0”
            ci_ruc = 'dNumIDRec=0'

        if not self.dTotIVA:
            self.dTotIVA = 0

        cant_items = len(self.items)

        self.dCarQR = f"nVersion=150|Id={self._Id}|dFeEmiDE={dFeEmiDE_hex}|{ci_ruc}|dTotGralOpe={self.dTotGralOpe}|dTotIVA={self.dTotIVA}|cItems={cant_items}|DigestValue=@DigestValue@|IdCSC=@IdCSC@"
        return self.dCarQR

    def generategCamIVA(self):
        """
        D013 = iTImp (Tipo de impuesto afectado):
            1= IVA
            2= ISC
            3=Renta 
            4=Ninguno
            5=IVA - Renta
        
        C002 = iTiDE (Tipo de Documento Electrónico)
            1= Factura electrónica  
            2= Factura electrónica de exportación (Futuro)
            3= Factura electrónica de importación (Futuro)
            4= Autofactura electrónica
            5= Nota de crédito electrónica 
            6= Nota de débito electrónica 
            7= Nota de remisión electrónica
            8= Comprobante de retención electrónico (Futuro)

        Obligatorio si D013=1, 3, 4 o 5 y C002 ≠ 4 o 7
        No informar si D013=2 y C002= 4 o 7		
        """

        #Agregado porque no se debe informar cuando es Nota de remision
        if not self.iTImp:
            return False

        if isinstance(self.iTImp, str):
            self.iTImp = int(self.iTImp)
        #self.iTImp = int(self.iTImp)
        if (self.iTImp == 1 or self.iTImp == 3 or self.iTImp == 4 or self.iTImp == 5) and (self.iTiDE != 4 and self.iTiDE != 7):
            return True
        elif self.iTImp == 2 and (self.iTiDE == 4 or self.iTiDE == 7):
            return False
        else:
            return False

    def getdDesTipDocAso(self):
        dic_des_tip_docu_aso = {1: "Electrónico",
                                2: "Impreso",
                                3: "Constancia Electrónica"}

        if not self.iTipDocAso:
            print("No puede estar vacio el campo iTipDocAso (Tipo de documento asociado) para obtener su descripcion")
        else:
            self.dDesTipDocAso = dic_des_tip_docu_aso.get(self.iTipDocAso)
            return self.dDesTipDocAso

    def get_dDesTImp(self):
        # Descripción   del   tipo de impuesto afectado
        # Obtenemos solo si está vacío el campo descripción, 
        # sino dejamos el que vino de la fuente
        if not self.dDesTImp:
            dic_dDesTImp = {"1": "IVA",
                            "2": "ISC",
                            "3":"Renta",
                            "4":"Ninguno",
                            "5":"IVA - Renta"}
        
            self.dDesTImp = dic_dDesTImp.get(str(self.iTImp))
            return self.dDesTImp
        else:
            return self.dDesTImp
        

    def get_dDCondCred(self):
        # Descripción de la condición de la operación a crédito
        # Obtenemos solo si está vacío el campo descripción, 
        # sino dejamos el que vino de la fuente
        if not self.dDCondCred:
            dic_dDCondCred = {"1": "Plazo",
                              "2": "Cuota"}
        
            self.dDCondCred = dic_dDCondCred.get(str(self.iCondCred))
            return self.dDCondCred
        else:
            return self.dDCondCred

    def get_datos_geograficos(self):
        """
        Si se envió los códigos de ciudades, departamento o  distrito y no 
        tiene las descripciones obtenerlos
        """
        if self.cDepRec and not self.dDesDepRec:
            linea = filter_referencia_geografica('COD_DEPARTAMENTO', self.cDepRec)
            self.dDesDepRec = linea.get('DEPARTAMENTO', '')
        
        if self.cDisRec and not self.dDesDisRec:
            linea = filter_referencia_geografica('COD_DISTRITO', self.cDisRec)
            self.dDesDisRec = linea.get('DISTRITO', '')

        if self.cCiuRec and not self.dDesCiuRec:
            linea = filter_referencia_geografica('COD_CIUDAD', self.cCiuRec)
            self.dDesCiuRec = linea.get('CIUDAD', '')


    def calculate_dSubExe(self):
        try:
            dSubExe = 0
            for item in self.items:
                if item.iAfecIVA == 3:
                    dSubExe += decimal_or_zero(item.dTotOpeItem)
            return dSubExe
        except:
            return 0

    def calculate_dSub5(self):
        try:
            dSub5 = 0
            for item in self.items:
                if (item.iAfecIVA in (1, 4) 
                        and item.dTasaIVA == 5 
                        and (self.iTImp == 1 or self.iTImp == 5)):
                    dSub5 += decimal_or_zero(item.dTotOpeItem)
            return dSub5
        except:
            return 0

    def calculate_dSub10(self):
        try:
            dSub10 = 0
            for item in self.items:
                if (item.iAfecIVA in (1, 4)
                        and item.dTasaIVA == 10
                        and (self.iTImp == 1 or self.iTImp == 5)):
                    dSub10 += decimal_or_zero(item.dTotOpeItem)
            return dSub10
        except:
            return 0

    def calculate_dTotOpe(self):
        try:
            if self.iTImp in (1, 3, 4, 5):
                dTotOpe = (decimal_or_zero(self.dSubExe) + 
                                decimal_or_zero(self.dSubExo) +
                                decimal_or_zero(self.dSub5) +
                                decimal_or_zero(self.dSub10))
            
            if self.iTiDE == 4:
                dTotOpe = 0
                for item in self.items:
                    dTotOpe += decimal_or_zero(item.dTotOpeItem)
            
            return dTotOpe
        except:
            return 0


    def calculate_dTotDesc(self):
        """
            Suma de todos los descuentos particulares por ítem (dDescItem)
            Calculo debe ser igual la suma de todas las ocurrencias de dDescItem 
            multiplicado por la cantidad es decir: dDescItem * dCantProSer
        """
        try:
            dTotDesc = 0
            for item in self.items:
                descuento_item = decimal_or_zero(item.dDescItem)
                cantidad = decimal_or_zero(item.dCantProSer)
                descuento = descuento_item * cantidad  
                dTotDesc += descuento
                
            valor = round(dTotDesc, 8)
            return valor
        except Exception as error:
            return 0

    def calculate_dTotDescGlotem(self):
        try:
            dTotDescGlotem = 0
            for item in self.items:
                dTotDescGlotem += decimal_or_zero(item.dDescGloItem)
            return dTotDescGlotem
        except:
            return 0

    def calculate_dTotAntItem(self):
        try:
            dTotAntItem = 0
            for item in self.items:
                dTotAntItem += decimal_or_zero(item.dAntPreUniIt)
            return dTotAntItem
        except:
            return 0

    def calculate_dTotAnt(self):
        try:
            dTotAnt = 0
            for item in self.items:
                dTotAnt += decimal_or_zero(item.dAntGloPreUniIt)
            return dTotAnt
        except:
            return 0

    def calculate_dDescTotal(self):
        try:
            dDescTotal = 0
            for item in self.items:
                dDescTotal += decimal_or_zero(item.dDescItem) * decimal_or_zero(item.dCantProSer) + decimal_or_zero(item.dDescGloItem)
            return round(dDescTotal, 8)
        except:
            return 0

    def calculate_dAnticipo(self):
        try:
            dAnticipo = 0
            for item in self.items:
                dAnticipo += decimal_or_zero(item.dAntPreUniIt) + decimal_or_zero(item.dAntGloPreUniIt)
            return dAnticipo
        except:
            return 0

    def calculate_dTotGralOpe(self):
        try:
            dTotGralOpe = (decimal_or_zero(self.dTotOpe)
                            - decimal_or_zero(self.dRedon) 
                            + decimal_or_zero(self.dComi))
            return round(dTotGralOpe, 8)
        except:
            return 0

    def calculate_dIVA5(self):
        try:
            dIVA5 = 0
            for item in self.items:
                if item.dTasaIVA == 5:
                    dIVA5 += decimal_or_zero(item.dLiqIVAItem)
            return round(dIVA5, 8)
        except:
            return 0

    def calculate_dIVA10(self):
        try:
            dIVA10 = 0
            for item in self.items:
                if item.dTasaIVA == 10:
                    dIVA10 += decimal_or_zero(item.dLiqIVAItem)
            return round(dIVA10, 8)
        except:
            return 0

    def calculate_dLiqTotIVA5(self):
        try:
            item = self.items[0]
            if (item.dTasaIVA == 5 
                    and (self.iTImp == 1 
                        or self.iTImp == 5)):
                dLiqTotIVA5 = round(decimal_or_zero(self.dRedon) / 1.05, 8)
                return dLiqTotIVA5
                
        except:
            return 0

    def calculate_dLiqTotIVA10(self):
        try:
            item = self.items[0]
            if (item.dTasaIVA == 10
                    and (self.iTImp == 1 
                        or self.iTImp == 5)):
                dLiqTotIVA10 = round(decimal_or_zero(self.dRedon) / 11, 8)
                return dLiqTotIVA10
                
        except:
            return 0

    def calculate_dTotIVA(self):
            try:
                dTotIVA = (decimal_or_zero(self.dIVA5)
                               + decimal_or_zero(self.dIVA10) 
                               - decimal_or_zero(self.dLiqTotIVA5)
                               - decimal_or_zero(self.dLiqTotIVA10)
                               + decimal_or_zero(self.dIVAComi))
                return round(dTotIVA, 8)
            except:
                return 0

    def calculate_dBaseGrav5(self):
        try:
            dBaseGrav5 = 0
            for item in self.items:
                if item.dTasaIVA == 5 and self.iTImp in (1, 5):
                    dBaseGrav5 += decimal_or_zero(item.dBasGravIVA)
            return round(dBaseGrav5, 8)
        except:
            return 0

    def calculate_dBaseGrav10(self):
        try:
            dBaseGrav10 = 0
            for item in self.items:
                if item.dTasaIVA == 10 and self.iTImp in (1, 5):
                    dBaseGrav10 += decimal_or_zero(item.dBasGravIVA)
            return round(dBaseGrav10, 8)
        except:
            return 0

    def calculate_dTBasGraIVA(self):
            try:
                dTBasGraIVA = (decimal_or_zero(self.dBaseGrav5)
                               + decimal_or_zero(self.dBaseGrav10))
                return round(dTBasGraIVA, 8)
            except:
                return 0

    def calculate_dTotalGs(self):
            try:
                dTotalGs = (decimal_or_zero(self.dTotGralOpe)
                               * decimal_or_zero(self.dTiCam))
                return round(dTotalGs, 8)
            except:
                return 0

    """
    dSubExe
    dSub5
    dSub10
    dTotOpe
    dTotDesc
    dTotDescGIotem
    dTotAntItem
    dTotAnt
    dDescTotal
    dAnticipo
    dTotGralOpe
    dIVA5
    dIVA10
    dLiqTotIVA5
    dLiqTotIVA10
    dTotIVA
    dBaseGrav5
    dBaseGrav10
    dTBasGraIVA
    
    """

    def get_descripciones(self):
        self.get_dDesTImp()
        self.get_dDCondCred()
        self.getdDesTiDE()
        self.getdDesTipTra()
        self.getdDesTImp()
        self.get_dDesMoneOpe()
        self.get_dDesPaisRe()
        self.getdDTipIDRec()
        self.get_dDesMotEmi()
        self.get_dDCondCred()
        self.get_datos_geograficos()
        self.getdDesIndPres()
        self.getdDCondOpe()

        for item in self.items:
            item.get_dDesUniMed()
            item.getdDesAfecIVA()

        for medio_pago in self.medios_pago:
            medio_pago.get_dDesTiPag()
            medio_pago.get_dDMoneTiPag()

        for cuota in self.cuotas:
            cuota.get_dDMoneCuo(self)      

        for documento_asociado in self.documentos:
            documento_asociado.getdDesTipDocAso()       
            documento_asociado.getdDTipoDocAso()
            documento_asociado.get_dDesTipCons()
        
        if self.autofactura:
            self.autofactura.get_dDesNatVen()
            self.autofactura.get_dDTipIDVen()
            self.autofactura.get_datos_geograficos_autof()

        if self.nota_remision:
            self.nota_remision.get_dDesMotEmiNR()
            self.nota_remision.get_dDesRespEmiNR()

        if self.transporte_mercaderia:
            self.transporte_mercaderia.get_dDesTipTrans()
            self.transporte_mercaderia.get_dDesModTrans()

            if self.transporte_mercaderia.salida_mercaderias:
                self.transporte_mercaderia.salida_mercaderias.get_datos_geograficos_sm()

            for local in self.transporte_mercaderia.locales_entrega:
                local.get_datos_geograficos_em()

            if self.transporte_mercaderia.transportista:
                self.transporte_mercaderia.transportista.get_dDTipIDTrans()
                self.transporte_mercaderia.transportista.get_dDesNacTrans()


    def obtener_valores_calculados(self, session):
        # Revisar1: Obtenemos los valores de los metodos, asignamos a su propiedad correspondiente
        try:
            if self._Id:
                self.get_datos_cdc()
            else:
                self.getId(session)

        except Exception:
            self._Id = "0" * 44
            raise ValueError("Error al generar el cdc, verifique los datos enviados")
        self.dFecFirma = self.getdFecFirma()
        self.dNomRec = self.getdNomRec()
        if not self.dTotGralOpe:
            self.dTotGralOpe = str(self.getdTotGralOpe())
        # self.dDesTipDocAso = doc.getdDesTipDocAso() (este es un caso particular)
        self.dCarQR = self.getdCarQR()
        if self.dInfAdic and isinstance(self.dInfAdic, dict):
            self.dInfAdic = json.dumps(self.dInfAdic)


    def convertir_etiquetas_numericas(self):
        self.iCondOpe = try_int(self.iCondOpe)
        self.iTiDE = try_int(self.iTiDE)
        self.iTImp = try_int(self.iTImp)
        self.iTiDE = try_int(self.iTiDE)
        self.iTipTra = try_int(self.iTipTra)
        self.iNatRec = try_int(self.iNatRec)
        self.iTipIDRec = try_int(self.iTipIDRec)
        # Convierte a 0 y eso queda como vacio despues para un valor '000'. Comentado PV 07/05/2022
        #self.dNumIDRec = try_str(int_or_same(self.dNumIDRec)) 

        # Si solo contiene numeros, convertimos a numerico. Puede ser alfanumerico!
        self.dRucRec = try_str(self.dRucRec)
        
        self.dDVRec = try_int(self.dDVRec)
        self.iTiOpe = try_int(self.iTiOpe)
        self.iTiContRec = try_int(self.iTiContRec)
        self.iIndPres = try_int(self.iIndPres)
        self.iCondCred = try_int(self.iCondCred)
        self.dCuotas = try_int(self.dCuotas)

    def validar_reglas_negocio(self):
        # Si hay direccion, informar tambien la ciudad y departamento obligatoriamente
        mensaje_error = ""
        """
        if self.dDirRec:
            if not self.cCiuRec or not self.cDepRec:
                mensaje_error = f"ERROR: Cuando el valor de la direccion del receptor tiene un valor, " \
                                "se debe informar tambien la ciudad y el departamento del receptor"
                return False, mensaje_error
        """

        #Solo si se informa la direccion, se debe informar el nro. de casa (sino, no tiene sentido generar el tag
        self.dNumCasRec = self.dNumCasRec if self.dDirRec else ""

        # Check del Digito verificador del origen vs. el que corresponde al RUC segun el calculo del "modulo 11"
        if self.dRucRec:            
            # El calculo del digito verificador aplica solamente cuando el ruc es numerico (y puede no serlo!)
            if self.dRucRec.isnumeric():
                digito_verificador = get_digito_verificador(self.dRucRec)
                if str(digito_verificador) != str(self.dDVRec):
                    mensaje_error = f"ERROR: El dígito verificador del RUC del Receptor ({self.dRucRec}) " \
                                f"debería ser {digito_verificador} en lugar de '{try_str(self.dDVRec)}'"
                    return False, mensaje_error

        #Si es Autofactura, NC o ND, tiene que tener documentos asociados
        if (self.iTiDE == 4 or self.iTiDE == 5 or self.iTiDE == 6) and not self.documentos:
            mensaje_error = f"ERROR: Si es Autofactura, NC o ND debe tener documentos asociados"
            return False, mensaje_error

        return True, mensaje_error


    def get_geography(self, ciudad, barrio):
        ciudad = ciudad.upper()
        barrio = barrio.upper()
        if ciudad == "ASUNCION":
            valores = [val for key, val in self.dict_geography.items() if ciudad in key]
        else:
            valores = [val for key, val in self.dict_geography.items() if barrio in key]

            if not valores:
                valores = [val for key, val in self.dict_geography.items() if ciudad in key]

        return valores


    def generarXML(self):
        # Abrimos el archivo csv que contiene la matriz de la estructura del xml
        this_folder = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(this_folder, 'estructura_nodos_xml.csv')
        csvData = csv.reader(open(my_file, encoding='utf8'), delimiter=';')
        header = next(csvData)

        root = CrearNodoRaiz(self, True)
        atributos_de = vars(self)

        for row in csvData:
            #if row[0].strip() == "dMonTiPag":
            #if self.iTiDE == 7:
            #    print("Sigamosle!")
            #    pass

            if row[4].strip() == "1":
                continue

            if self.iTiDE != 1 and (row[0].strip() == "gCamFE" or row[1].strip() == "gCamFE"):
                continue

            if (self.iTiDE != 5 and self.iTiDE != 6) and (row[0].strip() == "gCamNCDE" or row[1].strip() == "gCamNCDE"):
                continue

            if (self.iTiDE != 1 and self.iTiDE != 4) and (row[0].strip() == "gCamCond" or row[1].strip() == "gCamCond"):
                continue

            if self.iCondOpe != 2 and (row[0].strip() == "gPagCred" or row[1].strip() == "gPagCred"):
                continue

            if (self.iTiDE != 1 and self.iTiDE != 4 and self.iTiDE != 5 and self.iTiDE != 6 and self.iTiDE != 7) \
            and (row[0].strip() == "gCamDEAsoc" or row[1].strip() == "gCamDEAsoc"):
                continue

            if (self.iTiDE != 1 and self.iTiDE != 4) and (row[0].strip() == "iTipTra"
                                                          or row[0].strip() == "dDesTipTra"):
                continue

            if self.iCondOpe != 1 and (row[0].strip() == "gPaConEIni"):
                continue
            
            #if self.iTiDE == 7 and row[0].strip() == "gTotSub":
            #    continue            
                        
            if self.iTiDE == 7 and (row[0].strip() == "gTotSub" or row[0].strip() == "gValorItem"):
                if row[0].strip() == "gValorItem" :
                    print("aca tuvo que entrar para no agrgar el grupo de taggggggsss!")
                continue
            
            if self.iTiDE == 4 and (row[0].strip() == "dSubExe" or row[0].strip() == "dSubExo"
                                    or row[0].strip() == "dSub5" or row[0].strip() == "dSub10"
                                    or row[0].strip() == "dIVA5" or row[0].strip() == "dIVA10"
                                    or row[0].strip() == "dTotIVA" or row[0].strip() == "dBaseGrav5"
                                    or row[0].strip() == "dBaseGrav10" or row[0].strip() == "dTBasGraIVA"
                                    or row[0].strip() == "dTotalGs" or row[0].strip() == "dComi"
                                    or row[0].strip() == "dIVAComi"):
                continue
            if (self.iTiDE == 4 or self.iTiDE == 7) and (row[0].strip() == "gCamIVA" or row[1].strip() == "gCamIVA"):
                #print("es autofactura! algo sigue andando mal aca..")
                continue

            if row[1].strip() == root.tag:
                child_node = etree.SubElement(root, row[0].strip())
                if row[0].strip() == "DE":
                    child_node.set("Id", self._Id)
                elif row[0].strip() == "gCamFuFD":
                    pass
                else:
                    child_node.text = str(atributos_de.get(row[0].strip()))
                root.append(child_node)
            else:
                nodo = root.find(f".//{row[1].strip()}")
                if nodo is not None:
                    if row[0].strip() != "Id":
                        if row[2].strip() == "0":
                            valor = atributos_de.get(row[0].strip())
                            excepciones = ("dDVId", "dNumCas","dTotOpe", "dTotDesc","dTotDescGlotem", "dTotAntItem",
                                           "dTotAnt", "dPorcDescTotal", "dDescTotal", "dAnticipo", "dRedon",
                                           "dTotGralOpe", "dPropIVA", "dLiqIVAItem", "dTasaIVA", "dBasGravIVA",
                                           "dDVEmi", "dDVRec", "dNumCasRec", "dTotIVA", "dPUniProSer",
                                           "dTotBruOpeItem", "dDescItem","dTotOpeItem","dSub10", "dIVA10", "dBaseGrav10",
                                           "dSalAnt", "dTBasGraIVA", "dSubExe", "dSub5", "dMonTiPag")
                            if valor or row[0].strip() in excepciones:
                                child_node = etree.SubElement(nodo, row[0].strip())
                                if valor or (try_int(valor) == 0):
                                    child_node.text = str(valor)
                                    nodo.append(child_node)
                        elif row[2].strip() == "1" and row[3].strip() == "1":
                            child_node = etree.SubElement(nodo, row[0].strip())
                            nodo.append(child_node)
                        elif row[3].strip() == "transporte_mercaderia":
                            objeto = atributos_de.get(row[3].strip())
                            if objeto:
                                atributos_objeto = vars(objeto)
                                padre_objeto = etree.SubElement(nodo, row[0].strip())
                                for key, value in atributos_objeto.items():
                                    if key == '_sa_instance_state' or key == 'de_id' or key == 'de' \
                                            or key == 'transporte_mercaderia':
                                        continue
                                    elif key == 'salida_mercaderias' or key == 'transportista':
                                        #Otro nivel de anidamiento
                                        #PV, para continuar: si es locales de entrega, recorrer (porque es una lista de elementos)
                                        #locales_entrega, elemento 0..1...etc.
                                        objeto_anidado = atributos_objeto.get(key)
                                        atributos_objeto_asociado = vars(objeto_anidado)

                                        nombre_mapeado = key
                                        if key == 'salida_mercaderias':
                                            nombre_mapeado = 'gCamSal'
                                        #elif key == 'locales_entrega':
                                        #    nombre_mapeado = 'gCamEnt'
                                        elif key == 'transportista':
                                            nombre_mapeado = 'gCamTrans'

                                        padre_objeto_asociado = etree.SubElement(padre_objeto, nombre_mapeado)
                                        for k, v in atributos_objeto_asociado.items():
                                            if k == '_sa_instance_state' or k == 'de_id' or k == 'de' \
                                                    or k == 'transporte_mercaderias':
                                                continue
                                            nodo_objeto_hijo_asociado = etree.SubElement(padre_objeto_asociado, k)
                                            if v or (try_int(v) == 0):
                                                nodo_objeto_hijo_asociado.text = str(v)
                                    elif key == 'locales_entrega':
                                        # Otro nivel de anidamiento
                                        objeto_anidado = atributos_objeto.get(key)
                                        if objeto_anidado:
                                            atributos_objeto_asociado = vars(objeto_anidado)
                                            nombre_mapeado = 'gCamEnt'
                                            padre_objeto_asociado = etree.SubElement(padre_objeto, nombre_mapeado)
                                            for vehi in objeto_anidado:
                                                atributos_vehiculo = vars(vehi)
                                                for k, v in atributos_vehiculo.items():
                                                    if k == '_sa_instance_state' or k == 'de_id' or k == 'de' \
                                                            or k == 'transporte_mercaderias':
                                                        continue
                                                    nodo_objeto_hijo_asociado = etree.SubElement(padre_objeto_asociado,k)
                                                    if v or (try_int(v) == 0):
                                                        nodo_objeto_hijo_asociado.text = str(v)
                                    elif key == 'vehiculos':
                                        # Este bloque completo habria que eliminar y llevar a Item, tengo miedo ._.
                                        objeto_anidado = atributos_objeto.get(key)
                                        if objeto_anidado:
                                            atributos_objeto_asociado = vars(objeto_anidado)
                                            nombre_mapeado = 'gVehTras'
                                            padre_objeto_asociado = etree.SubElement(padre_objeto, nombre_mapeado)
                                            for vehi in objeto_anidado:
                                                atributos_vehiculo = vars(vehi)
                                                for k, v in atributos_vehiculo.items():
                                                    if k == '_sa_instance_state' or k == 'de_id' or k == 'de' \
                                                            or k == 'transporte_mercaderias':
                                                        continue
                                                    nodo_objeto_hijo_asociado = etree.SubElement(padre_objeto_asociado,k)
                                                    if v:
                                                        nodo_objeto_hijo_asociado.text = str(v)
                                    else:
                                        nodo_objeto_hijo = etree.SubElement(padre_objeto, key)
                                        if value:
                                            nodo_objeto_hijo.text = str(value)
                                        padre_objeto.append(nodo_objeto_hijo)
                        elif row[3].strip() == "autofactura" or row[3].strip() == "nota_remision" \
                                or row[3].strip() == "compra_publica":
                            objeto = atributos_de.get(row[3].strip())
                            if objeto:
                                atributos_objeto = vars(objeto)
                                padre_objeto = etree.SubElement(nodo, row[0].strip())
                                for key,value in atributos_objeto.items():
                                    if key == '_sa_instance_state' or key == 'de_id' or key == 'de' \
                                            or key == 'transporte_mercaderias':
                                        continue
                                    nodo_objeto_hijo = etree.SubElement(padre_objeto, key)
                                    #if value:
                                    if value or (try_int(value) == 0):
                                        nodo_objeto_hijo.text = str(value)
                                    padre_objeto.append(nodo_objeto_hijo)
                        elif row[3].strip() == 'cuotas' or row[3].strip() == 'medios_pago':
                            tags_tarjeta = ["iDenTarj", "dDesDenTarj", "dRSProTar", "dRUCProTar", "dDVProTar", 
                                            "iForProPa", "dCodAuOpe", "dNomTit", "dNumTarj"]
                            tags_cheque = ["dNumCheq", "dBcoEmi"]
                            tag_tcd_cheque_creado = False
                            objeto = atributos_de.get(row[3].strip())
                            if objeto:
                                for cu in objeto:
                                    atributos_objeto = vars(cu)
                                    padre_objeto = etree.SubElement(nodo, row[0].strip())
                                    #Se rehizo y se probo con JSON, Excel y Archivos XML convertidos de TXT por Planet 19/11/2022                                    
                                    for key, value in atributos_objeto.items():
                                        if key == '_sa_instance_state' or key == 'de_id' or key == 'de':
                                            continue
                                        if key == 'pago_cheque':
                                            nodo_cheque = etree.SubElement(padre_objeto, 'gPagCheq')
                                            atributos_pago_cheque = vars(value)
                                            for k2, v2 in atributos_pago_cheque.items():
                                                if k2 == '_sa_instance_state' or k2 == 'de_id' or k2 == 'de' or k2 == 'medio_pago':
                                                    continue
                                                if v2 or (try_int(v2) == 0):
                                                    nodo_objeto_hijo = etree.SubElement(padre_objeto, k2)
                                                    nodo_objeto_hijo.text = str(v2)
                                                    nodo_cheque.append(nodo_objeto_hijo)
                                        elif key == 'pago_tarjeta_cd':
                                            nodo_tarjeta = etree.SubElement(padre_objeto, 'gPagTarCD')
                                            atributos_pago_tarjeta = vars(value)
                                            for k2, v2 in atributos_pago_tarjeta.items():
                                                if k2 == '_sa_instance_state' or k2 == 'de_id' or k2 == 'de' or k2 == 'medio_pago':
                                                    continue
                                                if v2 or (try_int(v2) == 0):
                                                    nodo_objeto_hijo = etree.SubElement(padre_objeto, k2)
                                                    nodo_objeto_hijo.text = str(v2)
                                                    nodo_tarjeta.append(nodo_objeto_hijo)
                                        elif value or (try_int(value) == 0):
                                            nodo_objeto_hijo = etree.SubElement(padre_objeto, key)
                                            nodo_objeto_hijo.text = str(value)
                                            padre_objeto.append(nodo_objeto_hijo)                                                                             
                        elif row[2].strip() == "1" and row[3].strip() != "1":
                            #son varios elementos. Los que tienen N, aun no creamos la coleccion, los demas ya tenemos
                            if row[3].strip() == "N":
                                continue
                            nombre_atributo = row[3].strip()
                            #if nombre_atributo == "items":
                            #    print("prestemos atencion aqui mijo")
                            atributo = atributos_de.get(nombre_atributo)
                            if atributo:
                                nodos_aux = []
                                for elemento in atributo:
                                    #creo el padre
                                    if isinstance(elemento,Item):
                                        elemento.getdDesAfecIVA()
                                        if not elemento.dPropIVA:
                                            elemento.dPropIVA = "0"
                                        if not elemento.dTasaIVA:
                                            elemento.dTasaIVA = "0"
                                        if not elemento.dBasGravIVA:
                                            elemento.dBasGravIVA = "0"
                                        if not elemento.dLiqIVAItem:
                                            elemento.dLiqIVAItem = "0"

                                    padre_muchos = etree.SubElement(nodo, row[0].strip())
                                    atributos_hijos = vars(elemento)
                                    for key, value in atributos_hijos.items():
                                        if key == '_sa_instance_state' or key == 'de_id' or key == 'pago_tarjeta_cd' or key == 'pago_cheque':
                                            #print("puaj")
                                            continue
                                        if self.es_caso_especial_no_agregar(key):
                                            continue
                                        # Revisar 3: En el caso de los items, hay un NIVEL 5 LPM, esto hay que revisar
                                        excepciones_nivel = {"dPUniProSer":"gValorItem",
                                                             "dTiCamIt":"gValorItem",
                                                             "dTotBruOpeItem":"gValorItem",
                                                             "dDescItem":"gValorRestaItem",
                                                             "dPorcDesIt":"gValorRestaItem",
                                                             "dDescGloItem":"gValorRestaItem",
                                                             "dAntPreUniIt":"gValorRestaItem",
                                                             "dAntGloPreUniIt":"gValorRestaItem",
                                                             "dTotOpeItem":"gValorRestaItem",
                                                             "dTotOpeGs":"gValorRestaItem",
                                                             "iAfecIVA": "gCamIVA",
                                                             "dDesAfecIVA": "gCamIVA",
                                                             "dPropIVA": "gCamIVA",
                                                             "dTasaIVA": "gCamIVA",
                                                             "dBasGravIVA": "gCamIVA",
                                                             "dLiqIVAItem": "gCamIVA"}
                                        if key in excepciones_nivel:
                                            #if key == "dPropIVA":
                                            #    print("Mirale un poco")
                                            valor_tag = atributos_hijos.get(key)
                                            if not valor_tag and key not in ("dPropIVA", "dTasaIVA", "dBasGravIVA",
                                                                             "dLiqIVAItem", "dPUniProSer",
                                                                             "dTotBruOpeItem", "dDescItem","dTotOpeItem"):
                                                continue
                                            padre = excepciones_nivel.get(key)
                                            if padre == "gCamIVA" and not self.generategCamIVA():
                                                continue
                                            #nodo_padre = root.find(f".//{padre}")
                                            nodo_padre = padre_muchos.find(f".//{padre}")
                                            #Si no encuentra el nodo padre, le creamos :S
                                            if nodo_padre is None:                                                
                                                papa_del_corazon = ""
                                                if padre == "gValorItem" or padre == "gCamIVA":
                                                    papa_del_corazon="gCamItem"
                                                elif padre == "gValorRestaItem":
                                                    papa_del_corazon = "gValorItem"

                                                if papa_del_corazon == "gCamItem":
                                                    nodo_padre_corazon = padre_muchos
                                                else:
                                                    nodo_padre_corazon = padre_muchos.find(f".//{papa_del_corazon}")
                                                padre_nivel = etree.SubElement(padre_muchos, padre)
                                                hijo_nivel = etree.SubElement(padre_nivel, key)
                                                
                                                if value or (try_int(value) == 0):
                                                    hijo_nivel.text = str(value) #dPuniProser
                                                padre_nivel.append(hijo_nivel)
                                                nodo_padre_corazon.append(padre_nivel)
                                            else:
                                                nodo_nivel = etree.SubElement(nodo_padre, key)
                                                if value or (try_int(value) == 0):
                                                    nodo_nivel.text = str(value) #dTotBruOpeItem
                                                nodo_padre.append(nodo_nivel)
                                        elif key == 'itemvehiculo':
                                            # Otro nivel de anidamiento
                                            objeto_anidado = atributos_hijos.get(key)
                                            if objeto_anidado:
                                                atributos_objeto_asociado = vars(objeto_anidado)
                                                nombre_mapeado = 'gVehNuevo'
                                                padre_objeto_asociado = etree.SubElement(padre_muchos, nombre_mapeado)                                                
                                                for k, v in atributos_objeto_asociado.items():
                                                    if k == '_sa_instance_state' or k == 'item_id' or k == 'item':
                                                        continue
                                                    nodo_objeto_hijo_asociado = etree.SubElement(padre_objeto_asociado,k)
                                                    if v:
                                                        nodo_objeto_hijo_asociado.text = str(v)
                                        elif key == 'itemrastreomercaderia':
                                            # Otro nivel de anidamiento
                                            objeto_anidado = atributos_hijos.get(key)
                                            if objeto_anidado:
                                                atributos_objeto_asociado = vars(objeto_anidado)
                                                nombre_mapeado = 'gRasMerc'
                                                padre_objeto_asociado = etree.SubElement(padre_muchos, nombre_mapeado)                                                
                                                for k, v in atributos_objeto_asociado.items():
                                                    if k == '_sa_instance_state' or k == 'item_id' or k == 'item':
                                                        continue
                                                    nodo_objeto_hijo_asociado = etree.SubElement(padre_objeto_asociado,k)
                                                    if v:
                                                        nodo_objeto_hijo_asociado.text = str(v)
                                        else:
                                            nodo_hijos = etree.SubElement(padre_muchos, key)
                                            if value or (try_int(value) == 0):
                                                nodo_hijos.text = str(value) 
                                            padre_muchos.append(nodo_hijos)
                                    nodos_aux.append(padre_muchos)
                                if nodos_aux:
                                    for nx in nodos_aux:
                                        nodo.append(nx)

        # Removemos los tags vacios!
        context = etree.iterwalk(root)
        for action, elem in context:
            #if elem.tag == "dDVRec":
            #       print("seguirle paso a paso desde aca")
            parent = elem.getparent()
            #estaba en las excepciones dNumCasRec
            if self.recursively_empty(elem):
                if elem.tag not in ("dDVId", "dNumCas","dTotOpe", "dTotDesc","dTotDescGlotem", "dTotAntItem", "dTotAnt",
                                    "dPorcDescTotal", "dDescTotal", "dAnticipo", "dRedon", "dTotGralOpe", "dPropIVA",
                                    "dLiqIVAItem", "dTasaIVA", "dBasGravIVA", "dDVEmi", "dNumCasSal",
                                    "dNumCasEnt, dTotIVA", "dPUniProSer", "dTotBruOpeItem", "dDescItem","dTotOpeItem", 
                                    "dSub10", "dIVA10", "dBaseGrav10", "dSalAnt", "dTBasGraIVA", "dSubExe", "dSub5",
                                    "dMonTiPag"):
                    parent.remove(elem)
        tree = etree.ElementTree(root)
        xmlstr = etree.tostring(root).decode('utf-8')
        #tree.write("debuging.xml", pretty_print=True, encoding="utf-8")
        return self, xmlstr, tree

    def validar_xml_xsd(self, xmlstr):
        file_name = f'{self._Id}.xml'
        isvalid, err_msj = isXmlValid(self, xmlstr, file_name)
        if isvalid and not self.x_estado == self.ERROR_PREVALIDACION_INTERNA:
            self.x_estado = self.GENERADO
        else:
            self.x_estado = self.ERROR_PREVALIDACION_INTERNA
            self.x_error += err_msj

    def get_xml_file_name(self, OUTPUT_PATH):
        #os.makedirs(f"{OUTPUT_PATH}/{id_proceso}/error", exist_ok=True)
        path_error = os.path.join(OUTPUT_PATH, 'error')
        os.makedirs(path_error, exist_ok=True)
        if self.x_estado == self.GENERADO:
            path = f"{OUTPUT_PATH}"
        elif self.x_estado == self.ERROR_PREVALIDACION_INTERNA:
            path = path_error
        else:
            print("Error fatal. Estado de Documento Electrónico no reconocido")

        #if TESTING:
        #v_rand = random.randrange(10000, 99999999999)
        #self.xml_file_name = f"{path}/{self.nro_cuenta}_{self.fecha_corte}_{v_rand}.xml"
        #self.xml_file_name = f"{path}/{self._Id}.xml"
        self.xml_file_name = os.path.join(path, f'{self._Id}.xml')
        return self.xml_file_name

    def generar_archivo_xml(self, tree, proceso, OUTPUT_PATH, tipo_servicio='A'):
        # Generamos el archivo xml
        if tipo_servicio == 'A':
            #tree.write(self.get_xml_file_name(proceso.id, OUTPUT_PATH), pretty_print=True, encoding="utf-8")
            tree.write(self.get_xml_file_name(OUTPUT_PATH), pretty_print=True, encoding="utf-8")
        elif tipo_servicio == 'S':
            #self.xml_file_name = f"{OUTPUT_PATH}/{self._Id}.xml"
            #self.xml_file_name = f"{OUTPUT_PATH}/{self._Id}.xml"
            self.xml_file_name = os.path.join(OUTPUT_PATH, f'{self._Id}.xml')
            tree.write(self.xml_file_name, pretty_print=True, encoding="utf-8")

    def insertar_mysql(self, objeto_de, session, proceso):
        insert_mysql_db(objeto_de, session, proceso)

    def reemplazar_header_xml(self, tree):
        tree = ReemplazarNodoRaiz(self, tree)
        return tree

    def ejecutar_proceso_completo(self, session, proceso, OUTPUT_PATH, tipo_servicio='A'):
        try:
            # Formatear algunos campos
            self.dFeEmiDE = self.get_isoformat(self.dFeEmiDE)
            self.dEst = try_str(self.dEst).zfill(3)
            self.dPunExp = try_str(self.dPunExp).zfill(3)
            self.dNumDoc = try_str(self.dNumDoc).zfill(7)
            self.dFeIniT = self.get_short_iso_format(self.dFeIniT)
            self.dFecIniC = self.get_short_iso_format(self.dFecIniC)
            self.dFecFinC = self.get_short_iso_format(self.dFecFinC)
            self.dVencPag = self.get_short_iso_format(self.dVencPag)
            self.format_dNumDocAso()
            self.format_fechas_remision()
            self.get_descripciones()
            self.convertir_etiquetas_numericas()
            
            try:
                self.obtener_valores_calculados(session)
            except Exception as error:
                self.x_estado = self.ERROR_PREVALIDACION_INTERNA
                self.x_error += str(error)

            reglas_ok, msg = self.validar_reglas_negocio()

            if not reglas_ok:
                self.x_estado = self.ERROR_PREVALIDACION_INTERNA
                self.x_error += msg

            self.set_constantes()
            de, xml_string, tree = self.generarXML()
            self.validar_xml_xsd(xml_string)
            # luego de validar con los xsd locales, reemplazamos la cabecera 
            # para que apunte a la URL de la SIFEN
            tree = self.reemplazar_header_xml(xml_string)
            self.generar_archivo_xml(tree, proceso, OUTPUT_PATH, tipo_servicio)
            self.insertar_mysql(de, session, proceso)
            return de
        except Exception as ex:
            print(f"Error al generarXML: {ex}")
            self.x_estado = De.ERROR_PREVALIDACION_INTERNA
            self.x_error += f" Error no controlado: {ex}"
            log = Log(proceso_id=proceso.id, 
                      eventos=f"Error en metodo ejecutar_proceso_completo: {ex} dNumDoc:{self.dNumDoc}",
                      categoria=Log.ERROR, 
                      fecha_hora=datetime.now())
            session.add(log)
            session.commit()
            return self

    def recursively_empty(self, e):
        if e.text:
            return False
        return all((self.recursively_empty(c) for c in e.iterchildren()))

    def getdDesTImp(self):
        dic_des_tip_impuesto = {1: "IVA",
                                2: "ISC",
                                3: "Renta",
                                4: "Ninguno",
                                5: "IVA – Renta"}
        if self.iTImp:
            # Obtenemos solo si está vacío el campo descripción, 
            # sino dejamos el que vino de la fuente
            if not self.dDesTImp:
                self.dDesTImp = dic_des_tip_impuesto.get(try_int(self.iTImp))
            return self.dDesTImp
        # Puede que no se tenga que informar el tipo de impuesto (Si es nota de remision)
        #else:
        #    err_msg = "ERROR en getdDesTImp(): Se requiere el valor de iTImp para obtener la descripción asociada"
        #    print(err_msg)
        #    self.x_estado = De.ERROR_PREVALIDACION_INTERNA
        #    self.x_error += err_msg

    def get_geography(self, ciudad, barrio):
        if ciudad == "ASUNCION":
            valores = [val for key, val in self.dict_geography.items() if ciudad in key]
        else:
            valores = [val for key, val in self.dict_geography.items() if barrio in key]

            if not valores:
                valores = [val for key, val in self.dict_geography.items() if ciudad in key]

        return valores

    def get_dDesMoneOpe(self):
        if self.cMoneOpe:
            valores = [val for key, val in self.dict_currency.items() if self.cMoneOpe in key]
            if not self.dDesMoneOpe:
                # Obtenemos solo si está vacío el campo descripción, 
                # sino dejamos el que vino de la fuente
                self.dDesMoneOpe = valores[0][1]
            return self.dDesMoneOpe
        # Puede que sea una nota de remision, entonces no se informa la moneda, por consecuencia su descripcion
        #else:
        #    err_msg = "ERROR en get_currency(): Se requiere el valor de cMoneOpe para obtener dDesMoneOpe"
        #    print(err_msg)
        #    self.x_estado = De.ERROR_PREVALIDACION_INTERNA
        #    self.x_error += err_msg
        #    return ""

    def get_dDesPaisRe(self):
        return self.get_country()

    def get_country(self):
        if self.cPaisRec:
            # Obtenemos solo si está vacío el campo descripción, 
            # sino dejamos el que vino de la fuente
            if not self.dDesPaisRe:
                try:
                    valores = [val for key, val in self.dict_countries.items() if self.cPaisRec in key]
                    self.dDesPaisRe = valores[0][0]
                except Exception:
                    self.dDesPaisRe = ''
            return self.dDesPaisRe
        else:
            err_msg = "ERROR en get_country(): Se requiere el valor de cPaisRec para obtener dDesPaisRe"
            print(err_msg)
            self.x_estado = De.ERROR_PREVALIDACION_INTERNA
            self.x_error += err_msg
            return ""

    def format_dNumDocAso(self):
        for documento in self.documentos:
            #Agregado, porque si el documento asociado es 1(Electrónico) o 3(Constancia Electrónica)
            if documento.dNumDocAso:
                documento.dNumDocAso = str(documento.dNumDocAso).zfill(7)
            if documento.dEstDocAso:
                documento.dEstDocAso = str(documento.dEstDocAso).zfill(3)
            if documento.dPExpDocAso:
                documento.dPExpDocAso = str(documento.dPExpDocAso).zfill(3)

    def format_fechas_remision(self):
        """
        Formateamos fechas que corresponden a la Nota de Remisión 
        según el manual si es que posee algún valor
        """
        if self.nota_remision:
            if self.nota_remision.dFecEm:
                self.nota_remision.dFecEm = self.get_short_iso_format(self.nota_remision.dFecEm)

        if self.transporte_mercaderia:
            if self.transporte_mercaderia.dIniTras:
                self.transporte_mercaderia.dIniTras = self.get_short_iso_format(
                                                            self.transporte_mercaderia.dIniTras
                                                      )

        if self.transporte_mercaderia:
            if self.transporte_mercaderia.dFinTras:
                self.transporte_mercaderia.dFinTras = self.get_short_iso_format(
                                                        self.transporte_mercaderia.dFinTras
                                                      )

    def es_caso_especial_no_agregar(self, key):        
        """
            Si es nota remision, no generar tags que pueden estar incluso en las excepciones 
            de generar aunque tengan 0
            Todos los tags del grupo de gValorItem y por ende su hijo gValorRestaItem
        """        
        if self.iTiDE == 7 and (key == "dPUniProSer" or key == "dTiCamIt" 
                                or key == "dTotBruOpeItem" or key == "dDescItem" 
                                or key == "dPorcDesIt" or key == "dDescGloItem"
                                or key == "dAntPreUniIt" or key == "dAntGloPreUniIt"
                                or key == "dTotOpeItem" or key == "dTotOpeGs"):
            return True        
        else:
            return False



class Item(MysqlConnection.Base):
    __tablename__ = 'de_item'

    def __init__(self):
        self.dCodInt = ''
        self.dParAranc = ''
        self.dNCM = ''
        self.dDncpG = ''
        self.dDncpE = ''
        self.dGtin = ''
        self.dGtinPq = ''
        self.dDesProSer = ''
        self.cUniMed = ''
        self.dDesUniMed = ''
        self.dCantProSer = 0
        self.cPaisOrig = ''
        self.dDesPaisOrig = ''
        self.dInfItem = ''
        self.cRelMerc = ''
        self.dDesRelMerc = ''
        self.dCanQuiMer = ''
        self.dPorQuiMer = ''
        self.dCDCAnticipo = ''
        self.dPUniProSer = 0
        self.dTiCamIt = ''
        self.dTotBruOpeItem = 0
        self.dDescItem = 0
        self.dPorcDesIt = ''
        self.dDescGloItem = 0
        self.dAntPreUniIt = 0
        self.dAntGloPreUniIt = 0
        self.dTotOpeItem = 0
        self.dTotOpeGs = 0
        self.iAfecIVA = ''
        self.dDesAfecIVA = ''
        self.dPropIVA = ''
        self.dTasaIVA = ''
        self.dBasGravIVA = ''
        self.dLiqIVAItem = ''

    id = Column(Integer, primary_key=True)
    dCodInt = Column(String(50), nullable=True)
    dDesProSer = Column(String(2000), nullable=True)
    cUniMed = Column(Integer, nullable=True)
    dDesUniMed = Column(String(10), nullable=True)
    dCantProSer = Column(Integer, nullable=True)
    cPaisOrig = Column(String(3), nullable=True)
    dDesPaisOrig = Column(String(30), nullable=True)
    dInfItem = Column(String(500), nullable=True)
    cRelMerc = Column(Integer, nullable=True)
    dDesRelMerc = Column(String(21), nullable=True)
    dCanQuiMer = Column(Numeric(14, 4), nullable=True)
    dPorQuiMer = Column(Numeric(11, 8), nullable=True)
    dCDCAnticipo = Column(String(44), nullable=True)
    dParAranc = Column(Numeric(4), nullable=True)
    dNCM = Column(Numeric(8), nullable=True)
    dDncpG = Column(String(8), nullable=True)
    dDncpE = Column(String(4), nullable=True)
    dGtin = Column(Numeric(14), nullable=True)
    dGtinPq = Column(Numeric(14), nullable=True)
    dPUniProSer = Column(Numeric(23, 8), nullable=True)
    dTiCamIt = Column(Numeric(9, 4), nullable=True)
    dTotBruOpeItem = Column(Numeric(23, 8), nullable=True)
    dDescItem = Column(Numeric(23, 8), nullable=True)
    dPorcDesIt = Column(Numeric(11, 8), nullable=True)
    dDescGloItem = Column(Numeric(23, 8), nullable=True)
    dAntPreUniIt = Column(Numeric(23, 8), nullable=True)
    dAntGloPreUniIt = Column(Numeric(23, 8), nullable=True)
    dTotOpeItem = Column(Numeric(23, 8), nullable=True)
    dTotOpeGs = Column(Numeric(23, 8), nullable=True)
    iAfecIVA = Column(Integer, nullable=True)
    dDesAfecIVA = Column(String(23), nullable=True)
    dPropIVA = Column(Integer, nullable=True)
    dTasaIVA = Column(Integer, nullable=True)
    dBasGravIVA = Column(Numeric(23, 8), nullable=True)
    dLiqIVAItem = Column(Numeric(23, 8), nullable=True)
    de_id = Column(Integer, ForeignKey('de_documento_electronico.id'))
    itemvehiculo = relationship("ItemVehiculo", uselist=False, back_populates="item")
    itemrastreomercaderia = relationship("ItemRastreoMercaderia", uselist=False, back_populates="item")

    def getdTotBruOpeItem(self):
        """
        -Total bruto de la operación por ítem
        -Corresponde a la multiplicación del precio por ítem (E721) y la cantidad por ítem (E711)
        -Consulta realizada a la SET sobre descripción de concepto genérico (detallado en anexo)
        """
        self.dTotBruOpeItem = round(self.dPUniProSer * self.dCantProSer, 8)
        return self.dTotBruOpeItem

    def getdDescItem(self):
        """
        -Descuento particular sobre el precio unitario por ítem (incluidos impuestos)
        -Si no hay descuento por ítem completar con 0 (cero)
        -Consulta realizada a la SET sobre descripción de concepto genérico (detallado en anexo)
        """
        #Revisar, el campo que tiene el descuento es EA002 (dDescItem)?
        self.dDescItem = 0
        return self.dDescItem

    def getdPorcDesIt(self):
        """
        -Porcentaje de descuento particular por ítem
        -Debe existir si EA002 es mayor a 0 (cero) [EA002 * 100 / E721]
        -Consulta realizada a la SET sobre descripción de concepto genérico (detallado en anexo)
        """

        result = 0
        if self.dDescItem > 0:
            result = (self.dDescItem * 100) / self.dPUniProSer 	

        self.dPorcDesIt = round(result, 8)

        return self.dPorcDesIt

    def get_dTotOpeItem(self):
        """
        -Valor total de la operación por ítem
        -Cálculo para IVA, Renta, ninguno, IVA - Renta
        -Si D013 = 1, 3, 4 o 5 (afectado al IVA, Renta, ninguno, IVA - Renta), 
        entonces dTotOpeItem corresponde al cálculo aritmético: 
        (dPUniProSer (Precio unitario) 
            - dDescItem (Descuento particular) - dDescGloItem (Descuento global) 
            - dAntPreUniIt (Anticipo particular) - dAntGloPreUniIt (Anticipo global)
        ) * dCantProSer (cantidad)
        -Cálculo para Autofactura (iTiDE=4):
        -dPUniProSer * dCantProSer
        """
        try:
            self.dTotOpeItem = (self.dPUniProSer 
                - self.dDescItem  - self.dDescGloItem 
                - self.dAntPreUniIt - self.dAntGloPreUniIt 
                ) * self.dCantProSer
            return self.dTotOpeItem
        except Exception:
            self.dTotOpeItem = 0
        
        return self.dTotOpeItem

    def getdDesAfecIVA(self):		
        """
        -Descripción de la forma de afectación tributaria del IVA
        -Referente al campo E731 1= “Gravado IVA” 2= “Exonerado” (Art. 83- Ley 125/91) 3= “Exento” 4= “Gravado parcial” (Grav- Exento)
        -IDL, Variable
        -Relacionado al item anterior	
        -Segun respuesta, estos campos se obtienen del .dat 	
        """
        dic_des_afec_iva = {"1" : "Gravado IVA",
                            "2" : "Exonerado (Art. 83- Ley 125/91)",
                            "3" : "Exento",
                            "4" : "Gravado parcial (Grav- Exento)"}

        # Obligatorio si iTImp=1, 3, 4 o 5 y iTiDE ≠ 4 o 7
        # No informar si iTImp=2 y iTiDE= 4 o 7

        if self.iAfecIVA:
            # Obtenemos solo si está vacío el campo descripción, 
            # sino dejamos el que vino de la fuente
            if not self.dDesAfecIVA:
                self.dDesAfecIVA = dic_des_afec_iva.get(str(self.iAfecIVA)) 
            return self.dDesAfecIVA
        return ''


    def get_dBasGravIVA(self):
        """
        Si iAfecIVA = 1 o 4 este campo es igual al resultado del cálculo
        [dTotOpeItem* (dPropIVA/100)] / 1,1 si la tasa es del 10%
        [dTotOpeItem* (dPropIVA/100)] / 1,05 si la tasa es del 5%
        Si iAfecIVA = 2 o 3 este campo es igual 0
        """
        if self.iAfecIVA == 1 or self.iAfecIVA == 4:
            if self.dTasaIVA == 10:
                self.dBasGravIVA = round((self.dTotOpeItem * (self.dPropIVA / 100)) / 1.1, 8)
            elif self.dTasaIVA == 5:
                self.dBasGravIVA = round((self.dTotOpeItem * (self.dPropIVA / 100)) / 1.05, 8)
            else:
                print("Valor tasa de iva no reconocido para calcular dBasGravIVA")
        elif self.iAfecIVA == 2 or self.iAfecIVA == 3:
            self.dBasGravIVA = 0
        else:
            print("Valor iAfecIVA no reconocido para calcular dBasGravIVA")

    def get_dLiqIVAItem(self):
        """
        Corresponde al cálculo aritmético:
        dBasGravIVA * (dTasaIVA/100)
        Si iAfecIVA = 2 o 3 este campo es igual 0
        """
        if self.iAfecIVA == 1 or self.iAfecIVA == 4:
            self.dLiqIVAItem = round(self.dBasGravIVA * (self.dTasaIVA / 100), 8)
        elif self.iAfecIVA == 2 or self.iAfecIVA == 3:
            self.dLiqIVAItem = 0
        else:
            print("Valor iAfecIVA no reconocido para calcular dBasGravIVA")

    def get_dDesUniMed(self):
        dict_unidades_medidas = {87:'m',2366:'CPM',2329:'UI',110:'M3',77:'UNI',
            86:'g',89:'LT',90:'MG',91:'CM',92:'CM2',93:'CM3',94:'PUL',96:'MM2',
            79:'kg/m²',97:'AA',98:'ME',99:'TN',100:'Hs',101:'Mi',104:'DET',
            103:'Ya',108:'MT',109:'M2',95:'MM',666:'Se',102:'Di',83:'kg',
            88:'ML',625:'Km',660:'ml',885:'GL',891:'pm',869:'ha',569:'ración',}

        if self.cUniMed:
            # Obtenemos solo si está vacío el campo descripción, 
            # sino dejamos el que vino de la fuente
            if not self.dDesUniMed:
                self.dDesUniMed = dict_unidades_medidas.get(try_int(self.cUniMed)) 
            return self.dDesUniMed


class Actividad(MysqlConnection.Base):
    __tablename__ = 'de_actividad_economica'

    id = Column(Integer, primary_key=True)
    cActEco = Column(String(8), nullable=True)
    dDesActEco = Column(String(300), nullable=True)
    de_id = Column(Integer, ForeignKey('de_documento_electronico.id'))


class Log(MysqlConnection.Base):
    __tablename__ = 'proc_log_proceso'

    id = Column(Integer, primary_key=True)
    proceso_id = Column(Integer, ForeignKey('proc_proceso.id'))
    eventos = Column(String(1000), nullable=True)
    categoria = Column(String(15), nullable=True)
    fecha_hora = Column(DateTime, nullable=True)


    INFO = 'INFO'
    WARNING = 'WARNING'
    ERROR = 'ERROR'


class Archivo(MysqlConnection.Base):
    __tablename__ = 'proc_archivo'

    id = Column(Integer, primary_key=True)
    proceso_id = Column(Integer, ForeignKey('proc_proceso.id'))
    attached_file = Column(String(100), nullable=True)
    origin_file_name = Column(String(200), nullable=True)
    type = Column(Integer, nullable=True)
    date_time_received = Column(DateTime, nullable=True)
    state = Column(String(3), nullable=True)


class DocumentoAsociado(MysqlConnection.Base):
    __tablename__ = 'de_documento_asociado'

    def __init__(self):
        self.iTipDocAso = ''
        self.dDesTipDocAso = ''
        self.dCdCDERef = ''
        self.dNTimDI = ''
        self.dEstDocAso = ''
        self.dPExpDocAso = ''
        self.dNumDocAso = ''
        self.iTipoDocAso = ''
        self.dDTipoDocAso = ''
        self.dFecEmiDI = ''
        self.dNumComRet = ''
        self.dNumResCF = ''
        self.iTipCons = ''
        self.dDesTipCons = ''
        self.dNumCons = ''
        self.dNumControl = ''

    id = Column(Integer, primary_key=True)
    iTipDocAso = Column(Numeric(1), nullable=True)
    dDesTipDocAso = Column(String(25), nullable=True)
    dCdCDERef = Column(String(44), nullable=True)
    dNTimDI = Column(Numeric(8), nullable=True)
    dEstDocAso = Column(String(3), nullable=True)
    dPExpDocAso = Column(String(3), nullable=True)
    dNumDocAso = Column(String(7), nullable=True)
    iTipoDocAso = Column(Numeric(1), nullable=True)
    dDTipoDocAso = Column(String(16), nullable=True)
    dFecEmiDI = Column(Date, nullable=True)
    dNumComRet = Column(String(15), nullable=True)
    dNumResCF = Column(String(15), nullable=True)
    iTipCons = Column(Integer, nullable=True)
    dDesTipCons = Column(String(34), nullable=True)
    dNumCons = Column(BigInteger, nullable=True)
    dNumControl = Column(String(8), nullable=True)
    de_id = Column(Integer, ForeignKey('de_documento_electronico.id'))

    def getdDesTipDocAso(self):
        # Descripción del tipo de documento asociado
        # Referente al campo H002. Relacionado al item anterior
        dic_dDesTipDocAso = {"1": "Electrónico",
                             "2": "Impreso",
                             "3": "Constancia Electrónica"}

        if self.iTipDocAso:
            self.dDesTipDocAso = dic_dDesTipDocAso.get(str(self.iTipDocAso))
            return self.dDesTipDocAso
        else:
            return ''

    def getdDTipoDocAso(self):
        """
        Descripción del tipo de documento impreso
        """

        dic_descripciones = {
            "1": "Factura",
            "2": "Nota de crédito",
            "3": "Nota de débito",
            "4": "Nota de remisión"            
        }

        if self.iTipoDocAso and not self.dDTipoDocAso:
            self.dDTipoDocAso = dic_descripciones.get(str(self.iTipoDocAso), '')
            return self.dDTipoDocAso
        return self.dDTipoDocAso

    def get_dDesTipCons(self):
        """
        Descripción del tipo de constancia
        """
        
        dic_descripciones = {
            "1" : "Constancia de no ser contribuyente",
            "2" : "Constancia de microproductores"
        }

        if self.iTipCons and not self.dDesTipCons:
            self.dDesTipCons = dic_descripciones.get(str(self.iTipCons), '')
        return self.dDesTipCons


class MedioPago(MysqlConnection.Base):
    __tablename__ = 'de_medio_pago'

    def __init__(self):
        self.iTiPago = ''
        self.dDesTiPag = ''
        self.dMonTiPag = ''
        self.cMoneTiPag = ''
        self.dDMoneTiPag = ''
        self.dTiCamTiPag = ''

    id = Column(Integer, primary_key=True)
    iTiPago = Column(Numeric(2), nullable=True)
    dDesTiPag = Column(String(30), nullable=True)
    dMonTiPag = Column(Numeric(23, 8), nullable=True)
    cMoneTiPag = Column(String(3), nullable=True)
    dDMoneTiPag = Column(String(20), nullable=True)
    dTiCamTiPag = Column(Numeric(23, 8), nullable=True)
    de_id = Column(Integer, ForeignKey('de_documento_electronico.id'))
    pago_tarjeta_cd = relationship("PagoTarjetaCD", uselist=False, back_populates="medio_pago")
    pago_cheque = relationship("PagoCheque", uselist=False, back_populates="medio_pago")

    def get_dDesTiPag(self):
        """
        Descripción del tipo de pago
        """
        
        dic_descripciones = {
            "1" : "Efectivo",
            "2" : "Cheque",
            "3" : "Tarjeta de crédito",
            "4" : "Tarjeta de débito",
            "5" : "Transferencia",
            "6" : "Giro",
            "7" : "Billetera electrónica",
            "8" : "Tarjeta empresarial",
            "9" : "Vale",
            "10" : "Retención",
            "11" : "Pago por anticipo",
            "12" : "Valor fiscal",
            "13" : "Valor comercial",
            "14" : "Compensación",
            "15" : "Permuta”",
            "16" : "Pago bancario”",
            "17" : "Pago Móvil",
            "18" : "Donación",
            "19" : "Promoción",
            "20" : "Consumo Interno",
        }

        if self.iTiPago and not self.dDesTiPag:
            self.dDesTiPag = dic_descripciones.get(str(self.iTiPago), '')
            return self.dDesTiPag
        return self.dDesTiPag

    def get_dDMoneTiPag(self):
        """
        Descripción de la moneda por tipo de pago
        """

        if self.cMoneTiPag and not self.dDMoneTiPag:
            dict_currency = get_dict_currency()
            valores = [val for key, val in dict_currency.items() if self.cMoneTiPag in key]
            self.dDMoneTiPag = valores[0][1]
            return self.dDMoneTiPag
        return self.dDMoneTiPag


class ComprasPublicas(MysqlConnection.Base):
    __tablename__ = 'de_compras_publicas'

    def __init__(self):
        self.dModCont = ''
        self.dEntCont = ''
        self.dAnoCont = ''
        self.dSecCont = ''
        self.dFeCodCont = ''

    id = Column(Integer, primary_key=True)
    dModCont = Column(String(2), nullable=True)
    dEntCont = Column(Integer, nullable=True)
    dAnoCont = Column(Integer, nullable=True)
    dSecCont = Column(Integer, nullable=True)
    dFeCodCont = Column(Date, nullable=True)
    de_id = Column(Integer, ForeignKey('de_documento_electronico.id'))
    de = relationship("De", back_populates="compra_publica")


class Autofactura(MysqlConnection.Base):
    __tablename__ = 'de_autofactura'

    def __init__(self):
        self.iNatVen = ''
        self.dDesNatVen = ''
        self.iTipIDVen = ''
        self.dDTipIDVen = ''
        self.dNumIDVen = ''
        self.dNomVen = ''
        self.dDirVen = ''
        self.dNumCasVen = ''
        self.cDepVen = ''
        self.dDesDepVen = ''
        self.cDisVen = ''
        self.dDesDisVen = ''
        self.cCiuVen = ''
        self.dDesCiuVen = ''
        self.dDirProv = ''
        self.cDepProv = ''
        self.dDesDepProv = ''
        self.cDisProv = ''
        self.dDesDisProv = ''
        self.cCiuProv = ''
        self.dDesCiuProv = ''

    id = Column(Integer, primary_key=True)
    iNatVen = Column(Integer, nullable=True)
    dDesNatVen = Column(String(16), nullable=True)
    iTipIDVen = Column(Integer, nullable=True)
    dDTipIDVen = Column(String(20), nullable=True)
    dNumIDVen = Column(String(20), nullable=True)
    dNomVen = Column(String(60), nullable=True)
    dDirVen = Column(String(255), nullable=True)
    dNumCasVen = Column(Integer, nullable=True)
    cDepVen = Column(Integer, nullable=True)
    dDesDepVen = Column(String(16), nullable=True)
    cDisVen = Column(Integer, nullable=True)
    dDesDisVen = Column(String(30), nullable=True)
    cCiuVen = Column(Integer, nullable=True)
    dDesCiuVen = Column(String(30), nullable=True)
    dDirProv = Column(String(255), nullable=True)
    cDepProv = Column(Integer, nullable=True)
    dDesDepProv = Column(String(16), nullable=True)
    cDisProv = Column(Integer, nullable=True)
    dDesDisProv = Column(String(30), nullable=True)
    cCiuProv = Column(Integer, nullable=True)
    dDesCiuProv = Column(String(30), nullable=True)
    de_id = Column(Integer, ForeignKey('de_documento_electronico.id'))
    de = relationship("De", back_populates="autofactura")

    def get_dDesNatVen(self):
        """
        Descripción de la naturaleza del vendedor
        """
        
        dic_descripciones = {
            "1" : "No contribuyente",
            "2" : "Extranjero"
        }

        if self.iNatVen and not self.dDesNatVen:
            self.dDesNatVen = dic_descripciones.get(str(self.iNatVen), '')
            return self.dDesNatVen
        return self.dDesNatVen

    def get_dDTipIDVen(self):
        """
        Descripción del tipo de documento de identidad del vendedor
        """
        
        dic_descripciones = {
            "1" : "Cédula paraguaya",
            "2" : "Pasaporte",
            "3" : "Cédula extranjera",
            "4" : "Carnet de residencia"
        }

        if self.iTipIDVen and not self.dDTipIDVen:
            self.dDTipIDVen = dic_descripciones.get(str(self.iTipIDVen), '')
            return self.dDTipIDVen
        return self.dDTipIDVen

    def get_datos_geograficos_autof(self):

        if self.cDepVen and not self.dDesDepVen:
            linea = filter_referencia_geografica('COD_DEPARTAMENTO', self.cDepVen)
            self.dDesDepVen = linea.get('DEPARTAMENTO', '')
        
        if self.cDisVen and not self.dDesDisVen:
            linea = filter_referencia_geografica('COD_DISTRITO', self.cDisVen)
            self.dDesDisVen = linea.get('DISTRITO', '')

        if self.cCiuVen and not self.dDesCiuVen:
            linea = filter_referencia_geografica('COD_CIUDAD', self.cCiuVen)
            self.dDesCiuVen = linea.get('CIUDAD', '')

        if self.cDepProv and not self.dDesDepProv:
            linea = filter_referencia_geografica('COD_DEPARTAMENTO', self.cDepProv)
            self.dDesDepProv = linea.get('DEPARTAMENTO', '')
        
        if self.cDisProv and not self.dDesDisProv:
            linea = filter_referencia_geografica('COD_DISTRITO', self.cDisProv)
            self.dDesDisProv = linea.get('DISTRITO', '')

        if self.cCiuProv and not self.dDesCiuProv:
            linea = filter_referencia_geografica('COD_CIUDAD', self.cCiuProv)
            self.dDesCiuProv = linea.get('CIUDAD', '')


class NotaRemision(MysqlConnection.Base):
    __tablename__ = 'de_nota_remision'

    def __init__(self):
        self.iMotEmiNR = ''
        self.dDesMotEmiNR = ''
        self.iRespEmiNR = ''
        self.dDesRespEmiNR = ''
        self.dKmR = ''
        self.dFecEm = ''

    id = Column(Integer, primary_key=True)
    iMotEmiNR = Column(Integer, nullable=True)
    dDesMotEmiNR = Column(String(60), nullable=True)
    iRespEmiNR = Column(Integer, nullable=True)
    dDesRespEmiNR = Column(String(36), nullable=True)
    dKmR = Column(Integer, nullable=True)
    dFecEm = Column(Date, nullable=True)
    cPreFle = Column(Numeric(23, 8), nullable=True)
    de_id = Column(Integer, ForeignKey('de_documento_electronico.id'))
    de = relationship("De", back_populates="nota_remision")

    def get_dDesMotEmiNR(self):
        """
        Descripción del motivo de emisión
        """
        
        dic_descripciones = {
            "1" : "Traslado por ventas", 
            "2" : "Traslado por consignación", 
            "3" : "Exportación", 
            "4" : "Traslado por compra", 
            "5" : "Importación", 
            "6" : "Traslado por devolución", 
            "7" : "Traslado entre locales de la empresa",  
            "8" : "Traslado de bienes por transformación",
            "9" : "Traslado de bienes por reparación",
            "10" : "Traslado por emisor móvil",
            "11" : "Exhibición o Demostración",
            "12" : "Participación en ferias",
            "13" : "Traslado de encomienda",
            "14" : "Decomiso",
        }

        if self.iMotEmiNR and not self.dDesMotEmiNR:
            self.dDesMotEmiNR = dic_descripciones.get(str(self.iMotEmiNR), '')
            return self.dDesMotEmiNR
        return self.dDesMotEmiNR

    def get_dDesRespEmiNR(self):
        """
        Descripción del responsable de la emisión de la Nota de Remisión Electrónica
        """
        
        dic_descripciones = {
            "1" : "Emisor de la factura",
            "2" : "Poseedor de la factura y bienes",
            "3" : "Empresa transportista",
            "4" : "Despachante de Aduanas",
            "5" : "Agente de transporte o intermediario",
        }

        if self.iRespEmiNR and not self.dDesRespEmiNR:
            self.dDesRespEmiNR = dic_descripciones.get(str(self.iRespEmiNR), '')
            return self.dDesRespEmiNR
        return self.dDesRespEmiNR


class PagoTarjetaCD(MysqlConnection.Base):
    __tablename__ = 'de_pago_tarjeta_cd'

    def __init__(self):
        self.iDenTarj = ''
        self.dDesDenTarj = ''
        self.dRSProTar = ''
        self.dRUCProTar = ''
        self.dDVProTar = ''
        self.iForProPa = ''
        self.dCodAuOpe = ''
        self.dNomTit = ''
        self.dNumTarj = ''

    id = Column(Integer, primary_key=True)
    iDenTarj = Column(Integer, nullable=True)
    dDesDenTarj = Column(String(20), nullable=True)
    dRSProTar = Column(String(60), nullable=True)
    dRUCProTar = Column(String(8), nullable=True)
    dDVProTar = Column(Integer, nullable=True)
    iForProPa = Column(Integer, nullable=True)
    dCodAuOpe = Column(Integer, nullable=True)
    dNomTit = Column(String(30), nullable=True)
    dNumTarj = Column(Integer, nullable=True)
    medio_pago_id = Column(Integer, ForeignKey('de_medio_pago.id'))
    medio_pago = relationship("MedioPago", back_populates="pago_tarjeta_cd")


class PagoCheque(MysqlConnection.Base):
    __tablename__ = 'de_pago_cheque'

    def __init__(self):
        self.dNumCheq = ''
        self.dBcoEmi = ''

    id = Column(Integer, primary_key=True)
    dNumCheq = Column(String(8), nullable=True)
    dBcoEmi = Column(String(20), nullable=True)
    medio_pago_id = Column(Integer, ForeignKey('de_medio_pago.id'))
    medio_pago = relationship("MedioPago", back_populates="pago_cheque")


class Cuotas(MysqlConnection.Base):
    __tablename__ = 'de_cuotas'

    def __init__(self):
        self.cMoneCuo = ''
        self.dDMoneCuo = ''
        self.dMonCuota = ''
        self.dVencCuo = ''

    id = Column(Integer, primary_key=True)
    cMoneCuo = Column(String(3), nullable=True)
    dDMoneCuo = Column(String(20), nullable=True)
    dMonCuota = Column(Numeric(19, 4), nullable=True)
    dVencCuo = Column(Date, nullable=True)
    de_id = Column(Integer, ForeignKey('de_documento_electronico.id'))

    def get_dDMoneCuo(self, de):
        if self.cMoneCuo:
            valores = [val for key, val in de.dict_currency.items() if self.cMoneCuo in key]
            if not self.dDMoneCuo:
                # Obtenemos solo si está vacío el campo descripción, 
                # sino dejamos el que vino de la fuente
                self.dDMoneCuo = valores[0][1]
            return self.dDMoneCuo


class TransporteMercaderias(MysqlConnection.Base):
    __tablename__ = 'de_transporte_mercaderias'

    def __init__(self):
        self.iTipTrans = ''
        self.dDesTipTrans = ''
        self.iModTrans = ''
        self.dDesModTrans = ''
        self.iRespFlete = ''
        self.cCondNeg = ''
        self.dNuManif = ''
        self.dNuDespImp = ''
        self.dIniTras = ''
        self.dFinTras = ''
        self.cPaisDest = ''
        self.dDesPaisDest = ''

    id = Column(Integer, primary_key=True)
    iTipTrans = Column(Integer, nullable=True)
    dDesTipTrans = Column(String(7), nullable=True)
    iModTrans = Column(Integer, nullable=True)
    dDesModTrans = Column(String(10), nullable=True)
    iRespFlete = Column(Integer, nullable=True)
    cCondNeg = Column(String(3), nullable=True)
    dNuManif = Column(String(15), nullable=True)
    dNuDespImp = Column(String(16), nullable=True)
    dIniTras = Column(Date, nullable=True)
    dFinTras = Column(Date, nullable=True)
    cPaisDest = Column(String(3), nullable=True)
    dDesPaisDest = Column(String(30), nullable=True)
    de_id = Column(Integer, ForeignKey('de_documento_electronico.id'))
    de = relationship("De", back_populates="transporte_mercaderia")
    salida_mercaderias = relationship("SalidaMercaderias", uselist=False, back_populates="transporte_mercaderias")
    locales_entrega = relationship("LocalEntregaMercaderias")
    vehiculos = relationship("VehiculoMercaderias")
    transportista = relationship("Transportista", uselist=False, back_populates="transporte_mercaderias")

    def get_dDesTipTrans(self):
        """
        Descripción del tipo de transporte
        """
        
        dic_descripciones = {
            "1" : "Propio",
            "2" : "Tercero"
        }

        if self.iTipTrans and not self.dDesTipTrans:
            self.dDesTipTrans = dic_descripciones.get(str(self.iTipTrans), '')
        return self.dDesTipTrans

    def get_dDesModTrans(self):
        """
        Descripción del tipo de transporte
        """
        
        dic_descripciones = {
            "1" : "Terrestre",
            "2" : "Fluvial",
            "3" : "Aéreo",
            "4" : "Multimodal"
        }

        if self.iModTrans and not self.dDesModTrans:
            self.dDesModTrans = dic_descripciones.get(str(self.iModTrans), '')
        return self.dDesModTrans


class SalidaMercaderias(MysqlConnection.Base):
    __tablename__ = 'de_salida_mercaderias'

    def __init__(self):
        self.dDirLocSal = ''
        self.dNumCasSal = ''
        self.dComp1Sal = ''
        self.dComp2Sal = ''
        self.cDepSal = ''
        self.dDesDepSal = ''
        self.cDisSal = ''
        self.dDesDisSal = ''
        self.cCiuSal = ''
        self.dDesCiuSal = ''
        self.dTelSal = ''

    id = Column(Integer, primary_key=True)
    dDirLocSal = Column(String(255), nullable=True)
    dNumCasSal = Column(Integer, nullable=True)
    dComp1Sal = Column(String(255), nullable=True)
    dComp2Sal = Column(String(255), nullable=True)
    cDepSal = Column(Integer, nullable=True)
    dDesDepSal = Column(String(16), nullable=True)
    cDisSal = Column(Integer, nullable=True)
    dDesDisSal = Column(String(30), nullable=True)
    cCiuSal = Column(Integer, nullable=True)
    dDesCiuSal = Column(String(30), nullable=True)
    dTelSal = Column(Integer, nullable=True)
    transporte_mercaderias_id = Column(Integer, ForeignKey('de_transporte_mercaderias.id'))
    transporte_mercaderias = relationship("TransporteMercaderias", back_populates="salida_mercaderias")

    def get_datos_geograficos_sm(self):

        if self.cDepSal and not self.dDesDepSal:
            linea = filter_referencia_geografica('COD_DEPARTAMENTO', self.cDepSal)
            self.dDesDepSal = linea.get('DEPARTAMENTO', '')
        
        if self.cDisSal and not self.dDesDisSal:
            linea = filter_referencia_geografica('COD_DISTRITO', self.cDisSal)
            self.dDesDisSal = linea.get('DISTRITO', '')

        if self.cCiuSal and not self.dDesCiuSal:
            linea = filter_referencia_geografica('COD_CIUDAD', self.cCiuSal)
            self.dDesCiuSal = linea.get('CIUDAD', '')


class LocalEntregaMercaderias(MysqlConnection.Base):
    __tablename__ = 'de_local_entrega_mercaderias'

    def __init__(self):
        self.dDirLocEnt = ''
        self.dNumCasEnt = ''
        self.dComp1Ent = ''
        self.dComp2Ent = ''
        self.cDepEnt = ''
        self.dDesDepEnt = ''
        self.cDisEnt = ''
        self.dDesDisEnt = ''
        self.cCiuEnt = ''
        self.dDesCiuEnt = ''
        self.dTelEnt = ''

    id = Column(Integer, primary_key=True)
    dDirLocEnt = Column(String(255), nullable=True)
    dNumCasEnt = Column(Integer, nullable=True)
    dComp1Ent = Column(String(255), nullable=True)
    dComp2Ent = Column(String(255), nullable=True)
    cDepEnt = Column(Integer, nullable=True)
    dDesDepEnt = Column(String(16), nullable=True)
    cDisEnt = Column(Integer, nullable=True)
    dDesDisEnt = Column(String(30), nullable=True)
    cCiuEnt = Column(Integer, nullable=True)
    dDesCiuEnt = Column(String(30), nullable=True)
    dTelEnt = Column(Integer, nullable=True)
    transporte_mercaderias_id = Column(Integer, ForeignKey('de_transporte_mercaderias.id'))

    def get_datos_geograficos_em(self):

        if self.cDepEnt and not self.dDesDepEnt:
            linea = filter_referencia_geografica('COD_DEPARTAMENTO', self.cDepEnt)
            self.dDesDepEnt = linea.get('DEPARTAMENTO', '')
        
        if self.cDisEnt and not self.dDesDisEnt:
            linea = filter_referencia_geografica('COD_DISTRITO', self.cDisEnt)
            self.dDesDisEnt = linea.get('DISTRITO', '')

        if self.cCiuEnt and not self.dDesCiuEnt:
            linea = filter_referencia_geografica('COD_CIUDAD', self.cCiuEnt)
            self.dDesCiuEnt = linea.get('CIUDAD', '')


class VehiculoMercaderias(MysqlConnection.Base):
    __tablename__ = 'de_vehiculo_mercaderias'

    def __init__(self):
        self.dTiVehTras = ''
        self.dMarVeh = ''
        self.dTipIdenVeh = ''
        self.dNroIDVeh = ''
        self.dAdicVeh = ''
        self.dNroMatVeh = ''
        self.dNroVuelo = ''

    id = Column(Integer, primary_key=True)
    dTiVehTras = Column(String(10), nullable=True)
    dMarVeh = Column(String(10), nullable=True)
    dTipIdenVeh = Column(Integer, nullable=True)
    dNroIDVeh = Column(String(20), nullable=True)
    dAdicVeh = Column(String(20), nullable=True)
    dNroMatVeh = Column(String(7), nullable=True)
    dNroVuelo = Column(String(6), nullable=True)
    transporte_mercaderias_id = Column(Integer, ForeignKey('de_transporte_mercaderias.id'))


class Transportista(MysqlConnection.Base):
    __tablename__ = 'de_transportista'

    def __init__(self):
        self.iNatTrans = ''
        self.dNomTrans = ''
        self.dRucTrans = ''
        self.dDVTrans = ''
        self.iTipIDTrans = ''
        self.dDTipIDTrans = ''
        self.dNumIDTrans = ''
        self.cNacTrans = ''
        self.dDesNacTrans = ''
        self.dNumIDChof = ''
        self.dNomChof = ''
        self.dDomFisc = ''
        self.dDirChof = ''
        self.dNombAg = ''
        self.dRucAg = ''
        self.dDVAg = ''
        self.dDirAge = ''

    id = Column(Integer, primary_key=True)
    iNatTrans = Column(Integer, nullable=True)
    dNomTrans = Column(String(60), nullable=True)
    dRucTrans = Column(String(8), nullable=True)
    dDVTrans = Column(Integer, nullable=True)
    iTipIDTrans = Column(Integer, nullable=True)
    dDTipIDTrans = Column(String(20), nullable=True)
    dNumIDTrans = Column(String(20), nullable=True)
    cNacTrans = Column(String(3), nullable=True)
    dDesNacTrans = Column(String(30), nullable=True)
    dNumIDChof = Column(String(20), nullable=True)
    dNomChof = Column(String(60), nullable=True)
    dDomFisc = Column(String(150), nullable=True)
    dDirChof = Column(String(255), nullable=True)
    dNombAg = Column(String(60), nullable=True)
    dRucAg = Column(String(8), nullable=True)
    dDVAg = Column(Integer, nullable=True)
    dDirAge = Column(String(255), nullable=True)
    transporte_mercaderias_id = Column(Integer, ForeignKey('de_transporte_mercaderias.id'))
    transporte_mercaderias = relationship("TransporteMercaderias", back_populates="transportista")

    def get_dDTipIDTrans(self):
        """
        Descripción del tipo de documento de identidad del transportista
        """
        
        dic_descripciones = {
            "1" : "Cédula paraguaya",
            "2" : "Pasaporte",
            "3" : "Cédula extranjera",
            "4" : "Carnet de residencia",
        }

        if self.iTipIDTrans and not self.dDTipIDTrans:
            self.dDTipIDTrans = dic_descripciones.get(str(self.iTipIDTrans), '')
        return self.dDTipIDTrans

    def get_dDesNacTrans(self):
        """
        Descripción de la nacionalidad del transportista
        """

        if self.cNacTrans and not self.dDesNacTrans:
            dict_countries = get_dict_countries()
            valores = [val for key, val in dict_countries.items() if self.cNacTrans in key]
            self.dDesNacTrans = valores[0][0]
        return self.dDesNacTrans

class ItemVehiculo(MysqlConnection.Base):
    __tablename__ = 'de_item_vehiculo'

    def __init__(self):
        iTipOpVN = ''
        dDesTipOpVN = ''
        dChasis = ''
        dColor = ''
        dPotencia = ''
        dCapMot = ''
        dPNet = ''
        dPBruto = ''
        iTipCom = ''
        dDesTipCom = ''
        dNroMotor = ''
        dCapTracc = ''
        dAnoFab = ''
        cTipVeh = ''
        dCapac = ''
        dCilin = ''

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('de_item.id'))
    iTipOpVN = Column(Numeric(1), nullable=True)
    dDesTipOpVN = Column(String(30), nullable=True)
    dChasis = Column(String(17), nullable=True)
    dColor = Column(String(10), nullable=True)
    dPotencia = Column(Integer, nullable=True)
    dCapMot = Column(Integer, nullable=True)
    dPNet = Column(Numeric(10, 4), nullable=True)
    dPBruto = Column(Numeric(10, 4), nullable=True)
    iTipCom = Column(Numeric(1), nullable=True)
    dDesTipCom = Column(String(20), nullable=True)
    dNroMotor = Column(String(21), nullable=True)
    dCapTracc = Column(Numeric(10, 4), nullable=True)
    dAnoFab = Column(Integer, nullable=True)
    cTipVeh = Column(String(10), nullable=True)
    dCapac = Column(Integer, nullable=True)
    dCilin = Column(String(4), nullable=True)

    item = relationship('Item', back_populates="itemvehiculo")


class ItemRastreoMercaderia(MysqlConnection.Base):
    __tablename__ = 'de_item_rastreo_mercaderias'

    def __init__(self):
        dNumLote = ''
        dVencMerc = ''
        dNSerie = ''
        dNumPedi = ''
        dNumSegui = ''
        dNumReg = ''
        dNumRegEntCom = ''
        dNomPro = ''

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('de_item.id'))
    dNumLote = Column(String(80), nullable=True)
    dVencMerc = Column(Date, nullable=True)
    dNSerie = Column(String(10), nullable=True)
    dNumPedi = Column(String(20), nullable=True)
    dNumSegui = Column(String(20), nullable=True)
    dNumReg = Column(String(20), nullable=True)
    dNumRegEntCom = Column(String(20), nullable=True)
    dNomPro = Column(String(30), nullable=True)

    item = relationship('Item', back_populates="itemrastreomercaderia")


def insert_mysql_db(doc, session, proceso):
    try:
        doc.proceso_id = proceso.id
        session.add(doc)
        session.commit()
    except Exception as ex:
        session.rollback()
        print(f"Error al guardar en la base de datos: {ex}")
        now = datetime.now()
        log = Log(proceso_id=proceso.id, eventos=f"Error en metodo insert_mysql_db: {ex}",
                  categoria=Log.ERROR, fecha_hora=now)
        session.add(log)
        session.commit()


