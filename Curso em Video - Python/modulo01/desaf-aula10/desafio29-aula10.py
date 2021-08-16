num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
divisao = (num1 / num2)
resto = (num1 % num2)

if resto == 0 :
    print('A Divisão é {}'.format(divisao))
else:
    print('Divisão impossivel.')

