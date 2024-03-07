from gtts import gTTS

def create_mp3(sentence, filename):
    tts = gTTS(text=sentence, lang='ko')
    tts.save(filename)

def main():
    sentences = ["안녕하세요", "반갑습니다", "오늘은 날씨가 좋네요"]
    
    for i, sentence in enumerate(sentences, 1):
        filename = f"output_{i}.mp3"
        create_mp3(sentence, filename)
        print(f"File '{filename}' created successfully.")

if __name__ == "__main__":
    main()