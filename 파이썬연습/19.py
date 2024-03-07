# 데이터 처리하기 -> 연도별 출생아 수 계산하기
# def countBirths():
#     a = []
#     for y in range(1880,2016):
#         count = 0
#         f1 = 'names/yob%d.txt'%y
#         with open(f1,'r') as f:
#             data = f.readlines()
#             for d in data:
#                 if d[-1] == '\n':
#                     d = d[:-1]

#                 birth = d.split(',')[2]
#                 count += int(birth)
#         a.append((y,count))
#     return a

# result = countBirths()
# with open("birth_by_year.csv",'w') as f:
#     for year,birth in result:
#         data = '%s,%s\n'%(year,birth)
#         print(data)
#         f.write(data)

# 데이터 처리하기 -> 연도별 성별 출생아 수 계산하기
# def countBirthsBySex():
#     a = []
#     for y in range(1880,2016):
#         count_f = 0
#         count_m = 0
#         filename = 'names/yob%d.txt'%y
#         with open(filename,'r') as f:
#             data = f.readlines()
#             for d in data:
#                 if d[-1] == '\n':
#                     d = d[:-1]

#                 tmp = d.split(',')
#                 sex = tmp[1]
#                 birth = tmp[2]

#                 if sex == 'F':
#                     count_f += int(birth)
#                 else:
#                     count_m += int(birth)

#         a.append((y,count_f,count_m))
#     return a

# result = countBirthsBySex()
# with open("birth_by_sex.csv",'w') as f:
#     for y,bf,bm in result:
#         data = "%s,%s,%s\n"%(y,bf,bm)
#         print(data)
#         f.write(data)

# # 데이터 처리하기 -> 연도별 인기있는 상위 10개 성별 출생아 수 계산하기
from os.path import exists

def getTop10BabyName(year):
    nameF = {} #사전 정의
    nameM = {} #사전 정의

    filename = 'names/yob%s.txt'%year
    if not exists(filename):
        print("[%s] 파일이 존재하지 않습니다."%filename)
        return None
    with open(filename,'r') as f:
        data = f.readlines()
        for d in data:
            if d[-1] == '\n':
                d = d[:-1]

            tmp = d.split(',')
            name = tmp[0]
            sex = tmp[1]
            birth = tmp[2]

            if sex == "F":
                a = nameF
            else:
                a = nameM
            
            if name in a:
                a[name] += int(birth)
            else:
                a[name] = int(birth)

    aF = sorted(nameF.items(),key= lambda x : x[1],reverse = True) #_.items 구조
    aM = sorted(nameM.items(),key= lambda x : x[1],reverse = True)

    for i,name in enumerate(aF):
        if i > 9:
            break
        print("Top_%d 여자아기 이름: %s"%(i+1,name))

    for i,name in enumerate(aM):
        if i > 9:
            break
        print("Top_%d 남자아기 이름: %s"%(i+1,name))

y = input("인기순 상위10개 이름을 알고 싶은 출생년도를 입력하세요(예:2001):")
getTop10BabyName(y)

