# 파일 수신 프로그램 만들기
import socket

HOST = 'localhost'
PORT = 9009

def getFileFromServer(filename):
    data_transferred = 0

    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
        sock.connect((HOST,PORT))
        sock.sendall(filename.encode())

        data = sock.recv(1024)
        if not data:
            print('파일[%s]: 서버에 존재 하지 않거나 전송중 오류발생'%filename)
            return
        
        with open('download/'+filename,'wb') as f:
            try:
                f.write(data)
                data_transferred += len(data)
                data = sock.recv(1024)

            except Exception as e:
                print(e)

    print('파일 [%s]전송종료, 전송량[%d]'%(filename,data_transferred))

filename = input('다운로드 받을 파일이름을 입력하세요')
getFileFromServer(filename)
