import tkinter as tk
import pyupbit

def get_all_tickers():
    all_tickers = pyupbit.get_tickers(fiat="KRW")
    return all_tickers

def get_current_price(ticker):
    try:
        current_price = pyupbit.get_current_price(ticker)
        return current_price
    except Exception as e:
        return str(e)

def show_prices():
    ticker_list.delete(0, tk.END)
    for ticker in get_all_tickers():
        current_price = get_current_price(ticker)
        if isinstance(current_price, float):
            ticker_list.insert(tk.END, f"{ticker}: {current_price:.2f} KRW")
        else:
            ticker_list.insert(tk.END, f"{ticker}: Error - {current_price}")

# Tkinter 윈도우 생성
root = tk.Tk()
root.title("모든 가상화폐 시세 조회 프로그램")

# 리스트 박스 생성
ticker_list = tk.Listbox(root, width=50, height=20)
ticker_list.pack(padx=10, pady=10)

# 조회 버튼 생성
button_show_prices = tk.Button(root, text="시세 조회", command=show_prices)
button_show_prices.pack(padx=10, pady=5)

# Tkinter 윈도우 실행
root.mainloop()