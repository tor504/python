import pandas as pd

def save_emails_to_excel(emails, output_file):
    """
    이메일 주소를 엑셀 파일에 저장하는 함수
    :param emails: 저장할 이메일 주소 리스트
    :param output_file: 출력할 엑셀 파일 경로
    """
    # 이메일 주소를 DataFrame으로 변환합니다.
    df = pd.DataFrame({'Email': emails})

    # DataFrame을 엑셀 파일로 저장합니다.
    df.to_excel(output_file, index=False)

if __name__ == "__main__":
    emails = ["jjw1504@naver.com", "qnas2192@gmail.com"]  # 추출한 이메일 주소 리스트
    output_file = "파이썬연습2월/10.이메일을 수집하여 엑셀에 기록하기/이메일.xlsx"  # 저장할 엑셀 파일 경로
    save_emails_to_excel(emails, output_file)