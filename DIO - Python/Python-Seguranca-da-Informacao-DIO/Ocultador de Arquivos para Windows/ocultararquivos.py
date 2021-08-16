import ctypes

atributo_ocultar = 0x02

pasta = input("Digite o caminho da pasta a ser ocultada: EX: (C:/pasta/")

retorno = ctypes.windll.kernell32.SetFileAttributesW('ocultar')

if(retorno):
	print("O arquivo foi ocultado")
else:
	print("O arquivo nao foi ocultado")