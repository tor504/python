import openpyxl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 사용자로부터 이메일과 비밀번호 입력 받기
email_address = input("이메일 주소를 입력하세요: ")
email_password = input("이메일 비밀번호를 입력하세요: ")

# 엑셀 파일 열기
workbook = openpyxl.load_workbook('이메일.xlsx')
sheet = workbook.active

# 이메일 서버 설정
smtp_server = 'smtp.naver.com'  # SMTP 서버 주소
smtp_port = 465  # SMTP 포트 (일반적으로 587 또는 465)

# 이메일 보내는 함수
def send_email(to_email, name):
    # 이메일 내용 작성
    subject = f"{name}님 환영합니다"
    body = f"{name}님 늦지 않게 와주세요"
    message = MIMEMultipart()
    message['From'] = email_address
    message['To'] = to_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # 이메일 보내기
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(email_address, email_password)
        server.send_message(message)

# 각 행을 순회하며 이메일 보내기
for row in sheet.iter_rows(values_only=True):
    email = row[0]
    name = row[1]
    send_email(email, name)

# 엑셀 파일 닫기
workbook.close()