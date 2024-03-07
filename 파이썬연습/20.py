# 웹서버 로그 처리하기 -> 총페이지뷰 수 계산 
# pageviews = 0

# with open('access_log','r') as f:
#     logs = f.readlines()
#     for log in logs:
#         log = log.split()
#         status = log[8]
#         if status == '200':
#             pageviews += 1

# print("총 페이지 뷰:[%d]"%pageviews)

# 웹서버 로그 처리하기 -> 고유 방문자 수 계산 
# visit_ip = []

# with open('access_log','r') as f:
#     logs = f.readlines()
#     for log in logs:
#         log = log.split()
#         ip = log[0]
#         if ip not in visit_ip:
#             visit_ip.append(ip)

# print("고유 방문자 수:[%d]" %len(visit_ip))


# 웹서버 로그 처리하기 -> 총 서비스 용량 계산하기
# KB = 1024
# total_service = 0

# with open('access_log','r') as f:
#     logs = f.readlines()
#     for log in logs:
#         log = log.split()
#         sevicebyte = log[9]
#         if sevicebyte.isdigit():
#             total_service += int(sevicebyte)

# total_service /= KB
# print("총 서비스 용량:%dKB"%total_service)

# 웹서버 로그 처리하기 -> 사용자별 서비스 용량 계산하기
sevices = {}

with open('access_log','r') as f:
    logs = f.readlines()
    for log in logs:
        log = log.split()
        ip = log[0]
        servkicebyte = log[9]
        if servkicebyte.isdigit():
            servkicebyte = int(servkicebyte)
        else:
            servkicebyte = 0

        if ip not in sevices:
            sevices[ip] = servkicebyte
        else:
            sevices[ip] += servkicebyte

a = sorted(sevices.items(),key=lambda x:x[1],reverse=True)

print("사용자 IP - 서비스용량")
for ip,b in a:
    print("[%s]-[%s]"%(ip,b))


