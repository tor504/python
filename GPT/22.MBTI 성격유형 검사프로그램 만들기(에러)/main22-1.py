def mbti_test():
    print("MBTI 성격 유형 검사를 시작합니다.")
    print("다음 질문에 답해주세요. (1 또는 2 선택)")

    questions = [
        "당신은 다른 사람들과 어울리는 것을 좋아하는 편인가요? \n1. 그렇습니다. \n2. 아니요.",
        "새로운 상황에 적응하는 것이 쉽나요? \n1. 네. \n2. 아니요.",
        "일을 하는 동안 상세한 계획을 세우는 것을 좋아하나요? \n1. 그렇습니다. \n2. 아니요.",
        "자신의 감정을 다른 사람들과 쉽게 표현하나요? \n1. 네. \n2. 아니요."
        # 추가적으로 필요한 질문을 원하는 만큼 추가할 수 있습니다.
    ]

    personality_types = {
        "ISTJ": "청렴결백한 논리주의자",
        "ISFJ": "용감한 수호자",
        "INFJ": "선의의 옹호자",
        "INTJ": "용의주도한 전략가",
        "ISTP": "만능 재주꾼",
        "ISFP": "호기심 많은 예술가",
        "INFP": "열정적인 중재자",
        "INTP": "논리적인 사색가",
        "ESTP": "모험을 즐기는 사업가",
        "ESFP": "자유로운 영혼의 연예인",
        "ENFP": "재기발랄한 사교가",
        "ENTP": "뜨거운 논쟁을 즐기는 변론가",
        "ESTJ": "엄격한 관리자",
        "ESFJ": "사교적인 외교관",
        "ENFJ": "정의로운 사업가",
        "ENTJ": "대담한 통솔자"
    }

    # 각 요소에 대한 점수 초기화
    scores = {
        "E": 0,
        "I": 0,
        "S": 0,
        "N": 0,
        "T": 0,
        "F": 0,
        "J": 0,
        "P": 0
    }

    # 질문에 대한 답변 처리
    
    for question in questions:
        print(question)
        while True:
            answer = input()
            if answer in ['1', '2']:
                break
            else:
                print("잘못된 입력입니다. 1 또는 2를 선택해주세요.")
    # 성격 유형 결정
    personality_type = ""
    if scores['E'] >= 0:
        personality_type += 'E'
    else:
        personality_type += 'I'

    if scores['S'] >= 0:
        personality_type += 'S'
    else:
        personality_type += 'N'

    if scores['T'] >= 0:
        personality_type += 'T'
    else:
        personality_type += 'F'

    if scores['J'] >= 0:
        personality_type += 'J'
    else:
        personality_type += 'P'

    print("\n당신의 MBTI 성격 유형은", personality_types[personality_type], "입니다.")

if __name__ == "__main__":
    mbti_test()