import tkinter as tk
import os

def shutdown():
    os.system("shutdown -s -t 0")

# GUI 생성
root = tk.Tk()
root.title("컴퓨터 예약 종료 프로그램")
root.geometry("300x200")

# 종료 버튼
shutdown_button = tk.Button(root, text="컴퓨터 예약 종료", command=shutdown)
shutdown_button.pack()

root.mainloop()
