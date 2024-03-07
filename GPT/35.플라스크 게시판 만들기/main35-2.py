from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

# static 폴더 경로
static_folder = os.path.join(app.root_path, 'static')

# 게시글을 저장할 파일 경로
post_file = os.path.join(static_folder, 'posts.txt')

# 기존 게시글을 불러오는 함수
def load_posts():
    try:
        with open(post_file, 'r', encoding='utf-8') as file:
            posts = file.readlines()
    except FileNotFoundError:
        posts = []
    return posts

# 게시글을 파일에 저장하는 함수
def save_post(content):
    with open(post_file, 'a', encoding='utf-8') as file:
        file.write(content + '\n')

# 홈페이지 렌더링
@app.route('/')
def index():
    posts = load_posts()
    return render_template('index.html', posts=posts)

# 게시글 추가
@app.route('/add_post', methods=['POST'])
def add_post():
    content = request.form['content']
    save_post(content)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
