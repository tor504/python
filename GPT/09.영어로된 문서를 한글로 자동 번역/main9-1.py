from googletrans import Translator
import os

def translate_text(input_file):
    """
    주어진 파일에서 영어를 한국어로 번역하고 같은 파일에 저장하는 함수
    :param input_file: 입력 파일 경로
    """
    # 번역기 객체 생성
    translator = Translator()

    # 파일 경로에서 파일 이름과 확장자를 추출
    file_name, file_extension = os.path.splitext(input_file)
    # 번역된 파일의 이름을 설정 (예: "영어문서.txt" -> "한글문서.txt")
    output_file = file_name + "_한글" + file_extension

    # 입력 파일 열기
    with open(input_file, 'r', encoding='utf-8') as f:
        english_text = f.read()

    # 영어를 한국어로 번역
    translated_text = translator.translate(english_text, src='en', dest='ko').text

    # 번역된 텍스트를 파일에 쓰기
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(translated_text)

if __name__ == "__main__":
    input_file_path = r"파이썬연습2월/09.영어로된 문서를 한글로 자동 번역/1.txt"
    translate_text(input_file_path)