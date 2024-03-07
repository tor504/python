import enchant

def spell_check(text):
    # 영어 사전으로 초기화
    dictionary = enchant.Dict("en_US")

    # 텍스트를 단어 단위로 분할하여 맞춤법 검사
    words = text.split()
    misspelled_words = []
    for word in words:
        if not dictionary.check(word):
            misspelled_words.append(word)
    return misspelled_words

def main():
    text = input("맞춤법을 검사할 텍스트를 입력하세요: ")
    misspelled_words = spell_check(text)
    if misspelled_words:
        print("다음 단어들이 맞춤법에 어긋납니다:")
        print(", ".join(misspelled_words))
    else:
        print("맞춤법에 어긋나는 단어가 없습니다.")

if __name__ == "__main__":
    main()