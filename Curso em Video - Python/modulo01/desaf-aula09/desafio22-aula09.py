# DESAFIO 22 - AULA 09 - ANALISADOR DE TEXTOS
# Conta letras, minusculas e maiusculas

nome = str(input('Digite palavras: ' ))
separa = nome.split()

print('Analisando nome....')
print('O texto possui {} letras ao todo'.format(len(nome)))
print('Seu primeiro nome é {} e possui {} letras'.format(separa[0], len(separa[0])))
print('Em forma minúscula fica: {}.'.format(nome.lower()))
print('Em forma maiúscula fica: {}.'.format(nome.upper()))

####################################################################

#print('Seu primeiro nome possui {} letras'.format(nome.find(' ')))
#print('Seu nome possui ao todo {} letras'.format(len(nome) - nome.count(' ')))


