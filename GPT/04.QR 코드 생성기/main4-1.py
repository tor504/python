import qrcode

def generate_qr_code(text, filename='qr_code.png'):
    # QR 코드 생성
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    # 이미지 생성
    img = qr.make_image(fill_color="black", back_color="white")

    # 이미지 파일로 저장
    img.save(filename)
    print(f'QR 코드 이미지 "{filename}"이 생성되었습니다.')

# QR 코드로 변환할 텍스트 입력
text = "https://www.example.com"
# QR 코드 생성 및 저장
generate_qr_code(text)