# 에코 클라이언트 만들기
import socket

HOST = 'localhost'
PORT = 9009

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as h:
    h.connect((HOST,PORT))
    msg = input("메세지 입력")
    h.sendall(msg.encode())
    data = h.recv(1024)

print("에코 서버로부터 받은 데이터[%s]"%data.decode())
