from socket import *
serverPort = 12001
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
connectionSocket, addr = serverSocket.accept()
print(connectionSocket.getpeername())
while 1:
	number = connectionSocket.recv(1024)
	number = number.decode()
	number = int(number)
	print(number)
	total = total + number
	sendTotal = str(total)
	connectionSocket.send(sendTotal.encode())
connectionSocket.close()
