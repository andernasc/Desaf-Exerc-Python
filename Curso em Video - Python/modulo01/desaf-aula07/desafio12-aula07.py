# DESAFIO 12 - AULA 07 - CALCULANDO DESCONTOS PORCENTAGEM 10%

preco = float(input("Qual é o preço do produto? R$ "))
desc = preco - (preco * 10 / 100)
input("O produto que custava R$ {:.2f} , com o desconto de 10%, custará R$ {:.2f}".format(preco, desc))
