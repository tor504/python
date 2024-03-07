from datetime import datetime

def date_diff(date1, date2):
    try:
        # 문자열로부터 날짜 객체로 변환
        date1_obj = datetime.strptime(date1, "%Y-%m-%d")
        date2_obj = datetime.strptime(date2, "%Y-%m-%d")

        # 두 날짜 간의 차이 계산
        diff = abs(date2_obj - date1_obj).days
        return diff
    except ValueError:
        return "날짜 형식이 올바르지 않습니다. YYYY-MM-DD 형식으로 입력해주세요."

def main():
    print("날짜 계산기")
    print("두 날짜 간의 일수 차이를 계산합니다.")
    print("날짜 형식은 YYYY-MM-DD로 입력해주세요.")
    print()

    date1 = input("첫 번째 날짜를 입력하세요: ")
    date2 = input("두 번째 날짜를 입력하세요: ")

    diff = date_diff(date1, date2)
    print(f"두 날짜 간의 일수 차이: {diff}일")

if __name__ == "__main__":
    main()