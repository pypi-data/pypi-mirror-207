from lxml import etree
import logging
import os
from datetime import datetime, timedelta
from .globals import get_digito_verificador

xsd_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'xsd_files/siRecepDE_v150.xsd')


def isXmlValid(de, xml_string, file_name):
    try:
        #url = "https://ekuatia.set.gov.py/sifen/xsd/siRecepDE_v150.xsd"
        '''
            Primero las validaciones customizadas (no esta en el xsd)
            Despues, contra el XSD (porque sino si o si salta porque falta el Tag Signature al Catch) 
        '''

        #Custom 1: Si hay direccion, informar tambien la ciudad y departamento obligatoriamente
        '''
        if de.dDirRec:
            if not de.cCiuRec or not de.cDepRec:
                err_msj = "ERROR: cuando el valor de la direccion del receptor tiene un valor, " \
                          "se debe informar tambien la ciudad y el departamento del receptor"
                print(err_msj)
                return False, err_msj
        
        #Custom 2: Digito verificador que viene en el .dat vs. el que corresponde al RUC
        if de.dRucRec:
            digito_verificador = get_digito_verificador(de.dRucRec)
            if str(digito_verificador) != str(de.dDVRec):
                err_msj = f"ERROR: El digito verificador del RUC del Receptor ({de.dRucRec}) " \
                          f"deberia ser {digito_verificador} en lugar de {de.dDVRec}"
                print(err_msj)
                return False, err_msj
        '''
        """
            Custom 3: Fecha de emision (dFeEmiDE)
            Segun el MT "Se aceptará como límites técnicos del sistema, que la fecha de emisión del DE sea: 
            Atrasada hasta 720 horas (30 días) 
            Adelantada hasta 120 horas (5 días)             
        """
        #fecha_atrasada = de.dFeEmiDE - timedelta(days=30)
        #fecha_adelantada = de.dFeEmiDE + timedelta(days=5)

        """
            fecha_atrasada = datetime.strftime(de.dFeEmiDE, '%Y-%m-%d') - timedelta(days=30)
        fecha_adelantada = datetime.strftime(de.dFeEmiDE, '%Y-%m-%d') + timedelta(days=5)

        if de.dFeEmiDE.date() < fecha_atrasada.date():
            err_msj = f"ERROR: La fecha de Emision (dFeEmiDE) no puede ser menor a 720 horas (30 dias), " \
                      f"el valor de la fecha actual es ({de.dFeEmiDE})"
            return False, err_msj
        if de.dFeEmiDE.date() > fecha_adelantada.date():
            err_msj = f"ERROR: La fecha de Emision (dFeEmiDE) no puede estar adelantada mas de 5 dias), " \
                      f"el valor de la fecha actual es ({de.dFeEmiDE})"
            return False, err_msj
        """

        """
            Custom 4: Fecha de vencimiento (dVencPag)
            Segun el MT "Se aceptará como límites técnicos del sistema, que la fecha de emisión del DE sea: 
            Atrasada hasta 720 horas (30 días) 
            Adelantada hasta 120 horas (5 días)             
        """


        # Validacion contra el XSD
        xmlschema_doc = etree.parse(xsd_path)
        schema = etree.XMLSchema(xmlschema_doc)
        doc = etree.fromstring(xml_string)
        schema.assert_(doc)
        return True, ''
               
    except AssertionError as x:
        if "Signature" not in str(x):
            error_message = f'Error: {str(x)}'
            print(error_message)
            return False, error_message
        else:
            return True, ''

