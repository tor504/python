import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # 정적 폴더의 경로
    static_folder_path = os.path.join(app.root_path, 'static')
    # 정적 폴더 내의 모든 파일 목록을 가져오기
    image_files = [filename for filename in os.listdir(static_folder_path) if filename.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    # 이미지 파일 목록을 전달하여 HTML 템플릿을 렌더링
    return render_template('index2.html', image_files=image_files)

if __name__ == '__main__':
    app.run(debug=True)
