# 리스트의 모든 요소를 인덱스와 쌍으로 (enumerate)
s = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
a = list(enumerate(s))
print(a)

for i, body in enumerate(s):
    print('태양계의 %d번째 천체:%s'%(i,body))

#enumerate -> 인덱스와 리스트의 원소로 이뤄진 튜플이 출력

# 리스트의 모든 요소 합 구하기
ll = [2,3,4,7,8,3,8,9,2]
a = sum(ll)
print(a)

# 리스트 요소 모두 참 -> all
# 리스트 요소 모두 거짓 -> any
l1 = [0,1,2,3,4]
l2 = [True,True,True]
l3 = ['',[],(),(),None,False]
print(all(l1))
print(any(l1))
print(all(l2))
print(any(l2))
print(all(l3))
print(any(l3))
