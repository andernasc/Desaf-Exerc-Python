# DESAFIO 17 - AULA 08 - CATETOS E HIPOTENUSA


# usando modulos matematico (rapido) / import math

from math import hypot
co = float(input("Comprimento do Cateto oposto: "))
ca = float(input("Comprimento do Cateto adjacente: "))
hi = hypot(co, ca)
print("A hipotenusa vai medir {:.2f}".format(hi))


##############################################################

#modo tradicional matemática
co = float(input("Comprimento do Cateto oposto: "))
ca = float(input("Comprimento do Cateto adjacente: "))
hi = (co ** 2 + ca ** 2) ** (1/2)
print("A hipotenusa vai medir {:.2f}".format(hi))

