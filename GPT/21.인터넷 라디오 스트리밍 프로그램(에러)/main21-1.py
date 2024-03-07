import vlc

# 라디오 스트림 URL
radio_url = "http://serpent0.duckdns.org:8088/mbcfm.pls"

# VLC 미디어 플레이어 인스턴스 생성
player = vlc.MediaPlayer(radio_url)

# 라디오 재생
player.play()

# 재생 중인 동안 프로그램을 계속 실행하도록 유지
while True:
    pass
