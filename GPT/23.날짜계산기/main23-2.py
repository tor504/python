from datetime import datetime

def days_since_start(start_date):
    try:
        # 오늘 날짜를 가져옵니다.
        today = datetime.today().date()

        # 문자열로부터 기준 날짜를 datetime 객체로 변환합니다.
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d").date()

        # 오늘과 기준 날짜 간의 차이를 계산하여 반환합니다.
        days_passed = (today - start_date_obj).days
        return days_passed
    except ValueError:
        return "날짜 형식이 올바르지 않습니다. YYYY-MM-DD 형식으로 입력해주세요."

def main():
    print("기준 날짜부터 오늘까지의 일수 계산기")
    print("기준 날짜를 입력하면 오늘까지의 경과 일수를 출력합니다.")
    print("날짜 형식은 YYYY-MM-DD로 입력해주세요.")
    print()

    start_date = input("기준 날짜를 입력하세요: ")

    days_passed = days_since_start(start_date)
    print(f"기준 날짜로부터 오늘까지 {days_passed}일이 경과했습니다.")

if __name__ == "__main__":
    main()