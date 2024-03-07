import pyzipper
import os

def compress_with_password(source_dir, zip_file, password):
    """
    지정된 디렉토리의 파일을 암호화된 zip 파일로 압축하는 함수
    :param source_dir: 압축할 파일들이 있는 디렉토리 경로
    :param zip_file: 생성될 zip 파일의 이름
    :param password: 압축할 zip 파일의 암호
    """
    # 압축할 파일들을 추가할 암호화된 zip 파일을 생성합니다.
    with pyzipper.AESZipFile(zip_file, 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zf:
        # 암호를 설정합니다.
        zf.setpassword(password.encode())
        # 지정된 디렉토리의 파일들을 순회하며 압축합니다.
        for foldername, _, filenames in os.walk(source_dir):
            for filename in filenames:
                # 압축할 파일의 경로를 구성합니다.
                file_path = os.path.join(foldername, filename)
                # 파일을 암호화된 zip 파일에 추가합니다.
                zf.write(file_path, os.path.relpath(file_path, source_dir))

if __name__ == "__main__":
    # 압축할 파일들이 있는 디렉토리 경로
    source_dir = '압축.txt'
    # 생성될 zip 파일의 이름
    zip_file = 'compressed.zip'
    # 압축할 zip 파일의 암호
    password = 'your_password'

    # 파일을 압축합니다.
    compress_with_password(source_dir, zip_file, password)
