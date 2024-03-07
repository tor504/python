import zipfile
import os

def zip_files(directory, zip_name):
    """
    디렉토리 내의 파일들을 압축하는 함수
    :param directory: 압축할 파일들이 있는 디렉토리 경로
    :param zip_name: 생성될 zip 파일의 이름
    """
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for root, _, files in os.walk(directory):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), directory))

if __name__ == "__main__":
    # 압축할 파일들이 있는 디렉토리 경로
    directory = '파이썬연습2월\압축.txt'
    # 생성될 zip 파일의 이름
    zip_name = 'compressed.zip'
    zip_files(directory, zip_name)