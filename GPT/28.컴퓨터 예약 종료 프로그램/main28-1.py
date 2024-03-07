import os
import time

def 예약_종료(시간_분):
    """
    시간_분 후에 컴퓨터를 종료하는 함수
    """
    시간_초 = 시간_분 * 60
    os.system(f"shutdown -s -t {시간_초}")

if __name__ == "__main__":
    try:
        입력_분 = int(input("몇 분 후에 종료할까요? "))
        예약_종료(입력_분)
        print(f"{입력_분} 분 후에 컴퓨터가 종료됩니다.")
    except ValueError:
        print("올바른 숫자를 입력하세요.")