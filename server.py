import cv2 as cv
from socket import *
import pickle
import struct
import threading
import numpy
from random import randint


HEADER = 4 #CAN CHNAGE DEPENDING ON APPLICATION
HEADER_FORMAT = "unicode_escape"
SERVER_PORT = 12006
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',SERVER_PORT))
serverSocket.listen(10)
print('The server is ready to receive')


WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
 

def start_server():

    try:
        connected = True
        while connected:
            connectionSocket, addr = serverSocket.accept()
            thread = threading.Thread(target=deal_client_request, args = (connectionSocket,addr))
            thread.start()
            print(f"ACTIVE CONNECTIONS {threading.activeCount() - 1}")
            print(connectionSocket.getpeername())
            clientNo = threading.activeCount() - 1            
    except Exception as exp:
        print("Error while starting:", exp)
    finally:
        print("connection ended")
    

def deal_client_request(connectionSocket, addr):
    clientNo = randint(1,100000)
    writer = cv.VideoWriter('recording/server_video.mp4v', cv.VideoWriter_fourcc(*'DIVX'), 30, (WINDOW_WIDTH, WINDOW_HEIGHT))
    connected = True
    payload_size = struct.calcsize("Q")
    try:
        data = b''
        while connected:
            while len(data) < payload_size:
                packet = connectionSocket.recv(1024)
                if not packet:
                    break
                data += packet
            size = data[:payload_size]
            data = data[payload_size:]
            size = struct.unpack("Q",size)[0]
            while len(data) < size:
                data += connectionSocket.recv(1024)
            frame_data = data[:size]
            frame_data = pickle.loads(frame_data)
            data = data[size:]
            writer.write(frame_data)
            cv.imshow('client',frame_data)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
    except Exception as exp:
        print("Error in thread", exp)
    finally:
        connectionSocket.close()
        writer.release()
        cv.destroyAllWindows()

start_server()

