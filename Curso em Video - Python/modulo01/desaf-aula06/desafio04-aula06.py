# DESAFIO 04-AULA06- ler algo do teclado e mostre seu tipo primitivo.
###############################################################

x = input('Digite qualquer coisa: ')
print(f'Você escreveu: {x}')
print('Você escreveu o tipo: ', type(x))
print('Ele é alfanúmerico? ', x.isalnum())
print('Ele é númerico? ', x.isnumeric())
print('Ele é alfabético? ', x.isalpha())
print('Ele está em letras minúsculas? ', x.islower())
print('Ele está em letras maiúsculas? ', x.isupper())
print('Ele é imprimível? ', x.isprintable())
print('Ele é um espaço? ', x.isspace())
print('Ele é um dígito? ', x.isdigit())
print('Fim!')
