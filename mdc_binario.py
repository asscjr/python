# Programa que lê um arquivo binário com uma coleção de N pares de valores inteiros e calcule o máximo divisor comum

import struct
#Subprogramas
def mdc(a, b):
	if b == 0:
		return a
	return mdc(b, a % b)

#Programa Principal
try:
	with open('valores.bin', 'rb') as arq:
		inteiro = struct.unpack('i', arq.read(4))[0]
		for i in range(inteiro):
			a = struct.unpack('i', arq.read(4))[0]
			b = struct.unpack('i', arq.read(4))[0]
			if a < b:
				print(mdc(b, a))
			else:
				print(mdc(a, b))
		
 
except IOError:
	print('Erro ao abrir ou ao manipular o arquivo.')