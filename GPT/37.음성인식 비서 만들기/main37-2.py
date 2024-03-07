import speech_recognition as sr
import webbrowser
import pyttsx3

# 음성 출력 엔진 초기화
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def recognize_speech_from_microphone():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("말해주세요...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="ko-KR")
        print("인식된 텍스트:", text)
        return text
    except sr.UnknownValueError:
        print("음성을 인식할 수 없습니다.")
        return ""
    except sr.RequestError as e:
        print("음성 인식 API에 접근할 수 없습니다.", e)
        return ""

def main():
    while True:
        text = recognize_speech_from_microphone().lower()
        
        if "검색" in text:
            speak("무엇을 검색할까요?")
            search_query = recognize_speech_from_microphone().lower()
            if search_query:
                url = f"https://www.google.com/search?q={search_query}"
                webbrowser.open(url)
        
        elif "종료" in text:
            speak("프로그램을 종료합니다.")
            break

if __name__ == "__main__":
    main()
