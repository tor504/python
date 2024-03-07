import qrcode

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

if __name__ == "__main__":
    data = "https://www.example.com"  # QR 코드로 포함할 데이터
    filename = "qrcode_example.png"  # 이미지 파일로 저장할 파일명
    generate_qr_code(data, filename)
    print(f"QR 코드가 {filename} 파일로 저장되었습니다.")