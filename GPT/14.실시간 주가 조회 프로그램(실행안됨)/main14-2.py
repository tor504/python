import requests

API_KEY = 'YOUR_API_KEY'  # Alpha Vantage API 키

def get_stock_price(symbol):
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    if 'Global Quote' in data:
        return data['Global Quote']['05. price']
    else:
        return None

def main():
    symbol = input("조회할 종목 번호를 입력하세요: ")
    price = get_stock_price(symbol)
    if price:
        print(f'{symbol}의 현재 가격은 ${price}입니다.')
    else:
        print(f'{symbol}의 가격을 가져올 수 없습니다.')

if __name__ == "__main__":
    main()