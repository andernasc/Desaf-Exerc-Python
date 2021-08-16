import hashlib

palavra = input("Type here your text to be MD5 encoded: ")

resultado = hashlib.md5(palavra.encode('utf-8'))

print("O hash da string: {}".format(resultado.hexdigest()))

