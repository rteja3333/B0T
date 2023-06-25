from flask import Flask, request, render_template, redirect, url_for

# Importing whisper to control audio
import whisper
model = whisper.load_model("base")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('saving.html', transcription="Testing")

@app.route('/upload-audio', methods=['POST'])
def upload_audio():
    audio_file = request.files['audio']
    # Save the audio file to a desired location
    audio_file.save('audio.wav')

    text_from_audio = model.transcribe("audio.wav")
    transcription = text_from_audio["text"]

    global transcription_data
    transcription_data = transcription
    
    transcription = "create sales order"
    
    if transcription == "create sales order":
        return redirect(url_for('sales_order_route'))

    return redirect(url_for('get_transcription'))

@app.route('/transcription')
def get_transcription():

    return render_template('saving.html', transcription=transcription_data)


@app.route('/sales-order')
def sales_order_route():
    # Add your logic for the sales order route here
    return render_template("salesordercreation.html")


if __name__ == '__main__':
    app.run()
