import speech_recognition as sr

def recognize_speech_from_mic(recognizer, microphone):
    with microphone as source:
        print("말해주세요...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        response["transcription"] = recognizer.recognize_google(audio, language="ko-KR")
    except sr.RequestError:
        # Google Speech Recognition API에 연결할 수 없음
        response["success"] = False
        response["error"] = "인터넷에 연결되어 있지 않습니다."
    except sr.UnknownValueError:
        # 인식할 수 없는 음성
        response["error"] = "음성을 인식할 수 없습니다."

    return response

if __name__ == "__main__":
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    speech = recognize_speech_from_mic(recognizer, microphone)

    if speech["success"]:
        print("인식된 텍스트:", speech["transcription"])
    else:
        print("오류:", speech["error"])
