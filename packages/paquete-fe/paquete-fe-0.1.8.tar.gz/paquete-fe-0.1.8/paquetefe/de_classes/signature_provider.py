from .signature_providers.cima.cima_service_client import CimaServiceClient
from .signature_providers.code100.code100_service_client import Code100ServiceClient
from .signature_providers.factury.factury_service_client import FacturyServiceClient
import os
from zipfile import ZipFile
from .process_mysql import log_register
from de_classes.mysql_db_admin import Log


class SignatureProvider:
    def set_provider(self, provider_data):
        provider = None
        if provider_data['NAME'] == 'CIMA':
            provider = CimaServiceClient(provider_data['URL'], provider_data['USER'], provider_data['PASSWORD'],
                                         provider_data['MAX_RETRY'], provider_data['VELOCITY'])
        elif provider_data['NAME'] == 'CODE100':
            provider = Code100ServiceClient(provider_data['URL'], provider_data['USER'], provider_data['PASSWORD'],
                                            provider_data['MAX_RETRY'], provider_data['VELOCITY'])
        elif provider_data['NAME'] == 'FACTURY':
            provider = FacturyServiceClient(provider_data['URL'], provider_data['API_TOKEN'],
                                            provider_data['MAX_RETRY'], provider_data['VELOCITY'])
        else:
            print("El proveedor seleccionado no se encuentra habilitado")

        return provider

    def write_zip_file(self, proceso, list_xml_files, session, OUTPUT_PATH):
        #path_zip_file = f'{OUTPUT_PATH}/{proceso.id}/lote.zip'
        path_zip_file = os.path.join(OUTPUT_PATH, 'lote.zip')
        with ZipFile(path_zip_file, 'w') as zip:
            for file_path in list_xml_files:
                file = open(file_path, "rb").read()
                file_name = os.path.split(file_path)[-1]
                zip.writestr(file_name, file)
        log_register(session, proceso.id, f"Fue creado el archivo zip satisfactoriamente: {path_zip_file}", Log.INFO)
        return path_zip_file

