# DESAFIO 18 - AULA 08 - SENO , COSSENO E TANGENTE.

# utilizando biblioteca

from math import radians, sin, cos ,tan
angulo = float(input("Digite o ângulo que você deseja: "))
sen = sin(radians(angulo))
print("O ângulo de {}º tem o SENO de {:.2f}".format(angulo, sen))
coss = cos(radians(angulo))
print("O ângulo de {}º tem o COSSENO de {:.2f}".format(angulo, coss))
tan = tan(radians(angulo))
print("O ângulo de {}º tem a TANGENTE de {:.2f}".format(angulo, tan))






