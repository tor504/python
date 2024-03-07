import pyupbit

# 특정 가상화폐의 현재가를 가져오는 함수
def get_current_price(ticker):
    price = pyupbit.get_current_price(ticker)
    return price

# 비트코인(KRW-BTC)의 현재가 출력
btc_price = get_current_price("KRW-BTC")
print(f"비트코인(KRW-BTC)의 현재가: {btc_price} 원")
