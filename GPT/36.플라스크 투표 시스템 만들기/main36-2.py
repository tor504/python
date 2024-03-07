from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

# 예시 후보자 정보
candidates = [
    {"name": "Candidate 1", "votes": 10},
    {"name": "Candidate 2", "votes": 15},
    {"name": "Candidate 3", "votes": 8}
]

@app.route('/')
def index():
    return render_template('index2.html', candidates=candidates)

@app.route('/graph')
def graph():
    # 후보자 정보를 데이터프레임으로 변환
    df = pd.DataFrame(candidates)

    # 그래프 생성
    plt.bar(df['name'], df['votes'])
    plt.xlabel('Candidates')
    plt.ylabel('Votes')
    plt.title('Voting Results')

    # 그래프를 이미지로 변환하여 base64로 인코딩
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()

    return render_template('graph.html', graph_url=graph_url)

if __name__ == '__main__':
    app.run(debug=True)
