# Programa que lê strings da entrada padrão até que a string vazia (“”) seja digitada.
# O programa é capaz de dizer:
#	. a quantidade de strings não vazias lidas;
#	. a média dos valores, das strings numéricas lidas;
#	. o valor do maior número lido.

#Programa Principal
numero = input()

qnt = 0
soma = 0.0
maiorV = 0.0

while numero != '':

	pontoF = float(numero)	#Conversão para ponto flutuante

	soma += pontoF	#Variável para somar os numeradores da média

	qnt += 1	#Quantidade de números / Denominador para média 

	if pontoF > maiorV:	#Condicional para encontrar o maior valor
		maiorV = pontoF

	numero = input()

print('Quantidade de Números:', qnt)

if qnt != 0:	#Caso existam
	media = soma/qnt

	print('Média dos Números: %1.2f'%media)
	print('Maior:', maiorV)