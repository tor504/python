import tkinter as tk
from tkinter import filedialog
import pygame

def play_music():
    global music_file
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()

def choose_file():
    global music_file
    music_file = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])

def main():
    global music_file
    music_file = ""

    root = tk.Tk()
    root.title("Music Player")

    play_button = tk.Button(root, text="Play Music", command=play_music)
    play_button.pack(pady=10)

    choose_button = tk.Button(root, text="Choose Music File", command=choose_file)
    choose_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    main()