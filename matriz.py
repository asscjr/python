# Programa que lê a entrada padrão, contendo dois números inteiros separados por um espaço em branco, representando as duas dimensões de uma matriz bidimensional. 
# A matriz é gerada com valores aleatórios, via função randint importada do módulo random, no intervalo 100 a 999.
# O programa é capaz de dizer:
#	. O conteúdo da matriz;
#	. A posição (linha e coluna) do maior valor sorteado e o seu respectivo valor;
#	. A soma de cada linha, de todas as linhas da matriz;
#	. A soma de cada coluna, de todas as colunas da matriz.

#Subprogramas
def criarMatriz(linhas, colunas):	#Função para criar matriz
	from random import randint
	matriz = [None] * linhas
	for i in range(linhas):
		matriz[i] = [0] * colunas
		for j in range(colunas):
			matriz[i][j] = randint(100, 999)
	return matriz

def printar(vetor, linhas, colunas):	#Função para imprimir a matriz
	for i in range(linhas):
		for j in range(colunas):
			print(vetor[i][j], end = ' ')
		print()
	print()
	return None

def maior(vetor, linhas, colunas):	#Função para encontrar o maior valor e sua posição
	maior = vetor[0][0]
	posL = 0
	posC = 0
	for i in range(linhas):
		for j in range(colunas):
			if maior < vetor[i][j]:
				maior = vetor[i][j]
				posL = i
				posC = j
	print('Posição do Maior: (' + str(posL) + ',' + str(posC) + ')', 'Maior Valor:', maior)
	print()
	return None

def somaL(vetor, linhas, colunas):	#Função para encontrar a soma das linhas
	vetorSL = [0] * linhas
	for i in range(linhas):
		somaL = 0
		for j in range(colunas):
			somaL += vetor[i][j]
		vetorSL[i] = somaL
	for i in range(len(vetorSL)):
		print('Soma da Linha', i, '=', vetorSL[i])
	print()
	return None

def somaC(vetor, linhas, colunas):	#Função para encontrar a soma das colunas
	vetorSC = [0] * colunas
	for j in range(colunas):
		somaC = 0
		for i in range(linhas):
			somaC += vetor[i][j]
		vetorSC[j] = somaC
	for i in range(len(vetorSC)):
		print('Soma da Coluna', i, '=', vetorSC[i])
	print()		
	return None

#Programa Principal
dimensoes = input().split()

linha = int(dimensoes[0])
coluna = int(dimensoes[1])

matriz = criarMatriz(linha, coluna)

printar(matriz, linha, coluna)
maior(matriz, linha, coluna)
somaL(matriz, linha, coluna)
somaC(matriz, linha, coluna)