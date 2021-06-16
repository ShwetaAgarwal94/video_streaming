import socket
import urllib
import json
import pickle
import numpy as np
import cv2

url = 'http://192.168.43.1:8080/shot.jpg'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "192.168.43.224"
port = 2323

s.connect((ip, port))

while True:
    x = s.recv(1000000)
    print("received")
    
    imgResp = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgResp.read()))
    img = cv2.imdecode(imgNp, -1)
    img = cv2.resize(img,(600,500))
    ret, buffer = cv2.imencode('.jpg', img)
    bytedata = pickle.dumps(buffer)
    
    s.send(bytedata)
    try:
        data = pickle.loads(x)
        data = cv2.imdecode(data, cv2.IMREAD_COLOR)
        if data is not None:
            cv2.imshow('photo', data)
            if cv2.waitKey(10) == 13:
                break
    except:
        print("waiting for the server!")

cv2.destroyAllWindows()
