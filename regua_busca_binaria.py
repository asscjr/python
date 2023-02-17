# Programa para reforçar os conceitos do algoritmo de busca binária

#Subprogramas
def printar(vetor):	#Função para imprimir a régua
	for i in range(len(vetor) - 1):
		print('%.2d' % (i + 1), vetor[i])

def regua(vetor, meio, n):	#Função para criar a régua
	for i in range(n):
		vetor[meio] += '-'
	return None

def subIntervalos(vetor, inicio, fim, n):	#Função para encontrar os subIntervalos
	if n != 0:
		meio = (inicio + fim) // 2

		regua(vetor, meio, n)
		subIntervalos(vetor, inicio, meio, n - 1)
		subIntervalos(vetor, meio, fim, n - 1)
	return None

def pontosMedios(vetor, n):
	subIntervalos(vetor, 0, len(vetor) - 1, n)
	return None

#Programa Principal
n = int(input())

vetor = [''] * 2 ** n #Vetor para armazenar a régua

pontosMedios(vetor, n)
printar(vetor)