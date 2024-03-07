import urllib.request

def get_external_ip():
    try:
        # 외부 서비스에 GET 요청 보내기
        external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
        return external_ip
    except Exception as e:
        print("Error occurred while retrieving external IP:", e)
        return None
external_ip = get_external_ip()
if external_ip:
    print("외부 IP:", external_ip)