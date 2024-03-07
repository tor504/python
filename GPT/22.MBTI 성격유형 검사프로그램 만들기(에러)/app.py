from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    questions = [
        "당신은 다른 사람들과 어울리는 것을 좋아하는 편인가요?",
        "새로운 상황에 적응하는 것이 쉽나요?",
        "일을 하는 동안 상세한 계획을 세우는 것을 좋아하나요?",
        "자신의 감정을 다른 사람들과 쉽게 표현하나요?"
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

    for i in range(len(questions)):
        answer = request.form.get(str(i+1))
        if answer == '2':
            scores[questions[i][0]] += 1
        else:
            scores[questions[i][0]] -= 1

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

    result = personality_types.get(personality_type, "결과 없음")
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)