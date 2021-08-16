# DESAFIO 15 - AULA 07 - VALOR DO ALUGUEL DE CARROS TOTAL
# ( R$ 50 o dia, 0.10 cents km rodado)

dias = int(input("Quantos dias você utilizou o carro?:  "))
km = float(input("Quantos quilômetros foram rodados?:  "))
pago = (dias * 50) + (km * 0.10)
print("Você utilizou o carro por {} dias e rodou {}km , então o total a pagar é de R${:.2f}".format(dias, km, pago))

