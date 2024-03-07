def load_words_from_file(file_path):
    words = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            word, meaning = line.strip().split(':')
            words[word.strip()] = meaning.strip()
    return words

# 파일 경로 설정
file_path = 'voca.txt'
vocabulary = load_words_from_file(file_path)

def quiz_program(vocabulary):
    correct_count = 0
    total_count = len(vocabulary)

    print("영어 단어 암기 프로그램을 시작합니다!")

    for word, meaning in vocabulary.items():
        user_answer = input(f"{word}의 뜻은 무엇일까요? ")
        if user_answer.lower() == meaning.lower():
            print("정답입니다!")
            correct_count += 1
        else:
            print(f"오답입니다. 정답은 {meaning}입니다.")

    print(f"\n퀴즈 완료! 정답률: {correct_count / total_count * 100:.2f}%")

# 퀴즈 프로그램 실행
quiz_program(vocabulary)
