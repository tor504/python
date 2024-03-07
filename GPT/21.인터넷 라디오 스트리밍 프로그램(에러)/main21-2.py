from flask import Flask, render_template, request

app = Flask(__name__)

# Define questions for the MBTI test
questions = [
    "I am a social person and enjoy being around others.",
    "I often focus on the present moment rather than thinking about the future.",
    "I prefer to plan my activities rather than being spontaneous.",
    "I am more analytical and logical than emotional.",
    "I enjoy new experiences and am open to trying new things.",
    "I prefer to spend time alone rather than in large groups.",
    "I am organized and like to keep things neat and tidy.",
    "I am more of a practical person than a dreamer.",
]

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

@app.route('/result', methods=['POST'])
def result():
    answers = [request.form.get(f'q{i}') for i in range(1, len(questions) + 1)]
    # Calculate MBTI personality type based on user's answers
    personality_type = calculate_mbti_score(answers)
    return render_template('result.html', personality_type=personality_type)

def calculate_mbti_score(answers):
    # Implement MBTI score calculation logic here
    # This function will calculate the MBTI personality type based on the user's answers
    # You can use the same logic as in previous examples

if __name__ == '__main__':
    app.run(debug=True)