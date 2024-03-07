import qrcode
import os

def generate_qr_code(data, file_path):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save(file_path)

if __name__ == "__main__":
    # 스크립트의 현재 경로를 가져옴
    script_dir = os.path.dirname(os.path.realpath(__file__))
    
    # qrdata.txt 파일의 상대 경로
    data_file_path = os.path.join(script_dir, "qrdata.txt")
    
    # QR 코드 이미지가 저장될 폴더 경로
    folder_path = os.path.join(script_dir, "")
    
    # 폴더가 없으면 생성
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # 파일을 읽어서 QR 코드 생성
    with open(data_file_path, "r") as file:
        lines = file.readlines()
        for idx, line in enumerate(lines):
            qr_data = line.strip()
            file_name = f"qr_code_{idx}.png"
            file_path = os.path.join(folder_path, file_name)
            generate_qr_code(qr_data, file_path)
            print(f"QR 코드가 {file_path} 경로에 생성되었습니다.")
            
            '''이 코드는 스크립트 파일이 있는 디렉토리를 기준으로 
            qrdata.txt 파일을 찾습니다. 따라서 스크립트 파일과 qrdata.txt 
            파일이 같은 디렉토리에 있어야 합니다. 
            만약 다른 디렉토리에 있거나 절대 경로를 사용해야 하는 경우, 
            data_file_path 변수를 해당 경로로 수정하면 됩니다.'''