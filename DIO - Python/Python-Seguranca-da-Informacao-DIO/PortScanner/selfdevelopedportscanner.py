import os

host = '' # INSERT YOUR HOST HERE
port = '' # INSERT YOUR PORT HERE

os.system('ping -n 4 {} 80'.format(host))