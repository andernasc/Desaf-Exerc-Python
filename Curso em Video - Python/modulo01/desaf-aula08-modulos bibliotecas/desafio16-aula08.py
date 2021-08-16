# DESAFIO 16 - AULA 08 - QUEBRANDO NUMERO REAL PARA INTEIRO,
# USANDO MODULO MATH

from math import trunc
num = float(input("Digite um número fracionado: "))
print("O valor {} em sua porçao inteira fica {}".format(num, trunc(num)))


# USANDO NESTE CASO JEITO PADRÃO.

num = float(input("Digite um número fracionado: "))
print("O valor {} em sua porção inteira fica {}".format(num, int(num)))


