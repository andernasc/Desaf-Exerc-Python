# DESAFIO 25 - AULA 09 -
# Crie um programa que leia o nome de uma pessoa
# e diga se ela tem “SILVA” no nome.

nome = str(input('Qual é seu nome completo?: ')).strip()
print('Este nome tem Silva? : {}'.format('silva' in nome.lower()))



