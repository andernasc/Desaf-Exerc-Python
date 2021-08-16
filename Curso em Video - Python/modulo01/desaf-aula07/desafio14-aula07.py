# DESAFIO 14 - AULA 07 - CONVERSOR DE TEMPERATURAS

c = float(input("Informe a temperatura em Celsius: "))
f = 9 * c / 5 + 32     #nao precisa de parenteses, segue ordem precedencia * / +#
k = c + float(273.15)
print("A temperatura de {}Cº, corresponde a {}ºF ou {}ºK ".format(c, f, k))
