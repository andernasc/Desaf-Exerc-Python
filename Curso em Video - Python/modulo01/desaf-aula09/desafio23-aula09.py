# DESAFIO 23 - AULA 09 - SEPARANDO DIGITOS DE NUMERO
# unidade, dezena. centena,milhar


num = int(input('Informe numeros : '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))



