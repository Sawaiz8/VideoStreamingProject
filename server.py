import cv2 as cv
from socket import *
import pickle
import struct
import threading

HEADER = 64 #CAN CHNAGE DEPENDING ON APPLICATION
HEADER_FORMAT = "utf-8"
DISCONNECT_MESSAGE = "DISCOUNTED"
SERVER_PORT = 12001
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',SERVER_PORT))
serverSocket.listen(10)
print('The server is ready to receive')

def start_server():

    try:
        connected = True
        while connected:
            connectionSocket, addr = serverSocket.accept()
            thread = threading.Thread(target=deal_client_request, args = (connectionSocket,addr))
            thread.start()
            print(f"ACTIVE CONNECTIONS {threading.activeCount() - 1}")
            print(connectionSocket.getpeername())
    except Exception as exp:
        print("Error:", exp)
    finally:
        print("connection ended")
    

def deal_client_request(connectionSocket, addr):
    connected = True
    try:
        while connected:
            msgLength = connectionSocket.recv(HEADER).decode(HEADER_FORMAT)
            print(msgLength)
            if msgLength.isspace():
                continue
            frame = connectionSocket.recv(4096)
            print(len(frame), msgLength)
            while len(frame) <= int(msgLength):
                frame += connectionSocket.recv(4096)
            frame = pickle.loads(frame)

            #if msg == DISCONNECT_MESSAGE:
                #connected = False
                
            
            cv.imshow('Frame', frame)
            if cv.waitKey(1) & 0xFF == ord("q"):
                connected = False
    finally:
        connectionSocket.close()

start_server()
connectionSocket.close()



#sizeOfLength = struct.calcsize(">L")
#data = msg[sizeOfLength:]
#msglen = struct.unpack(">L", msg[:sizeOfLength])[0]
#print(msglen)
#while len(data) < msglen:
#    new = connectionSocket.recv(4096)
#    data = data + new
#print("first:", len(data))
#print()
#data = pickle.loads(data)
#start_server()


