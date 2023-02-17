# Programa auxiliar para criar e ler os valores em binario utilizados no programa que identifica o mdc

import struct
try:
	with open('valores.bin', 'wb') as arq:
		bloco = struct.pack('i', 2)
		bloco += struct.pack('i', 12)
		bloco += struct.pack('i', 18)
		bloco += struct.pack('i', 25)
		bloco += struct.pack('i', 26)
		arq.write(bloco)

	with  open('valores.bin', 'rb') as arq:
		byte = arq.read(4)
		while byte != b"":
			inteiro = struct.unpack('i', byte)[0]
			print(inteiro, end=' ')
			byte = arq.read(4)
		print()

except IOError:
	print('Erro ao abrir o arquivo.')