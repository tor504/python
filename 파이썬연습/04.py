# 사전에 요소 추가하기
# s1 = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
# s2 = ['Sun','Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']
# sdict ={}
# for i,k in enumerate(s1):
#     a = s2[i]
#     sdict[k] = a
# print(sdict)

# 사전의 특정요소값 변경하기
# names = {'Mary':10999,'Sam':2111,'Aimy':9778,'Tom':20245,'Mic':27115,'Bob':5887,'Kelly':7855}
# names['Sam'] = 10000
# print(names)

# 사전의 특정요소값 제거하기
# names = {'Mary':10999,'Sam':2111,'Aimy':9778,'Tom':20245,'Mic':27115,'Bob':5887,'Kelly':7855}
# del names['Mary']
# print(names)

# 사전의 모든요소 제거하기
# names = {'Mary':10999,'Sam':2111,'Aimy':9778,'Tom':20245,'Mic':27115,'Bob':5887,'Kelly':7855}
# names.clear()
# print(names)

# 사전의 key만 추출학기
# names = {'Mary':10999,'Sam':2111,'Aimy':9778,'Tom':20245,'Mic':27115,'Bob':5887,'Kelly':7855}
# k = names.keys()

# print(k)

# for i in k:
#     print('키:%s \t 밸류:%d'%(i,names[i]))

# 사전의 value만 추출학기
# names = {'Mary':10999,'Sam':2111,'Aimy':9778,'Tom':20245,'Mic':27115,'Bob':5887,'Kelly':7855}
# vals = names.values()

# print(vals)

# vals_list = list(vals)
# a = sum(vals_list)
# print("출생아수 총계:%d"%a)

# 사전의 모든요소  추출학기 -> items
# names = {'Mary':10999,'Sam':2111,'Aimy':9778,'Tom':20245,'Mic':27115,'Bob':5887,'Kelly':7855}
# items = names.items()

# print(items)

# for item in items:
#     print(item)

# 사전의 특정 키 존재 여부 확인하기 - >     in
# names = {'Mary':10999,'Sam':2111,'Aimy':9778,'Tom':20245,'Mic':27115,'Bob':5887,'Kelly':7855}
# k = input('이름을 입력하세요')
# if k in names:
#     print('이름이 <%s>인 출생아 수는 <%d>명입니다.'%(k,names[k]))
# else:
#     print('자료에 <%s>인 이름이 존재하지 않습니다.'%k)

# 사전의 특정 값 존재 여부 확인하기
# names = {'Mary':10999,'Sam':2111,'Aimy':9778,'Tom':20245,'Mic':27115,'Bob':5887,'Kelly':7855}

# if 9778 in names.values():
#     print('주어진 값이 사전에 존재')
# else:
#     print('주어진 값이 사전에 없음')

# 사전 정렬하기 -> sorted
names = {'Mary':10999,'Sam':2111,'Aimy':9778,'Tom':20245,'Mic':27115,'Bob':5887,'Kelly':7855}
a = sorted(names)
print(a)

def f1(x):
    return x[0]
def f2(x):
    return x[1]

b= sorted(names.items(),key = f1)
print(b)

c = sorted(names.items(),key = f2)

print(c)

d = sorted(names.items(),key=f2 ,reverse=True)
print(d)
