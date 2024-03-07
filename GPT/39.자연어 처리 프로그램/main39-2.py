from konlpy.tag import Okt

def extract_nouns(text):
    okt = Okt()
    nouns = okt.nouns(text)
    return nouns

def main():
    text = input("한글 텍스트를 입력하세요: ")
    nouns = extract_nouns(text)
    print("추출된 명사:", nouns)

if __name__ == "__main__":
    main()
