# 리스트에서 특정요소 구하기
# ll = [2,2,1,3,8,5,6,7,3,6,2,3,9,4,4]
# l1 = ll.count(2) #값이 2인 요소
# l2 = ll.count(7) #값이 7인 요소 
# print(l1)  
# print(l2)

#리스트 제거하기
# ll = [2,2,1,3,8,5,6,7,3,6,2,3,9,4,4]
# del ll
# print(ll)

# 리스트 요소 정렬(sort)
name = ['Mary','Sams','Aimy','Tom']
name.sort()
print(name)

# 리스트 요소 정렬(sorted)
name1 = ['Mary','Sams','Aimy','Tom']
a = sorted(name1)
b = sorted(name1,reverse=True)
print(name1)
print(a)
print(b)

# 리스트 무작위 섞기
from random import shuffle

l1 = list(range(1,11))
for i in range(3):
    shuffle(l1)
    print(l1)