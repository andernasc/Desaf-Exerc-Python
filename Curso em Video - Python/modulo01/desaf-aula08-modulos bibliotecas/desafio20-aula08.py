# DESAFIO 20 - AULA 08 - SORTEANDO ORDEM APRESENTACAO ALUNOS LISTA

from random import shuffle
nom1 = str(input("Nome do primeiro aluno(a): "))
nom2 = str(input("Nome do segundo aluno(a): "))
nom3 = str(input("Nome do terceiro aluno(a): "))
nom4 = str(input("Nome do quarto aluno(a): "))
lista = [nom1, nom2, nom3, nom4]
shuffle(lista)
print("A ordem de apresentação será:")
print(lista)

