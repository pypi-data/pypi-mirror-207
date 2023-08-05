from sqlalchemy import create_engine, Column, ForeignKey, String, Integer, \
                       Date, DateTime, Numeric, SmallInteger, Boolean, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


class VistaConnection:
    Base = declarative_base()
    
    def __init__(self, DATABASE):
        self.engine = create_engine(
            f'mysql+mysqlconnector://'
            f'{DATABASE["USER"]}:{DATABASE["PASSWORD"]}@'
            f'{DATABASE["HOST"]}:{DATABASE["PORT"]}/'
            f'{DATABASE["NAME"]}'
        )

    def connect(self):
        Session = sessionmaker()
        Session.configure(bind=self.engine)
        session = Session()
        self.create_tables(session)
        return session

    def create_tables(self, session):
        print("Creando todas las tablas")
        self.Base.metadata.create_all(self.engine)
        session.commit()


class De(VistaConnection.Base):
    __tablename__ = 'v_documento_electronico'
    id = Column(Integer, primary_key=True)
    # dVerFor = Column(Numeric(3), nullable=False)
    # _Id = Column(String(44), nullable=False)
    # dDVId = Column(Integer, nullable=False)
    # dFecFirma = Column(DateTime, nullable=False)
    # dSisFact = Column(Numeric(1), nullable=False)
    # iTipEmi = Column(Numeric(1), nullable=False)
    # dDesTipEmi = Column(String(12), nullable=False)
    # dCodSeg = Column(Numeric(9), nullable=False)
    dInfoEmi = Column(String(3000), nullable=True)
    dInfoFisc = Column(String(3000), nullable=True)
    iTiDE = Column(Numeric(2), nullable=False)
    dDesTiDE = Column(String(40), nullable=False)
    dNumTim = Column(Numeric(8), nullable=False)
    dEst = Column(String(3), nullable=False)
    dPunExp = Column(String(3), nullable=False)
    dNumDoc = Column(String(7), nullable=False)
    dSerieNum = Column(String(2), nullable=True)
    dFeIniT = Column(Date, nullable=False)
    #dFeFinT = Column(Date, nullable=True)
    dFeEmiDE = Column(DateTime, nullable=False)
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
    # dRucEm = Column(String(8), nullable=False)
    # dDVEmi = Column(Integer, nullable=False)
    # iTipCont = Column(Numeric(1), nullable=False)
    # cTipReg = Column(Numeric(2), nullable=True)
    # dNomEmi = Column(String(255), nullable=False)
    # dNomFanEmi = Column(String(255), nullable=True)
    # dDirEmi = Column(String(255), nullable=False)
    # dNumCas = Column(Numeric(6), nullable=False)
    # dCompDir1 = Column(String(255), nullable=True)
    # dCompDir2 = Column(String(255), nullable=True)
    # cDepEmi = Column(Numeric(2), nullable=False)
    # dDesDepEmi = Column(String(16), nullable=False)
    # cDisEmi = Column(Numeric(4), nullable=True)
    # dDesDisEmi = Column(String(30), nullable=True)
    # cCiuEmi = Column(Numeric(5), nullable=False)
    # dDesCiuEmi = Column(String(30), nullable=False)
    # dTelEmi = Column(Numeric(15), nullable=False)
    # dEmailE = Column(String(80), nullable=False)
    # dDenSuc = Column(String(30), nullable=True)
    iNatRec = Column(Numeric(1), nullable=False)
    iTiOpe = Column(Numeric(1), nullable=False)
    cPaisRec = Column(String(3), nullable=False)
    dDesPaisRe = Column(String(30), nullable=False)
    iTiContRec = Column(Numeric(1), nullable=True)
    dRucRec = Column(String(8), nullable=True)
    dDVRec = Column(Integer, nullable=True)
    iTipIDRec = Column(Numeric(1), nullable=True)
    dDTipIDRec = Column(String(20), nullable=True)
    dNumIDRec = Column(String(20), nullable=True)
    dNomRec = Column(String(255), nullable=False)
    dNomFanRec = Column(String(255), nullable=True)
    dDirRec = Column(String(255), nullable=True)
    dNumCasRec = Column(Numeric(6), nullable=False)
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
    iIndPres = Column(Numeric(1), nullable=False)
    dDesIndPres = Column(String(30), nullable=False)
    dFecEmNR = Column(DateTime, nullable=True)

    # COMPRAS PÚBLICAS
    dModCont = Column(String(2), nullable=True)
    dEntCont = Column(Integer, nullable=True)
    dAnoCont = Column(Integer, nullable=True)
    dSecCont = Column(Integer, nullable=True)
    dFeCodCont = Column(Date, nullable=True)
    
    iMotEmi = Column(Numeric(2), nullable=False)
    dDesMotEmi = Column(String(20), nullable=True)
    
    dKmR = Column(Numeric(5), nullable=True)
    dFecEm = Column(Date, nullable=True)

    iCondOpe = Column(Numeric(1), nullable=False)
    dDCondOpe = Column(String(7), nullable=False)
    iCondCred = Column(Numeric(1), nullable=False)
    dDCondCred = Column(String(6), nullable=False)
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
    dTotOpe = Column(Numeric(23, 8), nullable=False)
    dTotDesc = Column(Numeric(23, 8), nullable=False)
    dTotDescGlotem = Column(Numeric(23, 8), nullable=False)
    dTotAntItem = Column(Numeric(23, 8), nullable=False)
    dTotAnt = Column(Numeric(23, 8), nullable=False)
    dPorcDescTotal = Column(Numeric(11, 8), nullable=False)
    dDescTotal = Column(Numeric(23, 8), nullable=False)
    dAnticipo = Column(Numeric(23, 8), nullable=False)
    dRedon = Column(Numeric(7, 4), nullable=False)
    dComi = Column(Numeric(23, 8), nullable=True)
    dTotGralOpe = Column(Numeric(23, 8), nullable=False)
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
    dCarQR = Column(String(600), nullable=False)
    dInfAdic=Column(String(5000), nullable=True)
        
    
class Actividad(VistaConnection.Base):
    __tablename__ = 'v_actividad_economica'

    id = Column(Integer, primary_key=True)
    de_id = Column(Integer, nullable=True)
    cActEco = Column(String(8), nullable=False)
    dDesActEco = Column(String(300), nullable=False)


class Item(VistaConnection.Base):
    __tablename__ = 'v_item'

    id = Column(Integer, primary_key=True)
    de_id = Column(Integer, nullable=True)
    dCodInt = Column(String(20), nullable=False)
    dDesProSer = Column(String(120), nullable=False)
    cUniMed = Column(Numeric(5), nullable=False)
    dDesUniMed = Column(String(10), nullable=False)
    dCantProSer = Column(Numeric(14, 4), nullable=False)
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
    dPUniProSer = Column(Numeric(23, 8), nullable=False)
    dTiCamIt = Column(Numeric(9, 4), nullable=True)
    dTotBruOpeItem = Column(Numeric(23, 8), nullable=False)
    dDescItem = Column(Numeric(23, 8), nullable=True)
    dPorcDesIt = Column(Numeric(11, 8), nullable=True)
    dDescGloItem = Column(Numeric(23, 8), nullable=True)
    dAntPreUniIt = Column(Numeric(23, 8), nullable=True)
    dAntGloPreUniIt = Column(Numeric(23, 8), nullable=True)
    dTotOpeItem = Column(Numeric(23, 8), nullable=False)
    dTotOpeGs = Column(Numeric(23, 8), nullable=True)
    iAfecIVA = Column(Numeric(1), nullable=False)
    dDesAfecIVA = Column(String(23), nullable=False)
    dPropIVA = Column(Numeric(3), nullable=False)
    dTasaIVA = Column(Numeric(2), nullable=False)
    dBasGravIVA = Column(Numeric(23, 8), nullable=False)
    dLiqIVAItem = Column(Numeric(23, 8), nullable=False)


class MedioPago(VistaConnection.Base):
    __tablename__ = 'v_medio_pago'

    id = Column(Integer, primary_key=True)
    de_id = Column(Integer, nullable=True)
    iTiPago = Column(Numeric(2), nullable=True)
    dDesTiPag = Column(String(30), nullable=True)
    dMonTiPag = Column(Numeric(23, 8), nullable=True)
    cMoneTiPag = Column(String(3), nullable=True)
    dDMoneTiPag = Column(String(20), nullable=True)
    dTiCamTiPag = Column(Numeric(23, 8), nullable=True)

    # PAGO TARJETA CRÉDITO-DÉBITO
    iDenTarj = Column(Integer, nullable=True)
    dDesDenTarj = Column(String(20), nullable=True)
    dRSProTar = Column(String(60), nullable=True)
    dRUCProTar = Column(String(8), nullable=True)
    dDVProTar = Column(Integer, nullable=True)
    iForProPa = Column(Integer, nullable=True)
    dCodAuOpe = Column(Integer, nullable=True)
    dNomTit = Column(String(30), nullable=True)
    dNumTarj = Column(Integer, nullable=True)

    # PAGO CHEQUE
    dNumCheq = Column(String(8), nullable=True)
    dBcoEmi = Column(String(20), nullable=True)
    

class Cuotas(VistaConnection.Base):
    __tablename__ = 'v_cuotas'

    id = Column(Integer, primary_key=True)
    de_id = Column(Integer, nullable=True)
    cMoneCuo = Column(String(3), nullable=True)
    dDMoneCuo = Column(String(20), nullable=True)
    dMonCuota = Column(Numeric(19, 4), nullable=True)
    dVencCuo = Column(Date, nullable=True)
    
    

class Autofactura(VistaConnection.Base):
    __tablename__ = 'v_autofactura'

    id = Column(Integer, primary_key=True)
    de_id = Column(Integer, nullable=True)
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


class DocumentoAsociado(VistaConnection.Base):
    __tablename__ = 'v_documento_asociado'

    id = Column(Integer, primary_key=True)
    de_id = Column(Integer, nullable=True)
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
    

class NotaRemision(VistaConnection.Base):
    __tablename__ = 'v_nota_remision'

    id = Column(Integer, primary_key=True)
    de_id = Column(Integer, nullable=True)
    iMotEmiNR = Column(Integer, nullable=True)
    dDesMotEmiNR = Column(String(60), nullable=True)
    iRespEmiNR = Column(Integer, nullable=True)
    dDesRespEmiNR = Column(String(36), nullable=True)
    dKmR = Column(Integer, nullable=True)
    dFecEm = Column(Date, nullable=True)

    # TRANSPORTE MERCADERÍAS
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

    # SALIDA DE MERCADERÍAS
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

    # ENTREGA DE MERCADERIAS
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

    #VEHICULO MERCADERIAS
    dTiVehTras = Column(String(10), nullable=True)
    dMarVeh = Column(String(10), nullable=True)
    dTipIdenVeh = Column(Integer, nullable=True)
    dNroIDVeh = Column(String(20), nullable=True)
    dAdicVeh = Column(String(20), nullable=True)
    dNroMatVeh = Column(String(6), nullable=True)
    dNroVuelo = Column(String(6), nullable=True)

    # TRANSPORTISTA
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
