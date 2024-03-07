import os
import cv2
from mtcnn import MTCNN

def detect_and_mosaic_faces(image_path):
    # 이미지 읽기
    image = cv2.imread(image_path)
    # MTCNN 모델 로드
    detector = MTCNN()
    # 얼굴 검출
    faces = detector.detect_faces(image)
    
    # 얼굴에 대해 모자이크 처리
    for face in faces:
        x, y, w, h = face['box']
        # 모자이크 처리
        face_image = image[y:y+h, x:x+w]
        face_image = cv2.GaussianBlur(face_image, (99, 99), 30)
        # 모자이크된 얼굴을 원래 이미지에 삽입
        image[y:y+h, x:x+w] = face_image

    return image

def process_images_in_folder(folder_path):
    # 폴더 내 모든 파일에 대해 처리
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg"):
            # 파일 경로
            file_path = os.path.join(folder_path, filename)
            # 얼굴 감지 및 모자이크 처리
            processed_image = detect_and_mosaic_faces(file_path)
            # 파일명 수정
            new_filename = "modify_" + filename
            new_file_path = os.path.join(folder_path, new_filename)
            # 모자이크 처리된 이미지 저장
            cv2.imwrite(new_file_path, processed_image)
            print(f"Processed: {filename} -> {new_filename}")

if __name__ == "__main__":
    folder_path = "."  # 현재 폴더
    process_images_in_folder(folder_path)
