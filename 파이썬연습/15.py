# 1mb 10개로 분리
# fn = 'python-3.8.2.exe'
# ss = 1024 * 1024 * 2 # 3mb
# suf = 0

# with open(fn,'rb') as f:
#     buf = f.read(ss)
#     while buf:
#         sub = fn + '_' + str(suf)
#         with open(sub,'wb') as h:
#             h.write(buf)
#             print("[%s]완료"%sub)


#         buf = f.read(ss)
#         suf += 1


# 1m 10개 합쳐서 10mb 파일 만들기
BUFSIZE = 256 * 1024
mergef = 'ret.exe'
flist = ['python-3.8.2.exe_' + str(x) for x in range(12)]

with open(mergef,'wb') as f:
    for filename in flist:
        print("[%s] 합치는 중 ... "%filename)
        with open(filename,'rb') as h:
            buf = h.read(BUFSIZE)
            while buf:
                f.write(buf)
                buf = h.read((BUFSIZE))

print("파일 합치기가 완료되었습니다")