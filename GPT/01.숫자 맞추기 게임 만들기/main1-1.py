import random

a = random.randint(1,100) # 1부터 100까지 무작위 숫자 생성

b = 0 #몇 회 시도했는지 저장하는 변수

while True: # 무한 반복문 
    c = int(input("1부터 100까지의 숫자를 입력하세요:  "))  #사용자로 부터 숫자 입력 받기 
    b += 1 # 시도 횟수 증가
    if c > a:
        print("입력한 숫자가 너무 큽니다.")
    elif c < a:
        print("입력한 숫자가 너무 작습니다.")
    else:
        print(f'축하합니다! {b}회 만에 숫자를 맞췄습니다.') 
        break
    