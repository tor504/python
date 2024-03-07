import requests
import re

def extract_emails_from_webpage(url):
    """
    웹페이지에서 이메일 주소를 추출하는 함수
    :param url: 웹페이지의 URL
    :return: 추출된 이메일 주소 리스트
    """
    # 웹페이지의 HTML을 가져옵니다.
    response = requests.get(url)
    html_content = response.text

    # 이메일 주소를 추출하기 위한 정규 표현식
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    # 추출된 이메일 주소를 저장할 리스트
    extracted_emails = []

    # HTML에서 이메일 주소를 찾습니다.
    emails = re.findall(email_pattern, html_content)
    extracted_emails.extend(emails)

    return extracted_emails

if __name__ == "__main__":
    url = "https://v.daum.net/v/20230303140011566"  # 웹페이지의 URL을 입력하세요
    emails = extract_emails_from_webpage(url)
    print("추출된 이메일 주소:")
    for email in emails:
        print(email)