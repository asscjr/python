# Programa que lê a entrada padrão o nome de um arquivo texto, contendo pontos no espaço bidimensional representando coordenadas x e y.
# O programa é capaz de dizer:
#	. o centroide;
#	. qual é o ponto mais próximo do centroide.

#Programa Principal
arq = input()

somaX = 0
somaY = 0
qnt = 0

dados = open(arq, 'r')

linha = dados.readline()

while linha != '':
	decimal = linha.split()
	
	somaX += float(decimal[0])
	somaY += float(decimal[1])
	qnt += 1

	linha = dados.readline()

mX = somaX/qnt
mY = somaY/qnt

print('Centroide: ' + '(%1.1f'%mX + ', ' + '%1.1f'%mY + ')')

dados.close()

dados = open(arq, 'r')

linha = dados.readline()

decimal = linha.split()

d = ((float(decimal[0]) - mX) ** 2 + (float(decimal[1]) - mY) ** 2) ** (1/2)

while linha != '':
	decimal = linha.split()

	x = ((float(decimal[0]) - mX) ** 2 + (float(decimal[1]) - mY) ** 2) ** (1/2)

	if x < d:
		d = x
		pmp = decimal

	linha = dados.readline()

print('Ponto Mais Próximo: ' + '(' + str(pmp[0]) + ', ' + str(pmp[1]) + ')')

dados.close()