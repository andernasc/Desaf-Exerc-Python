# DESAFIO 13 - AULA 07 - REAJUSTE SALARIAL de + 15 %

salario = float(input('Digite o valor do Salário: R$ '))
reaj = salario + (salario * 15 / 100)
input("O salário que era de R$ {:.2f} , com reajuste de +15% é de R$ {:.2f}".format(salario, reaj))

