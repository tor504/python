import cv2
from mtcnn import MTCNN

def detect_face(image_path):
    # 이미지 읽기
    image = cv2.imread(image_path)
    # MTCNN 모델 로드
    detector = MTCNN()
    # 얼굴 검출
    faces = detector.detect_faces(image)
    
    # 각 얼굴에 대해 모자이크 처리
    for face in faces:
        x, y, w, h = face['box']
        # 모자이크 처리
        face_image = image[y:y+h, x:x+w]
        face_image = cv2.GaussianBlur(face_image, (99, 99), 30)
        # 모자이크된 얼굴을 원래 이미지에 삽입
        image[y:y+h, x:x+w] = face_image

    return image

def save_image(image, output_path):
    # 이미지 저장
    cv2.imwrite(output_path, image)

if __name__ == "__main__":
    # 입력 이미지 경로
    input_image_path = "input_image.jpg"
    # 출력 이미지 경로
    output_image_path = "output_image.jpg"

    # 얼굴 감지 및 모자이크 처리
    processed_image = detect_face(input_image_path)
    # 모자이크 처리된 이미지 저장
    save_image(processed_image, output_image_path)
