import cv2 as cv
from socket import *
import pickle
import struct

HEADER_SIZE = 64
HEADER_FORMAT = "utf-8"
SERVER_NAME = 'localhost'	# 'servername'
SERVER_PORT = 12001
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((SERVER_NAME, SERVER_PORT))


def start_client():
        connected = True
        while connected:
                print("Starting video capture") 
                cap = cv.VideoCapture(0)
                if not cap.isOpened():
                        print("Cannot open camera")

                ret, frame = cap.read()
                if not ret:
                        print("Cannot recieve gram (stream end?) Exiting")
                        break

                #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                gray = frame

                frame = pickle.dumps(frame)
                msg_len = str(len(frame)).encode(HEADER_FORMAT)
                msg_len += b' ' * (HEADER_SIZE -len(msg_len))
                clientSocket.send(msg_len)
                clientSocket.send(frame)

                if cv.waitKey(1) == ord("q"):
                        break           

        cap.release()
        cv.destroyAllWindows()




def send_client_message(frame, clientSocket): 
        pass

start_client()
