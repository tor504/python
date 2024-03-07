import tkinter as tk
from tkinter import ttk

def convert_length():
    value = float(entry_value.get())
    from_unit = combo_from.get()
    to_unit = combo_to.get()

    conversion_rates = {
        'm': {'km': 0.001, 'cm': 100, 'mm': 1000},
        'km': {'m': 1000, 'cm': 100000, 'mm': 1000000},
        'cm': {'m': 0.01, 'km': 0.00001, 'mm': 10},
        'mm': {'m': 0.001, 'km': 0.000001, 'cm': 0.1}
    }

    if from_unit in conversion_rates and to_unit in conversion_rates[from_unit]:
        conversion_rate = conversion_rates[from_unit][to_unit]
        result = value * conversion_rate
        label_result.config(text=f"{value} {from_unit}은(는) {result} {to_unit}입니다.")
    else:
        label_result.config(text="지원되지 않는 단위입니다.")

# Tkinter 윈도우 생성
root = tk.Tk()
root.title("단위 변환 프로그램")

# 입력 레이블과 엔트리 위젯
label_value = ttk.Label(root, text="변환할 값:")
label_value.grid(row=0, column=0, padx=5, pady=5)
entry_value = ttk.Entry(root)
entry_value.grid(row=0, column=1, padx=5, pady=5)

# 단위 선택 콤보 박스
label_from = ttk.Label(root, text="원래 단위:")
label_from.grid(row=1, column=0, padx=5, pady=5)
combo_from = ttk.Combobox(root, values=['m', 'km', 'cm', 'mm'])
combo_from.grid(row=1, column=1, padx=5, pady=5)
combo_from.current(0)

label_to = ttk.Label(root, text="변환할 단위:")
label_to.grid(row=2, column=0, padx=5, pady=5)
combo_to = ttk.Combobox(root, values=['m', 'km', 'cm', 'mm'])
combo_to.grid(row=2, column=1, padx=5, pady=5)
combo_to.current(0)

# 변환 버튼
btn_convert = ttk.Button(root, text="변환", command=convert_length)
btn_convert.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# 결과 레이블
label_result = ttk.Label(root, text="")
label_result.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# 윈도우 실행
root.mainloop()