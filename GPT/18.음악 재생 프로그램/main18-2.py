import pygame

def play_music(file_path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    # Wait for the music to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def main():
    music_file = "D:/port/work-1/work/파이썬연습2월/18.음악 재생 프로그램\output_1.mp3"  # Replace 'your_music_file.mp3' with the path to your music file
    play_music(music_file)

if __name__ == "__main__":
    main()