import os
import time

with open("host.txt", "r") as file:
	dump = file.read()
	dump = dump.splitlines()

	for ip in dump:
		print("Verificando o ip: {}".format(ip))
		os.system("ping -n 4 {}".format(ip_ou_host))
		