#  문자 코드(ord)
# a = input("문자 1개를 입력하세요")
# if len(a) != 0:
#     a = a[0]
#     av = ord(a)
#     print("문자: %s \t 코드값:%d[%s]"%(a,av,hex(av)))

#  코드 값에 대응하는 문자 (chr) -> ord의 반대기능
# a = input("문자 코드값를 입력하세요")
# a = int(a)
# try:
#     b = chr(a)
#     print("코드값:%d[%s],문자:%s"%(a,hex(a),b))
# except ValueError:
#     print("입력한 <%d>에 대한 문자가 존재하지 않습니다!"%a)


# 문자열로 된 식 실행 (eval)
# a = '2+3'
# b = 'round(3.7)'
# c = eval(a)
# d = eval(b)

# print('<%s>를 eval()로 실행한 결과: '%a,end='');print(c)
# print('<%s>를 eval()로 실행한 결과: '%b,end='');print(d)


# 이름없는 한줄짜리 함수 (lambda)
# add = lambda x,y:x + y # lambda 인자,인자 ... : 실행코드
# a = add(1,3)
# print(a)

# func = [lambda x:x+'.pptx',lambda x:x+'.docx']
# a1 = func[0]('intro')
# a2 = func[1]('report')

# print(a1)
# print(a2)

# names = {'Mary':10999,'Sams':2111,'Aimy':9778,'Tom':20245,'Mic':27115,'Bob':5887,'Kelly':7855}
# b = sorted(names.items(),key=lambda x : x[0])
# print(b)


# 인자 바꿔 함수 반복 호출 결과값 (map)
a = lambda x : x * x 
args = [1,2,3,4,5]
b = map(a,args)
print(list(b))

c = lambda x,y : x * x + y
X = [1,2,3,4,5]
Y = [10,9,8,7,6]
d = map(c,X,Y) 
print(list(d))