# def getTextFreq(filename):
#     with open(filename,'r') as f:
#         t = f.read()
#         fa = {}
#         for c in t:
#             if c in fa:
#                 fa[c] += 1
#             else:
#                 fa[c] = 1
#     return fa 

# a = getTextFreq('mydata.txt')
# a = sorted(a.items(),key=lambda x:x[1],reverse=True)
# for c,freq in a:
#     if c == '\n':
#         continue
#     print('[%c]->[%d]회 나타 남'%(c,freq))


# 텍스트 파일에 있는 단어 개수 계산
# with open('mydata.txt','r') as f:
#     a = f.read()
#     b = a.split()
#     print('단어수:[%d]'%len(b))

# 파일에서 특정단어 개수 계산
# def countWord(filename,word):
#     with open(filename,'r') as f:
#         t = f.read()
#         t = t.lower()
#         p = t.find(word)
#         count = 0
#         while p != -1:
#             count += 1
#             p = t.find(word,p+1)
#         return count
    
# word = input('mydata.txt에서 개수를 구할 단어를 입력하세요')
# word = word.lower()
# a = countWord('mydata.txt',word)
# print('[%s]의 개수 :%d'%(word,a))

# 파일에서 특정 문자열 교체
a1 = input('찾을 단어를 입력하세요')
a2 = input('변경할 단어를 입력하세요')

with open('mydata.txt','r') as f:
    with open('mydata1.txt','w') as h:
        t = f.read()
        t = t.replace(a1,a2)
        h.write(t)

print('[%s]를[%s]로 변경하였습니다'%(a1,a2))
