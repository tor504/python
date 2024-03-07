import psutil
import tkinter as tk

def update_usage():
    cpu_label.config(text=f"CPU 사용량: {psutil.cpu_percent()}%")
    ram_label.config(text=f"RAM 사용량: {psutil.virtual_memory().percent}%")
    root.after(1000, update_usage)  # 1초마다 업데이트

# GUI 생성
root = tk.Tk()
root.title("시스템 모니터")

cpu_label = tk.Label(root, text="", font=("Helvetica", 12))
cpu_label.pack(pady=10)

ram_label = tk.Label(root, text="", font=("Helvetica", 12))
ram_label.pack(pady=10)

update_usage()  # 업데이트 함수 호출

root.mainloop()