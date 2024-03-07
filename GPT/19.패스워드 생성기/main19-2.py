import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    special_characters = special_char_entry.get()
    characters = string.ascii_letters + string.digits + special_characters
    password = ''.join(random.choice(characters) for _ in range(length))
    password_display.config(state=tk.NORMAL)
    password_display.delete(1.0, tk.END)
    password_display.insert(tk.END, password)
    password_display.config(state=tk.DISABLED)

# Create GUI window
root = tk.Tk()
root.title("패스워드 생성기")
root.geometry("300x300")

# Label for length input
length_label = tk.Label(root, text="패스워드 길이:")
length_label.pack(pady=5)

# Entry for password length
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Label for special characters input
special_char_label = tk.Label(root, text="특수문자:")
special_char_label.pack(pady=5)

# Entry for special characters
special_char_entry = tk.Entry(root)
special_char_entry.pack(pady=5)

# Button to generate password
generate_button = tk.Button(root, text="생성된 패스워드", command=generate_password)
generate_button.pack(pady=10)

# Text widget to display generated password
password_display = tk.Text(root, height=5, width=30, state=tk.DISABLED)
password_display.pack(pady=10)

root.mainloop()