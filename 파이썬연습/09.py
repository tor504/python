# 현재 시간을 년월일시분초로 출력 -> localtime, strftime
# from time import localtime,strftime

# logfile = 'test log'
# def writelog(logfile,log):
#     time_stamp = strftime("%Y-%m-%d %X\t",localtime())
#     log = time_stamp + log + '\n'

#     with open(logfile,'a') as f:
#         f.writelines(log)
# writelog(logfile,'2번째 로깅문장입니다')

# 올해 경과된 날짜수 계산하기 -> (localtime)
# from time import localtime

# t = localtime()
# s_day = "%d-01-01"%t.tm_year
# e_day = t.tm_yday

# print("오늘은 [%s]이후 [%d]일째 되는 날입니다"%(s_day,e_day))

# 오늘의 요일 계산
from time import localtime

b = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']

t = localtime()
today = '%d-%d-%d' %(t.tm_year,t.tm_mon,t.tm_mday)
a = b[t.tm_wday]

print("[%s]오늘은 [%s]입니다"%(today,a))

# 프로그램 실행시간 계산 -> datetime.now

from datetime import datetime

s = datetime.now()
print('1에서 100만까지 더합니다')

a = 0
for i in range(1000001):
    a += i

print('1에서 백만까지 결과: %d'%a)
end = datetime.now()

b = end - s
print('총계산 시간:',end='');print(b)
b_ms = int(b.total_seconds()*1000)
print('총 계산시간:%d ms'%b_ms)
