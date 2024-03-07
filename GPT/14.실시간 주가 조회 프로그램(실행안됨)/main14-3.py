import tkinter as tk
import requests

API_KEY = 'YOUR_API_KEY'  # Alpha Vantage API 키

def get_stock_price(symbol):
    url = f'https://finance.naver.com/item/sise.naver?code=005930'
    response = requests.get(url)
    data = response.json()
    if 'Global Quote' in data:
        return data['Global Quote']['05. price']
    else:
        return None

def show_price():
    symbol = symbol_entry.get()
    price = get_stock_price(symbol)
    if price:
        result_label.config(text=f'{symbol}의 현재 가격은 ${price}')
    else:
        result_label.config(text=f'{symbol}의 가격을 가져올 수 없습니다.')

# GUI 생성
root = tk.Tk()
root.title("주식 가격 조회 프로그램")

# 레이블 및 입력 필드 생성
symbol_label = tk.Label(root, text="종목 번호:")
symbol_label.pack(pady=5)
symbol_entry = tk.Entry(root)
symbol_entry.pack(pady=5)

# 가격 출력을 위한 레이블 생성
result_label = tk.Label(root, text="")
result_label.pack(pady=5)

# 조회 버튼 생성
search_button = tk.Button(root, text="조회", command=show_price)
search_button.pack(pady=5)

root.mainloop()