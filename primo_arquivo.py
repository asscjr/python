# Programa que encontra os números primos em arquivo txt

#Subprograma
def primo(inteiro):
	if inteiro > 1:
		for i in range(2, inteiro):
			if inteiro % i == 0:
				return False
		return True

#Programa Principal
inteiros = input()
primos = input()

saida = open(primos, 'w')
entrada = open(inteiros, 'r')

linha = entrada.readline()

novaL = ''

while linha != '':
	numeros = linha.split()

	for n in numeros:
		convertido = int(n)
		if primo(convertido):
			novaL += str(convertido) + ' '

	saida.write(novaL + '\n')
	novaL = ''
	linha = entrada.readline()

entrada.close()
saida.close()