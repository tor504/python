import os
from distutils.dir_util import copy_tree

def backup(source_dir, target_dir):
    try:
        # 만약 대상 디렉토리가 존재하지 않는다면 생성합니다.
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        
        # 소스 디렉토리의 내용을 대상 디렉토리로 복사합니다.
        copy_tree(source_dir, target_dir)
        print("백업이 완료되었습니다.")
    except Exception as e:
        print(f"백업 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    source_directory = input("원본 디렉토리 경로를 입력하세요: ")
    target_directory = input("대상 디렉토리 경로를 입력하세요: ")
    
    backup(source_directory, target_directory)