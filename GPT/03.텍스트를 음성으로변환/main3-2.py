from gtts import gTTS
import os

def text_to_speech(text, filename='output.mp3'):
    # gTTS 객체 생성
    tts = gTTS(text=text, lang='ko')
    # 음성 파일로 저장
    tts.save(filename)
    print(f'음성 파일 "{filename}"이 생성되었습니다.')

# 텍스트 입력
text = "안녕하세요. 나는 백수입니다."
# 텍스트를 음성으로 변환하여 저장
text_to_speech(text)