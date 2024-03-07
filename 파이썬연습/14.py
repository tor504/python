# url에 접속 html 페이지 화면 출력
# from urllib.request import urlopen

# url ='https://www.naver.com'
# with urlopen(url) as f:
#     a = f.read().decode()
#     print(a)


# url에 접속 html 페이지 파일로 저장
# from urllib.request import urlopen

# url ='https://www.naver.com'
# with urlopen(url) as f:
#     a = f.read().decode()
#     with open('naverhome.html','w',encoding='utf-8') as h:
#         h.writelines(a)

# 인터넷 이미지 내피씨 저장
# from urllib.request import urlopen
# import ssl

# ssl._create_default_https_context = ssl._create_stdlib_context

# a = 'https://ygfamily.com/contents/images/2024/01/yooInna-main-image_1.jpg'
# b = a.split('/')[-1]
# try:
#     with urlopen(a) as f:
#         with open(b,'wb') as h:
#             img = f.read()
#             h.write(img)
# except Exception as e:
#     print(e) 


# from urllib.request import urlopen
# BUFSIZE = 256 * 1024
# a = 'https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe'
# b = a.split('/')[-1]
# try:
#     with urlopen(a) as f:
#         with open(b,'wb') as h:
#             buf = f.read(BUFSIZE)
#             while buf:
#                 h.write(buf)
#                 buf = f.read(BUFSIZE)
# except Exception as e:
#     print(e) 