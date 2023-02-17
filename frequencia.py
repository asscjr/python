# Programa que lê a entrada padrão contendo uma linha vários números de ponto flutuante. 
# O programa é capaz de dizer:
#	. qual o número que mais ocorreu;
#	. quantidade de vezes que ocorreu.

#Subprogramas
def ocorrencias(vetor):
	auxiliar = [0] * len(vetor)	#Vetor para contar a frequência de um número

	for i in range(len(vetor)):
		auxiliar[i] = 1
		for j in range(i + 1, len(vetor)):
				if vetor[j] == vetor[i]:
					auxiliar[i] += 1

	frequencia = 1	#Variável para saber a frenquência do número mais frequente
	qntOcorrencias = 0	#Variável para saber a posição do número mais frequente

	for i in range(1, len(auxiliar)):
		if auxiliar[i] > auxiliar[qntOcorrencias]:
			qntOcorrencias = i
			frequencia = auxiliar[i]
	return [vetor[qntOcorrencias], frequencia]

#Programa Principal
numeros = input().split()

if numeros != []:	#Caso existam
	repetidos = ocorrencias(numeros)

	print('Valor que mais ocorreu:', repetidos[0], 'que foi encontrado:', repetidos[1], 'vez(es)')

else:	#Caso não existam
	print('nenhum número foi lido!!!')