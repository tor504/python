# 파일 크기 구하기 -> (os.path  ~  getsize)

# from os.path import getsize

# f1 = 'stockcode.txt'
# f2 = '/Volumes/sub/port/port-2/img_sample.jpg'
# file_size1 = getsize(f1)
# file_size2 = getsize(f2)

# print('파일네임:%s \t파일크기:%d'%(f1,file_size1))
# print('파일네임:%s \t파일크기:%d'%(f2,file_size2))

# 파일삭제하기(os.remove)
# from os import remove

# a = 'stockcode_part.txt'
# b = input('[%s]파일을 삭제하시겠습니까?(y/n)'%a)
# if b == 'y':
#     remove(a)
#     print('[%s]를 삭제했습니다.'%a)

# 파일 이름 바꾸기 -> os.rename
# from os import rename

# a = 'stockcode_copy.txt'
# newname = input('[%s]에 대한 새로운 파일이름을 입력하세요:'%a)
# rename(a,newname)c 
# print('[%s]->[%s]로 파일이름이 변경되었습니다.'%(a,newname))

# 파일을 다른 디렉토리로 이동하기
# from os import rename

# a = 's1.txt'
# newpath = input('[%s]를 이동할 디렉터리의 절대 경로를 입력하세요'%a)

# if newpath[-1] == '/':
#     newname = newpath + a
# else:
#     newname =newpath +'/' +a

# try:
#     rename(a,newname)
#     print('[%s]-> [%s]로 이동되었습니다'%(a,newname))
# except FileNotFoundError as e:
#     print(e)


#파일 목록 얻기 -> os.listdir ,glob.glob
# import os,glob

# folder = '/Volumes/sub/port/'
# file_list = os.listdir(folder)
# print(file_list)

# files = '*.txt'
# file_list = glob.glob(files)
# print(file_list)

# 현재 디렉토리 확인 바꾸기 -> os.getcwd, os.chdir
# import os

# pdir = os.getcwd();print(pdir)
# os.chdir('..');print(os.getcwd())
# os.chdir(pdir);print(os.getcwd())

# 디렉터리 생성 -> os.mkdir
# import os

# newfolder = input('새로 생성 할 디렉터리 이름을 입력 하세요')
# try:
#     os.mkdir(newfolder)
#     print('[%s]디렉터리를 새로 생성햇습니다'%newfolder)
# except Exception as e:
#     print(e)

# 디렉터리 제거 -> os.rmdir
import os

# a = 'tmp'
# b = input('[%s]디렉토리를 삭제하겠습니까?(y/n)'%a)
# if b == 'y':
#     try:
#         os.rmdir(a)
#         print('[%s]디렉터리를 삭제했습니다'%a)
#     except Exception as e:
#         print(e)

# 하위 디렉토리 및 파일 전체 삭제하기 -> shutil.rmtree
# import shutil
# import os

# a = '/Volumes/sub/port/port'
# print('[%s]하위 모든 디렉토리 및 파일들을 삭제합니다'%a)
# for file in os.listdir(a):
#     print(file)
# b = input('[%s]를 삭제하겠습니까?(y/n)'%a)
# if b == 'y':
#     try:
#         shutil.rmtree(a)
#         print('[%s]의 모든 하위디렉토리와 파일들을 삭제햇습니다'%a)
#     except Exceptionn as e:
#         print(e)

# 파일이 존재하는지 체크 -> os.path.exists
# import os
# from os.path import exists

# a = input('새로 생성할 디렉터리 이름을 입력하세요')
# if not exists(a):
#     os.mkdir(a)
#     print('[%s]디렉터리를 생성했습니다'%a)
# else:
#     print('[%s]은 이미 존재합니다'%a)


# 파일인지 디렉터리인지 확인 -> os.path.isfile , os.path.isdir
import os
from os.path import exists,isdir,isfile

a = os.listdir()

for file in a:
    if isdir(file):
        print("디렉토리: %s"%a)

for file in a:
    if isfile(file):
        print("파일:%s"%a)

