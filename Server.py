import socket
import json
import pickle
import cv2

cap = cv2.VideoCapture(0)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "192.168.43.224"
port = 2323

s.bind((ip,port))
print("Binded")
s.listen()

o, addr = s.accept()
print("connected to {}".format(addr))
while True:
    r, ph = cap.read()
    r, buffer = cv2.imencode('.jpg', ph)
    bytedata = pickle.dumps(buffer)
    o.send(bytedata)
    
    
    x = o.recv(1000000)
    
    try: 
        data = pickle.loads(x)
        data = cv2.imdecode(data, cv2.IMREAD_COLOR)
        if data is not None:
            cv2.imshow('server',data)
            if cv2.waitKey(10) == 13:
                break
    except:
        print("waiting for the client!")
cv2.destroyAllWindows()
