from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# 게시글을 저장할 리스트
posts = []

@app.route('/')
def home():
    return render_template('index.html', posts=posts)

@app.route('/add_post', methods=['POST'])
def add_post():
    # POST 요청으로부터 게시글 내용을 받아옴
    content = request.form['content']
    # 받아온 내용을 게시글 리스트에 추가
    posts.append(content)
    # 홈페이지로 리다이렉트
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
