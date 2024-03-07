# url 호스트 도메인 추출
# url = 'http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid=105&oid=028&aid=002334601'

# a = url.split('/')
# do = a[4]
# print(do)

# url 쿼리 문자열 추출
url = 'http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid=105&oid=028&aid=002334601'

a = url.split('?')
qu = a[1].split('&')
for q in qu:
    print(q)