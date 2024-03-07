import pandas as pd
import matplotlib.pyplot as plt
import pyupbit

# 특정 기간 동안의 비트코인 가격 데이터를 가져오는 함수
def get_price_data(ticker, start_date, end_date):
    df = pyupbit.get_ohlcv(ticker, interval="day", to=end_date)
    return df.loc[start_date:end_date]

# 1년 동안의 비트코인 가격 데이터 가져오기 (2023년 3월 5일부터 2024년 3월 5일까지)
btc_data = get_price_data("KRW-BTC", "2023-03-05", "2024-03-05")

# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(btc_data.index, btc_data["close"], label="Bitcoin Price (KRW-BTC)")
plt.xlabel("Date")
plt.ylabel("Price (KRW)")
plt.title("Bitcoin Price in the Last Year")
plt.grid(True)
plt.legend()
plt.show()
