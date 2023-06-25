from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('3.html')

@app.route('/upload-audio', methods=['POST'])
def upload_audio():
    audio_file = request.files['audio']
    # Save the audio file to a desired location
    audio_file.save('audio.wav')

    user_input = "text output"
    print(user_input)

    # Return the user input as the response
    return jsonify({'user_input': user_input})


if __name__ == '__main__':
    app.run(debug=True)
