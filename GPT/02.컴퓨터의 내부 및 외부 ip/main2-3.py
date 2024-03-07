import socket
import requests

def get_internal_ip():
    try:
        # 호스트 이름 가져오기
        hostname = socket.gethostname()
        # 호스트 이름에 대한 IP 주소 가져오기
        ip = socket.gethostbyname(hostname)
        return ip
    except Exception as e:
        print("Error occurred while retrieving internal IP:", e)
        return None

def get_external_ip():
    try:
        # 외부 서비스에 GET 요청 보내기
        response = requests.get('https://api.ipify.org')
        # 응답에서 IP 주소 추출
        ip = response.text
        return ip
    except Exception as e:
        print("Error occurred while retrieving external IP:", e)
        return None

internal_ip = get_internal_ip()
external_ip = get_external_ip()

if internal_ip:
    print("내부 IP:", internal_ip)

if external_ip:
    print("외부 IP:", external_ip)