import matplotlib.pyplot as plt
import pyupbit
import pandas as pd

# 비트코인 티커
ticker = "BTC-KRW"

# 1년 전의 시간 계산
end_date = pd.Timestamp.now()
start_date = end_date - pd.Timedelta(days=365)

# 가격 데이터 가져오기
data = pyupbit.get_ohlcv(ticker, interval="day", to=end_date, count=365)

# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['close'], color='blue')
plt.title('Bitcoin Price (1 Year)')
plt.xlabel('Date')
plt.ylabel('Price (KRW)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# 그래프 표시
plt.show()