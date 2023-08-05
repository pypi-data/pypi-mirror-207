import csv
import traceback
import sys
import os


def read_referencia_geografica():
    this_folder = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(this_folder, 'referencia_geografica.csv')
    with open(my_file, mode='r', encoding='utf8') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        return list(csv_reader)


list_ref_geo = read_referencia_geografica()


def filter_referencia_geografica(column, value):
    """
        Permite filtrar el csv de referencia geografica para obtener un registro
        a partir del valor de una columna. 
        Columnas del csv: 
        COD_DEPARTAMENTO;DEPARTAMENTO;COD_DISTRITO;DISTRITO;COD_CIUDAD;CIUDAD
        Parámetros:
        column: Nombre de la columna a filtrar
        value: Valor por el cual se filtra 
        Resultado:
        Diccionario de un registro

    """
    global list_ref_geo  
    value = str(value)  
    filtered = list(filter(lambda row: row[column] == value, list_ref_geo))
    first = filtered[0] if filtered else {}
    return first

def get_dict_geography():
    data_dict = {}
    try:
        """
            Agregamos a manopla la principal ciudad que vendra de claro: ASUNCION, porque en el csv
            viene como "ASUNCION(DISTRITO) es un caso especial porque tampoco tiene departamento, sino 
            que es el distrito CAPITAL.
        """
        row = (1, "CAPITAL", 1, "ASUNCION (DISTRITO)", 1, "ASUNCION (DISTRITO)")
        data_dict["ASUNCION"] = row

        row = (12, "CENTRAL", 161, "ÑEMBY", 5975, "ÑEMBY")
        data_dict["ÑEMBY"] = row

        row = (6, "CAAGUAZU", 61, "CNEL. OVIEDO", 2937, "CNEL. OVIEDO")
        data_dict["CORONEL OVIEDO"] = row

        this_folder = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(this_folder, 'referencia_geografica.csv')
        with open(my_file, encoding='utf8') as f_obj:
            reader = csv.reader(f_obj, delimiter=';')
            for line in reader:
                if line[1].strip() != "DEPARTAMENTO":
                    cod_departamento = line[0].strip()
                    desc_departamento = line[1].strip()
                    cod_distrito = line[2].strip()
                    desc_distrito = line[3].strip()
                    cod_ciudad = line[4].strip()
                    desc_ciudad = line[5].strip()
                    row = (cod_departamento, desc_departamento, cod_distrito, 
                            desc_distrito, cod_ciudad, desc_ciudad)
                    data_dict[desc_ciudad] = row
        return data_dict
    except Exception:
        traceback.print_exc()
        print("Unexpected error:", sys.exc_info()[0])
        raise


def get_dict_currency():
    data_dict = {}
    try:
        """
            Descargamos la lista de monedas en base al ISO 4217
            Link de referencia del MT: https://www.currency-iso.org/en/home/tables/table-a1.html
        """
        this_folder = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(this_folder, 'currency_iso_4217_table.csv')
        with open(my_file, encoding='utf8') as f_obj:
            reader = csv.reader(f_obj, delimiter=';')
            for line in reader:
                if line[1].strip() != "currency":
                    country = line[0].strip()
                    currency = line[1].strip()
                    currency_code = line[2].strip()
                    row = (country, currency, currency_code)
                    data_dict[currency_code] = row
        return data_dict
    except Exception:
        traceback.print_exc()
        print("Unexpected error:", sys.exc_info()[0])
        raise


def get_dict_countries():
    data_dict = {}
    try:
        """
            Descargamos la lista de paises en base a la CODIFICACION DE PAISES Estandar Internacional ISO 3166
            Link csv disponible: https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes/tree/master/all
        """
        this_folder = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(this_folder, 'countries_iso3166.csv')
        with open(my_file, encoding='utf8') as f_obj:
            reader = csv.reader(f_obj, delimiter=';')
            for line in reader:
                if line[0].strip() != "country":
                    country = line[0].strip()
                    code_three_dig = line[1].strip()
                    row = (country, code_three_dig)
                    data_dict[code_three_dig] = row
        return data_dict
    except Exception:
        traceback.print_exc()
        print("Unexpected error:", sys.exc_info()[0])
        raise


