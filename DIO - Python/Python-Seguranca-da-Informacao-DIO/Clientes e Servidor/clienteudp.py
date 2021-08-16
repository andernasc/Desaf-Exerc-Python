import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket client created successfully!")

host = 'localhost'
port = 5433
message = "Hello, server."

try:
	print("Client: {}".format(message))
	s.sendto(message.encode(), (host,5432))

	data, server = s.recvfrom(4096)
	data = data.decode()
	print("Sent to server: {}".format(data))
finally:
	print("Client: Closing the connection")
	s.close()