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
	
	return gramatica

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
	gramatica = fazConversao(gramatica)
	print("\nAutômato de Pilha:")
	escreve(gramatica)
	
	input("Pressione ENTER para continuar . . .")
