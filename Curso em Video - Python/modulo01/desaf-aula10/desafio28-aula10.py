# DESAFIO 28 - AULA 10 - JOGO ADIVINHAÇÃO

from random import randint
from time import sleep
computador = randint(0, 10) # faz o codigo sortear de 0 a 10
print('-==-' * 16)
print('Vou pensar em um número aleatório, de 0 a 10 tente adivinhar....')
print('-==-' * 16)
print('Aguarde, estou processando....')
sleep(6)
jogador = int(input('Pronto.. qual número eu sortiei?: '))
if jogador == computador:
    print('Parabéns, o número é {} você conseguio adivinhar!'.format(computador))
else:
    print('Eu ganhei e você errou, HAHAHA! o número foi {} e não o seu número {}'.format(computador, jogador))



