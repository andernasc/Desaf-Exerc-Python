import random, string

size = 72

chars = string.ascii_letters + string.digits + '!@#$%&*()-=+}{;:?/\\'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(size)))