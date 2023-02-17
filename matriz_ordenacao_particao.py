# Programa para reforçar os conceitos do algoritmo de ordenação particionada

#Subprogramas
def criarMatriz(linhas, colunas):	#Função para criar matriz
	from random import randint
	matriz = [None] * linhas
	for i in range(linhas):
		matriz[i] = [0] * colunas
		for j in range(colunas):
			matriz[i][j] = randint(10, 99)
	return matriz

def printar(vetor, linhas, colunas):	#Função para imprimir a matriz
	for i in range(linhas):
		for j in range(colunas):
			print(vetor[i][j], end = ' ')
		print()
	print()
	return None

def somaL(vetor, linhas, colunas):	#Função para encontrar a soma das linhas
	vetorSL = [0] * linhas
	for i in range(linhas):
		somaL = 0
		for j in range(colunas):
			somaL += vetor[i][j]
		vetorSL[i] = somaL
	return vetorSL

def arruma(matriz, i, j):	#Função que organiza as linhas de forma crescente a soma das linhas
	temp = matriz[i]
	matriz[i] = matriz[j]
	matriz[j] = temp
	return None

def particionando(matriz, inicio, fim, indice):
	meio = indice[inicio]
	i = inicio + 1
	j = fim

	while i < j:
		while i < fim and indice[i] < meio:
			i += 1
		while j > inicio and indice[j] >= meio:
			j -= 1
		if i < j:
			arruma(indice, i, j)
			arruma(matriz, i, j)

	if meio > indice[j]:
		arruma(indice, inicio, j)
		arruma(matriz, inicio, j)
	return j
	
def particao(matriz, inicio, fim, indice):	#Função recursiva que separa a matriz
	if inicio < fim:
		meio = particionando(matriz, inicio, fim, indice)

		particao(matriz, inicio, meio - 1, indice)
		particao(matriz, meio + 1, fim, indice)
	return None

def ordena(matriz, indice):	#Função para ordenar a matriz
	particao(matriz, 0, len(matriz) - 1, indice)
	return None

#Programa Principal
dimensoes = input().split()

linha = int(dimensoes[0])
coluna = int(dimensoes[1])

matriz = criarMatriz(linha, coluna)

printar(matriz, linha, coluna)
ordena(matriz, somaL(matriz, linha, coluna))
printar(matriz, linha, coluna)