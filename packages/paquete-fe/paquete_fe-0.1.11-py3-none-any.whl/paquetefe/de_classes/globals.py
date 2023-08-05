import csv
import traceback
import sys
import os

#Metodos para validaciones y demás que pueden ser utilizadas en todas las clases
#@staticmethod
def isEmpty(any_structure):
#Aplica no solamente con variables de tipo string, sino también con dictionary, list, set y tuple
	if any_structure:
		return False
	else:
		return True


#@staticmethod
def pad_zeros(number,size):

	"""
	Método para completar con ceros a la izquierda
	Recibe el número y la longitud que debe tener
	Retorna el número con la cantidad de ceros a la izquierda que necesite
	"""
	return str(number).zfill(size)


def get_digito_verificador(numero, basemax=11):
	numero = str(numero)
	numero_al = ""
	for i in range(0, len(numero)):
		c = numero[i:i + 1]
		codigo = ord(c.upper())
		if not (codigo >= 48 and codigo <= 57):
			numero_al = numero_al + codigo
		else:
			numero_al = numero_al + c
	k = 2
	total = 0
	for i in range(len(numero_al), 0, - 1):
		if (k > basemax):
			k = 2
		numero_aux = numero_al[i - 1:i]
		numero_entero = int(numero_aux)
		total = total + (numero_entero * k)
		k = k + 1

	resto = total % 11
	if (resto > 1):
		digito = 11 - resto
	else:
		digito = 0
	digito_verificador = digito
	return str(digito_verificador)



