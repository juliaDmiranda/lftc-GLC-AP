import sys
from funcoesAuxiliares import limpaTela, filtra, escreve

def leGramatica(nomeArquivo):
	if not ".txt" in nomeArquivo[-4::]:
		nomeArquivo += ".txt"
	arquivo	 = open(nomeArquivo, 'r')
	gramatica = arquivo.readlines()
	arquivo.close()
	#Filtra "\n"s e espacos
	return filtra(gramatica)

def fazConversao(gramatica):
	#Lista de simbolos
	simbolos = []

	#Linhas do automato
	automato = []

	#Criar transições equivalentes e capturar simbolos terminais
	for linha in gramatica:
		#Monta transicao e adiciona ao automato
		transicao = f'(q,@,{linha[0]})=(q,{linha[3::]})'
		automato.append(transicao)
		#Captura simbolos e guarda
		for caracter in linha[3::]:
			if caracter.islower() and not caracter in simbolos:
				simbolos.append(caracter)

	#Ordena simbolos em ordem alfabetica
	simbolos = sorted(simbolos)

	#Criar transições finais a partir de simbolos capturados
	for simbolo in simbolos:
		#Monta transicao e adiciona ao automato
		transicao = f'(q,{simbolo},{simbolo})=(q,@)'
		automato.append(transicao)
	return automato

#Captura argumentos passados
argumentos    = sys.argv
#Remove primeiro argumento(converte.py)
listaArquivos = argumentos[1::]

for nomeArquivo in listaArquivos:

	limpaTela()

	#Lê gramatica a partir de um arquivo
	gramatica  = leGramatica(nomeArquivo)
	print("\nGramática Livre de Contexto:")
	escreve(gramatica)
	
	#Converte a gramática livre de contexto em autômato de pilha
	automato = fazConversao(gramatica)
	print("\nAutômato de Pilha:")
	escreve(automato)
	
	input("Pressione ENTER para continuar . . .")
