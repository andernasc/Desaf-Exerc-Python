import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Successfully created socket client")

host = 'localhost'
port = 5433

s.bind((host, port))
message = '\nServer: Hello, client.'

while(True):
	data, address = s.recvfrom(4096)

	if(data):
		print("Server sending message...")
		s.sendto(data + (message.encode()), end)
