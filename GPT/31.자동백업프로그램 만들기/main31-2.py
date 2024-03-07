import tkinter as tk
from tkinter import filedialog
from distutils.dir_util import copy_tree

def select_source_folder():
    source_folder_path = filedialog.askdirectory()
    source_folder_entry.delete(0, tk.END)
    source_folder_entry.insert(0, source_folder_path)

def select_destination_folder():
    destination_folder_path = filedialog.askdirectory()
    destination_folder_entry.delete(0, tk.END)
    destination_folder_entry.insert(0, destination_folder_path)

def backup():
    source_folder = source_folder_entry.get()
    destination_folder = destination_folder_entry.get()
    copy_tree(source_folder, destination_folder)
    result_label.config(text="백업이 완료되었습니다.")

# GUI 생성
root = tk.Tk()
root.title("폴더 백업 프로그램")
root.geometry("300x200")

# 레이블 생성
source_folder_label = tk.Label(root, text="원본 폴더:")
source_folder_label.pack()

destination_folder_label = tk.Label(root, text="대상 폴더:")
destination_folder_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# 텍스트 엔트리 생성
source_folder_entry = tk.Entry(root, width=30)
source_folder_entry.pack()

destination_folder_entry = tk.Entry(root, width=30)
destination_folder_entry.pack()

# 버튼 생성
select_source_button = tk.Button(root, text="원본 폴더 선택", command=select_source_folder)
select_source_button.pack()

select_destination_button = tk.Button(root, text="대상 폴더 선택", command=select_destination_folder)
select_destination_button.pack()

backup_button = tk.Button(root, text="백업 시작", command=backup)
backup_button.pack()

root.mainloop()
