from lxml import etree
import os


try:
    xsd_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'xsd_files/siRecepEvento_v150.xsd')
    xml_file = 'caso xml generado.xml'

    # Validacion contra el XSD
    xmlschema_doc = etree.parse(xsd_path)
    schema = etree.XMLSchema(xmlschema_doc)
    tree = etree.parse(xml_file)
    #root = tree.getroot()
    schema.assert_(tree)
    print('paso la validacion!')

except AssertionError as x:
    if "Signature" not in str(x):
        error_message = f'Error: {str(x)}'
        print(error_message)
        print('todo mal con la firma')
    else:
        print('todo mal')

