import pyupbit
import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect("crypto_prices.db")
cursor = conn.cursor()

# 특정 가상화폐의 현재가를 가져오는 함수
def get_current_price(ticker):
    price = pyupbit.get_current_price(ticker)
    return price

# 비트코인(KRW-BTC)의 현재가 조회
btc_price = get_current_price("KRW-BTC")
print(f"비트코인(KRW-BTC)의 현재가: {btc_price} 원")

# 데이터베이스에 현재가 저장
cursor.execute("CREATE TABLE IF NOT EXISTS crypto_prices (ticker TEXT, price REAL)")
cursor.execute("INSERT INTO crypto_prices (ticker, price) VALUES (?, ?)", ("KRW-BTC", btc_price))
conn.commit()

# 데이터베이스 연결 종료
conn.close()
