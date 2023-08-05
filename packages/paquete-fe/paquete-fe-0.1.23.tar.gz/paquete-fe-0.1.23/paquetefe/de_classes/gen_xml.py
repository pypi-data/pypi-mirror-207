from lxml import etree 
import re
from io import StringIO


def CrearNodoRaiz(self, test=False):
    #Trate de varias formas para que genere en el mismo orden, sin exito hasta el momento
    if test:
        attr_qname = etree.QName("http://www.w3.org/2001/XMLSchema-instance", "noNamespaceSchemaLocation")
        nsmap = {"xsi": "http://www.w3.org/2001/XMLSchema-instance"}
        #se crea el nodo raiz, con los namespaces. Nivel 0
        root = etree.Element("rDE",
                        {attr_qname: "siRecepDE_v150.xsd"},
                        nsmap=nsmap)
        return root
    else:
        attr_qname = etree.QName("http://www.w3.org/2001/XMLSchema-instance", "schemaLocation")
        nsmap = {None: "http://ekuatia.set.gov.py/sifen/xsd",
                       "xsi": "http://www.w3.org/2001/XMLSchema-instance"}
        #se crea el nodo raiz, con los namespaces. Nivel 0
        root = etree.Element("rDE",
                        {attr_qname: "http://ekuatia.set.gov.py/sifen/xsd siRecepDE_v150.xsd"},
                        nsmap=nsmap)
        return root


def EsTagInnecesario(self, etiqueta, valorNodo=None, ValorAtributo=None):
    if etiqueta not in ("dDVId", "dNumCas","dTotOpe", "dTotDesc","dTotDescGlotem", "dTotAntItem", "dTotAnt",
                        "dPorcDescTotal", "dDescTotal", "dAnticipo", "dRedon", "dTotGralOpe", "dPropIVA",
                        "dLiqIVAItem", "dTasaIVA", "dBasGravIVA", "dDVEmi", "dDVRec", "dNumCasRec"):
        if valorNodo is None and ValorAtributo is None:
            return False
        elif re.search("^0+$",str(valorNodo)) or re.search("^0+$",str(ValorAtributo)) \
                or str(valorNodo).strip() == "" \
                or str(ValorAtributo).strip() == "":
            return True
        else:
            return False
    else:
        return False


def AgregarNodoHijo(self, nodoPadre, etiqueta, valorNodo=None, atributo=None, ValorAtributo=None):
    #Antes de agregar un Tag que no contiene un valor, o es 0... validamos. Salvo dInfoFisc
    if not EsTagInnecesario(self,etiqueta,valorNodo,ValorAtributo):
        nodoHijo = etree.SubElement(nodoPadre, etiqueta)

        if valorNodo:
            nodoHijo.text = str(valorNodo).strip()

        if atributo and ValorAtributo:
            nodoHijo.set(atributo, str(ValorAtributo).strip())

        return nodoHijo


def ReemplazarNodoRaiz(self, xml_string):
    #reemplazamos en seco y sin dudar, mil formas de cambiar los atributos del namespace
    close_rde = xml_string.find('>')
    sifen_xmlns = '<rDE xmlns="http://ekuatia.set.gov.py/sifen/xsd" ' \
                  'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" ' \
                  'xsi:schemaLocation="http://ekuatia.set.gov.py/sifen/xsd siRecepDE_v150.xsd">'
    output_line = sifen_xmlns + xml_string[close_rde+1:]
    root = etree.fromstring(output_line)
    tree = etree.ElementTree(root)
    return tree


def CrearNodoEventoRaiz():    
    #No aplica como en DE armar primero para el XSD local. Directo apuntando a los lions.
    attr_qname = etree.QName("http://www.w3.org/2001/XMLSchema-instance", "schemaLocation")
    nsmap = {None: "http://ekuatia.set.gov.py/sifen/xsd",
                    "xsi": "http://www.w3.org/2001/XMLSchema-instance"}    
    root = etree.Element("gGroupGesEve",
                    {attr_qname: "http://ekuatia.set.gov.py/sifen/xsd siRecepEvento_v150.xsd"},
                    nsmap=nsmap)
    return root


