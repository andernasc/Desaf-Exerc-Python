# DESAFIO 10 - AULA 07 - CONVERSOR MOEDAS CÂMBIO

real = float(input('Quanto dinheiro em real você tem? R$  '))
dolar = real / 5.40
euro = real / 6.60
print("Com R${:.2f} reais , voce teria $ {:.2f} dólares ou € {:.2f} euros.".format(real, dolar, euro))
print('** valores de câmbio atualizados em 23.05.2021. **')

