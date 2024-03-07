import random

# 단어와 뜻의 딕셔너리
words = {
    'apple': '사과',
    'banana': '바나나',
    'carrot': '당근',
    'dog': '개',
    # 추가적으로 필요한 단어를 원하는 만큼 추가할 수 있습니다.
}

def memorize_words():
    print("일상생활에 많이 쓰이는 단어를 암기하세요!")
    print("프로그램을 종료하려면 'q'를 입력하세요.")

    while True:
        # 무작위로 단어 선택
        word = random.choice(list(words.keys()))
        meaning = words[word]

        # 사용자에게 뜻을 제시
        print(f"단어: {word}")
        user_input = input(f"{meaning}의 영어 단어를 입력하세요: ")

        # 프로그램 종료
        if user_input.lower() == 'q':
            print("프로그램을 종료합니다.")
            break

        # 정답 확인
        if user_input.lower() == word:
            print("정답입니다!")
        else:
            print(f"오답입니다. 정답은 {word}입니다.")

if __name__ == "__main__":
    memorize_words()