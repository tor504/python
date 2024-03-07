import tkinter as tk
import random

def generate_lotto_numbers():
    lotto_numbers = sorted(random.sample(range(1, 46), 6))
    result_label.config(text="로또 번호: " + ', '.join(map(str, lotto_numbers)))

# 윈도우 생성
window = tk.Tk()
window.title("로또 번호 생성기")
window.geometry("300x100")

# 버튼 생성
generate_button = tk.Button(window, text="로또 번호 생성", command=generate_lotto_numbers)
generate_button.pack(pady=10)

# 결과 텍스트 레이블 생성
result_label = tk.Label(window, text="")
result_label.pack()

# GUI 시작
window.mainloop()