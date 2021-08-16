# DESAFIO 19 - AULA 08 - SORTEANDO ITEM LISTA ALUNOS

from random import choice
nom1 = str(input("Nome do primeiro aluno(a): "))
nom2 = str(input("Nome do segundo aluno(a): "))
nom3 = str(input("Nome do terceito aluno(a): "))
nom4 = str(input("Nome do quarto aluno(a): "))
lista = [nom1, nom2, nom3, nom4]
escolhido = choice(lista)
print("Sorteando..Sorteando..O Aluno(a) escolhido foi: {} ".format(escolhido))


