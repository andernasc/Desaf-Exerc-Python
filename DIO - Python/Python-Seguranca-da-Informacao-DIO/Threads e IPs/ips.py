from threading import Thread
import ipaddress

ip = '192.68.0.100/24'

endereco = ipaddress.ip_address(ip)

rede = ipaddress.ip_network(ip, strict=False)

for ip in rede:
	print(ip)

print("Endereco: {}".format(endereco))

print("Rede: {}".format(rede))