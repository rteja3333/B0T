# # Functions using NLP, *** Will slow down the system **** ::
# from agentwithoutmemory import classify_input
# from answer_generator import question_answering_bot


from flask import Flask, request, render_template, jsonify
import requests

import whisper
import os



questions = []  # List to store the submitted questions

app = Flask(__name__)

@app.route('/')
def homepage():
    print("This is working")
    return render_template('2.html')



# @app.route('/submit', methods=['POST'])
# def submit_question():
#     print("Not even reaching this line")
#     question = request.form.get('question')  # Get the submitted question from the form
#     questions.append(question)  # Add the question to the beginning of the list
    
#     print("This works now")
#     print(question)

    
#     return render_template('1.html', questions=questions)


# @app.route('/speech-recognition', methods=['POST'])
# def speech_recognition():
    
#     audio_url = request.form.get('audioUrl')

#     # Save the audio file locally
#     audio_path = 'audio.wav'
#     # subprocess.run(['curl', '-o', audio_path, audio_url])
#     os.system(f'curl -o {audio_path} {audio_url}')

#     # # Perform speech recognition using Whisper locally
#     # whisper_command = ['whisper', 'recognize', audio_path]
#     # recognized_text = subprocess.check_output(whisper_command).decode().strip()

#     # # Delete the temporary audio file
#     # os.remove(audio_path)
    
#     recognized_text = "Test-1"

#     return jsonify({'recognizedText': recognized_text})


@app.route('/save-audio', methods=['POST'])
def save_audio():
    audio = request.files['audio']
    audio.save('recording.wav')
    return 'Audio saved successfully'

if __name__ == '__main__':
    app.run()
    
    
    # category = classify_input(question)
    # json_data = category[0]

    # value = json_data
    # answer = None  # Initialize answer with a default value

    # if value == "Q&A":
    #     answer = question_answering_bot(input_question=question)
    #     print("\n\n\n")
    #     print(answer["results"])
    #     print("\n\n\n")
    # else:
    #     answer = "Sorry unable to help !"
        
    # print(question)
    # print(answer)
    


# @app.route('/process', methods=['POST'])
# def process_form():
#     question = request.form.get('question')  # Get the value of the 'question' field from the form
#     print(question)

#     # category = classify_input(question)
#     # json_data = category[0]

#     # value = json_data
#     # answer = None  # Initialize answer with a default value

#     # if value == "Q&A":
#     #     answer = question_answering_bot(input_question=question)
#     #     print("\n\n\n")
#     #     print(answer["results"])
#     #     print("\n\n\n")
#     # else:
#     #     answer = "Sorry unable to help !"
    
#     return jsonify({'question': question})