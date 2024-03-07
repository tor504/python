from datetime import datetime, timedelta
from plyer import notification
import time

def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name='회의 알림',  # 알림의 앱 이름 설정
        app_icon=None,  # 알림에 사용할 아이콘 파일 경로 (None으로 설정하면 기본값 사용)
        timeout=10  # 알림이 표시될 시간 (초 단위, 기본값은 10초)
    )

def check_meeting_time():
    current_time = datetime.now()
    weekday = current_time.weekday()  # 현재 요일 (월요일: 0, 화요일: 1, ... 일요일: 6)

    if weekday in [0, 2, 4]:  # 월요일, 수요일, 금요일인 경우
        if current_time.hour == 9 and current_time.minute == 50:
            # 9시 50분에 알림 표시
            show_notification("회의 시작 10분 전", "회의가 곧 시작됩니다.")

def main():
    while True:
        check_meeting_time()
        time.sleep(60)  # 1분마다 반복하여 현재 시간을 확인

if __name__ == "__main__":
    main()