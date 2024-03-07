import random

# 사용자에게 인사하는 함수
def greet():
    responses = ["안녕하세요!", "안녕하세요, 어떻게 도와드릴까요?", "반가워요!"]
    return random.choice(responses)

# 사용자의 입력에 대해 응답하는 함수
def respond(user_input):
    if "안녕" in user_input:
        return greet()
    elif "잘 있어" in user_input:
        return "안녕히 가세요!"
    else:
        return "죄송해요, 잘 이해하지 못했어요. 다시 말씀해주세요."

# 챗봇 메인 함수
def chat():
    print("챗봇을 시작합니다. 종료하려면 '잘 있어'를 입력하세요.")
    while True:
        user_input = input("사용자: ")
        if user_input == "잘 있어":
            print("챗봇: 안녕히 가세요!")
            break
        response = respond(user_input)
        print("챗봇:", response)

if __name__ == "__main__":
    chat()
