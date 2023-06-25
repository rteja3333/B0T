from flask import Flask, request, render_template, Response
from agentwithoutmemory import classify_input
from answer_generator import question_answering_bot

app = Flask(__name__)

def generate_answers(question):
    for answer in question_answering_bot(input_question=question):
        yield f'Answer: {answer}\n'

@app.route('/')
def homepage():
    return render_template('streaming.html')

@app.route('/process', methods=['POST'])
def process_form():
    question = request.form.get('question')

    category = classify_input(question)
    json_data = category[0]
    value = json_data

    if value == "Q&A":
        return Response(generate_answers(question), mimetype='text/plain')

if __name__ == '__main__':
    app.run()
