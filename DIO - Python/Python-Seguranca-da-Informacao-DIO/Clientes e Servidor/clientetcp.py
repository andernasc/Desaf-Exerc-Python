import socket 
import sys

def main():
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) #Tipo de conexao a ser realizada
	except socket.error as e:
		print("Connection failured!")
		print("Error: {}".format(e))
		sys.exit()

	print("Socket client created successfully!")

	targetHost = input("Type the host/ip to be connected: ")
	targetPort = input("Type the port to be connected: ")

	try:
		s.connect((targetHost, int(targetPort)))
		print("TCP client successfully connected on\nHost: {}\nPort: {}".format(targetHost,targetPort))
		s.shutdown(2)
	except socket.error as e:
		print("Failured to connect to the TCP client")
		print("Error: {}".format(e))
		sys.exit()

if __name__ == "__main__":
	main()