from socket import *
serverName = 'localhost'	# 'servername'
serverPort = 12001
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print(clientSocket.getsockname())
while 1:
    sentence = input('Input number: ')
    clientSocket.send(sentence.encode())
    Sum = clientSocket.recv(1024)
    print('From Server sum: ', Sum.decode())

clientSocket.close()
