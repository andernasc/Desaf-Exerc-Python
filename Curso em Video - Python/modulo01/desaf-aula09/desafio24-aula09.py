# DESAFIO 24 - AULA 09 - VERIFICANDO PRIMEIRAS LETRAS
#programa que leia o nome de uma cidade diga
# se ela começa ou não com o nome “SANTO”

cid = str(input('Em que cidade você nasceu?: '))
print(cid[:5].upper() == 'SANTO')


