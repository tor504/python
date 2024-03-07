import zipfile
import itertools

def crack_zip_password(zip_file_path):
    """
    지정된 zip 파일의 암호를 찾는 함수
    :param zip_file_path: zip 파일의 경로
    """
    # 가능한 암호 조합을 생성하기 위해 숫자와 영문자를 조합하여 만듭니다.
    characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # 암호의 자리수를 1부터 9까지 변경하여 시도합니다.
    for length in range(1, 10):
        # itertools.product를 사용하여 가능한 모든 조합을 생성합니다.
        for attempt in itertools.product(characters, repeat=length):
            password = ''.join(attempt)
            try:
                # 현재 시도 중인 암호로 zip 파일을 엽니다.
                with zipfile.ZipFile(zip_file_path, 'r') as zipf:
                    # extractall 메서드를 사용하여 압축을 푸는데, 암호가 틀리면 BadZipFile 에러가 발생합니다.
                    zipf.extractall(pwd=password.encode())
                # 암호가 올바르게 해독되었을 때 메시지를 출력하고 함수를 종료합니다.
                print(f'암호를 찾았습니다: {password}')
                return
            except zipfile.BadZipFile:
                # 암호가 틀렸을 때는 그냥 다음 암호를 시도합니다.
                pass
    # 암호를 찾지 못한 경우 메시지를 출력합니다.
    print('암호를 찾지 못했습니다.')

if __name__ == "__main__":
    # zip 파일의 경로를 지정합니다.
    zip_file_path = r"파이썬연습2월/06.압축파일 암호푸는 프로그램/암호.zip"
    # 암호를 찾는 함수를 호출합니다.
    crack_zip_password(zip_file_path)