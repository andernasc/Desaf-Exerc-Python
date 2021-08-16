# DESAFIO 21 - AULA 08 - TOCANDO MP3
# adicionar os mp3 teste no diretorio do script
# importar/instalar biblioteca PYGAME
# importar/instalar biblioteca PLAYSOND
# será reproduzido um após o outro.

# METODO USANDO PYGAME

import pygame
pygame.init()
pygame.mixer.music.load('diabloIIrogerandme.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass

# USANDO PLAYSOUND

from playsound import playsound
playsound('halflife01.mp3')




