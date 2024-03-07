# 파일을 zip 압축파일로 만들기
# from zipfile import *

# def comPress(zipf,f):
#     print('[%s]-> [%s]압축 ...'%(f,zipf))
#     with ZipFile(zipf,'w') as ziph:
#         ziph.write(f)
#     print("압축이 끝났습니다")

# f = 'mydata.txt'
# zipf = f + '.zip'
# comPress(zipf,f)


# 디렉터리를 하나의 zip 압축파일 만들기
# from zipfile import *
# import os

# def comPressAll(zipn,folder):
#     print('[%s] -> [%s] 압축중 ...'%(folder,zipn))
#     with ZipFile(zipn,'w') as ziph:
#         for dirn,subd,lines in os.walk(folder):
#             for file in files:
#                 ziph.write(os.path.join(dirn,file))

# folder = 'tmp'
# zipn = folder + '.zip'
# comPressAll(zipn,folder)


# zip 파일 압축 풀기
from zipfile import *

def extractZip(zipname):
    with ZipFile(zipname,'r') as ziph:
        ziph.extractall()
        print("[%s] 가 성공적으로 추출되었습니다."%zipname)

extractZip('files.zip')