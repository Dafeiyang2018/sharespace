import socket
import cv2
import numpy

address = ("223.3.203.38", 8888)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address)
print('listen')
s.listen(True)
print('start')

def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

conn, addr = s.accept()
print('accept')
while 1:
    data = recvall(conn,16)
    if data is None:
        print('None')
    else:
        print(data)
    print('recvall')

    if cv2.waitKey(10) == 27:
        break
    
s.close()