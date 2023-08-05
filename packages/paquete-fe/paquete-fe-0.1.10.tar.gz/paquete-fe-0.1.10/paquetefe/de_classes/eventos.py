from datetime import datetime
from de_classes.mysql_db_admin import De
from lxml import etree
from .gen_xml import CrearNodoEventoRaiz

def gen_xml_evento(session, evento_id, dict_event_params):
    try:        
        # Podriamos tener hasta 15 eventos, pero seguramente lo haremos por cada uno..
        root = CrearNodoEventoRaiz() #verif el True para el xsd local        
        # Grupos de campos generales del evento (independiente de cual sea)
        r_ges_eve_node = etree.SubElement(root, "rGesEve")        
        root.append(r_ges_eve_node)
        r_eve_node = etree.SubElement(r_ges_eve_node, "rEve")
        r_eve_node.set("Id", str(evento_id))
        r_ges_eve_node.append(r_eve_node)
        d_fec_firma_node = etree.SubElement(r_eve_node, "dFecFirma")
        d_fec_firma_node.text = str(datetime.now())
        r_eve_node.append(d_fec_firma_node)
        d_ver_for_node = etree.SubElement(r_eve_node, "dVerFor")
        d_ver_for_node.text = "150" #esto no debe ser una constante!!
        r_eve_node.append(d_ver_for_node)
        g_group_tievt_node = etree.SubElement(r_eve_node, "gGroupTiEvt")

        """
            AQUI ES DONDE DEPENDIENDO DEL TIPO DE EVENTO SE DEBERIAN AGREGAR DISTINTOS NODOS
        """
        # El "cuerpo" especifico de cada tipo de evento...
        gen_evento_body(g_group_tievt_node, dict_event_params)
        r_eve_node.append(g_group_tievt_node)        
        tree = etree.ElementTree(root)
        xmlstr = etree.tostring(root).decode('utf-8')
        return xmlstr
    except Exception as ex:
        print(f"Error: {ex}")
        raise


def gen_evento_body(g_group_tievt_node, ordered_dict):
    # Del diccionario ordenado, vamos agregando los nodos!
    try:
        for key, value in ordered_dict.items(): 
            if not value:
                node = etree.SubElement(g_group_tievt_node, key)
                g_group_tievt_node.append(node)
            else:
                subnode = etree.SubElement(node, key)
                subnode.text = value
                node.append(subnode)        
        return g_group_tievt_node
    except Exception as ex:
        print(f"Error: {ex}")
        raise
