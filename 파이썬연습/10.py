# 주어진 숫자를 천단위 구분 
# isdigit -> 사용자가 입력한 문자열이 숫자로만 구성 되어있는지 확인

# n = input('아무 숫자를 입력하세요')

# if n.isdigit():
#     n = n[::-1]
#     a = ''
#     for i,c in enumerate(n):
#         i += 1
#         if i != len(n) and i%3 == 0 :
#             a += (c + ',')
#         else:
#             a += c

#     a = a[::-1]
#     print(a)
# else:
#     print('입력한 내용[%s]: 숫자가 아닙니다.'%n)

# 문자열의 각 문자를 그 다음 문자로 변경
t = input('문장을 입력하세요')

a = ''
for i in range(len(t)):
    if i != len(t)-1:
        a += t[i+1]
    else:
        a += t[0]

print(a)