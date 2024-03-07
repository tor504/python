import pytesseract
from PIL import Image

# 이미지 파일 경로
image_path = '/Volumes/sub/port/work-2/파이썬연습2월/32.이미지에서 글자추출하기/image.png'

# 이미지 열기
image = Image.open(image_path)

# 이미지에서 텍스트 추출
extracted_text = pytesseract.image_to_string(image)

# 추출된 텍스트 출력
print(extracted_text)
