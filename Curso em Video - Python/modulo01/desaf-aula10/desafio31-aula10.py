# DESAFIO 31 - CUSTO VIAJEM
#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens
# de até 200Km e R$0,45 para viagens mais longas.

dist = float(input('Quantos Km tem sua viajem total?: '))
print('Você quer começar uma viajem de {}Km?'.format(dist))
if dist <= 200:
    preco = dist * 0.50
else:
    preco = dist * 0.45
print('O preço da sua passagem será de R${:.2f}'.format(preco))


# EXECUÇÃO TERNARIA IF e ELSE (unica linha)
# dist = float(input('Quantos Km tem sua viajem total?: '))
# print('Você quer começar uma viajem de {}Km?'.format(dist))
# preco = dist * 0.50 if dist <= 200 else dist * 0.45
# print('O preço da sua passagem será de R${:.2f}'.format(preco))