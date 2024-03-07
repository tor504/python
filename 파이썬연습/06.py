#read
# f = open('stockcode.txt','r')
# a = f.read()
# print(a)
# f.close()

#readline
# f = open('stockcode.txt','r')
# line_num = 1
# line  = f.readline()
# while line:
#     print('%d %s'%(line_num,line),end= '')
#     line = f.readline()
#     line_num +=1
# f.close()

#readlines
# f = open('stockcode.txt','r')

# lines  = f.readlines()
# for line_num,line in enumerate(lines):
#     print('%d %s'%(line_num+1,line),end='')
# f.close()

# write
# t = input("파일에 저장할 내용을 입력하세요")
# f = open('mydata.txt','w')
# f.write(t)
# f.close()
# f1 = open('mydata.txt','r')
# a= f1.read()
# print(a)
# f1.close()

#writelines
# count = 1
# d = []
# print('파일에 내용을 저장하려면 내용을 입력하지 말고 [Enter]를 누르세요')
# while True:
#     t = input('[%d]파일에 저장할 내용을 입력하세요'%count)
#     if t == '':
#         break
#     d.append(t+'\n')
#     count += 1

# f = open('mydata.txt','w')
# f.writelines(d)
# f.close()


# read,write -> copy
# f = open('stockcode.txt','r')
# h = open('stockcode_copy.txt','w')

# data = f.read()
# h.write(data)

# f.close()
# h.close()

# 바이너리 파일 복사하기
# bufsize = 1024
# f = open('img_sample.jpg','rb')
# h = open('img_sample_copy.jpg','wb')

# data = f.read(bufsize)
# while data:
#     h.write(data)
#     data = f.read(bufsize)

# f.close()
# h.close()

# 파일을 열고 자동으로 닫기 -> with ~ as
with open('stockcode.txt','r') as f:
    for line_num,line in enumerate(f.readlines()):
        print("%d %s"%(line_num+1,line),end='')
