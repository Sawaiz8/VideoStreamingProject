import cv2 as cv
from socket import *
import pickle
import struct
import imutils

HEADER = 8
HEADER_FORMAT = "unicode_escape"
SERVER_NAME = 'localhost'	# 'servername'
SERVER_PORT = 12004

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((SERVER_NAME, SERVER_PORT))
print("Starting video capture") 
cap = cv.VideoCapture(0)
if not cap.isOpened():
        print("Cannot open camera")

def start_client():
        connected = True
        while connected:
                ret, frame = cap.read()
           
                if not ret:
                        print("Cannot recieve gram (stream end?) Exiting")
                        break
                frame = imutils.resize(frame, width=320)
                cv.imshow("Frame", frame)
                
                frame = pickle.dumps(frame, 0)
                msg_len = len(frame)
                msg_len_stream = struct.pack("Q", msg_len)
		
                clientSocket.sendall(msg_len_stream+frame)

                if cv.waitKey(1) == ord("q"):
                        break           

        cap.release()
        cv.destroyAllWindows()




def send_client_message(frame, clientSocket): 
        pass

start_client()
