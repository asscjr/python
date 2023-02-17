# Programa que lê a entrada padrão contendo valores inteiros na forma binária e escreve na saída padrão cada valor convertido para as bases 3 a 10.

#Subprogramas
def binario():	#Função que lê os números binários do usuário
	binarios = []

	x = True

	while x == True:
		binario = input()

		if binario != '-1':
			binarios.append(binario)
		else:
			x = False
	return binarios

def decimal(vetor):	#Função que converte binário em decimal
	decimais = [0] * len(vetor)
	for i in range(len(vetor)):
		j = 0
		n = len(vetor[i]) - 1
		while n >= 0:
			decimais[i] += int(vetor[i][j]) * 2 ** n
			n -= 1
			j += 1
	return decimais

def converte(vetor):	#Função que converte decimal em qualquer base
	convertidos = [''] * len(vetor)
	for i in range(len(vetor)):
		base = 3
		while base != 10:
			decimal = vetor[i]
			convertido = ''
			if decimal != 0:
				while decimal > 0:
					resto = decimal % base
					convertido = str(resto) + convertido
					decimal = decimal // base
				convertidos[i] += convertido + ' '
			
			else:
				convertido = '0'
				convertidos[i] += convertido + ' '

			base += 1
	return convertidos

#Programa Principal
binarios = binario()
decimais = decimal(binarios)
convertidos = converte(decimais)

for i in range(len(binarios)):
	print(convertidos[i] + str(decimais[i]))