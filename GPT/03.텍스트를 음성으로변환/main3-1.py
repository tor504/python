from gtts import gTTS
import os

def text_to_speech(text, filename='output.mp3'):
    # 한글 텍스트를 한국어로 설정하여 gTTS 객체 생성
    tts = gTTS(text=text, lang='ko')
    # 음성 파일로 저장
    tts.save(filename)
    # 음성 파일 재생 (이 코드는 윈도우 운영체제를 기준으로 작성되었습니다)
    os.system(f'start {filename}')

# 텍스트 입력
text = "안녕하세요. 반갑습니다."
# 텍스트를 음성으로 변환하여 재생
text_to_speech(text)