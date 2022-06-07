import platform, os

def limpaTela():
	#Função para limpar tela
	if platform.system() == "Windows":
		os.system("cls")
	else:
		os.system("clear")

def escreve(texto):
	#Função para escrever um texto formatado
	separador = f'{"":-<16}'
	print(separador)
	cont = 0
	for linha in texto:
		cont+=1
		print(f'{cont: >3} | {linha}')
	print(separador)

def filtraQuebraDeLinha(linha):
	#Função para remover quebras de linha
	return linha.replace("\n", "")

def filtraEspacos(linha):
	#Função para remover espaços
	return linha.replace(" ", "")

def filtra(texto):
	#Função para filtrar um texto
	textoFiltrado = []
	for linha in texto:
		linha = filtraQuebraDeLinha(linha)
		linha = filtraEspacos(linha)
		if linha != "":
			textoFiltrado.append(linha)
	return textoFiltrado
