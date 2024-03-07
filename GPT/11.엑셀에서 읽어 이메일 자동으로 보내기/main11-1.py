import openpyxl

# 엑셀 파일 열기
workbook = openpyxl.load_workbook('이메일.xlsx')

# 첫 번째 시트 선택
sheet = workbook.active

# 각 행을 순회하며 이메일 주소와 이름 출력
for row in sheet.iter_rows(min_row=2,values_only=True):
    email, name = row
    print(f"이메일: {email}, 이름: {name}")

# 엑셀 파일 닫기
workbook.close()