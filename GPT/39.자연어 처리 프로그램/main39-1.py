import re

def extract_words(text):
    # 정규표현식을 사용하여 알파벳으로만 이루어진 단어를 추출
    words = re.findall(r'\b\w+\b', text)
    return words

def main():
    text = input("텍스트를 입력하세요: ")
    words = extract_words(text)
    print("추출된 단어:", words)

if __name__ == "__main__":
    main()
