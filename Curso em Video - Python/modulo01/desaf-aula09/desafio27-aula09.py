# DESAFIO 27 - AULA 09
#Faça um programa que leia o nome completo de uma pessoa, mostrando
# em seguida o primeiro e o último nome separadamente.

n = str(input('Digite seu nome completo: '))
nome = n.split()
print('Olá, muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))