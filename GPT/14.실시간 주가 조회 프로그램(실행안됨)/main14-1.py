import requests
import json
import time

API_KEY = 'YOUR_API_KEY'  # 여기에 Alpha Vantage API 키를 입력하세요.
SYMBOL = 'AAPL'  # 조회할 주식의 심볼

def get_stock_price(symbol):
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    if 'Global Quote' in data:
        return data['Global Quote']['05. price']
    else:
        return None

def main():
    while True:
        price = get_stock_price(SYMBOL)
        if price:
            print(f'현재 {SYMBOL}의 가격은 ${price}입니다.')
        else:
            print(f'{SYMBOL}의 가격을 가져올 수 없습니다.')
        time.sleep(5)  # 5초마다 업데이트

if __name__ == "__main__":
    main()