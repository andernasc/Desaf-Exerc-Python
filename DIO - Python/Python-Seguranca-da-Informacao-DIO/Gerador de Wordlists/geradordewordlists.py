import itertools

resultado = itertools.permutations('abc', 3)

for char in resultado:
	print(''.join(char))