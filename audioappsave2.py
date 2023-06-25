from flask import Flask, request, render_template

# Importing whisper to control audio
import whisper
model = whisper.load_model("base")

# Importing the question answering bot 
from answer_generator import question_answering_bot



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('saving.html',transcription="Testing")

@app.route('/upload-audio', methods=['POST','GET'])
def upload_audio():
    
    audio_file = request.files['audio']
    # Save the audio file to a desired location
    audio_file.save('audio.wav')

    text_from_audio = model.transcribe("audio.wav")   
    transcription = text_from_audio["text"]
    
    global transcription_data, reply
    
    
    transcription_data = transcription
    llm_output = question_answering_bot(transcription_data)
    
    reply = llm_output["results"]
        
    print(reply)
    print(transcription)
    return "Audio input successful"


@app.route('/transcription')
def get_transcription():
    if(transcription_data==None):
        return render_template('saving.html',transcription="Ask me anything")
        
    

    return render_template('saving.html',transcription=transcription_data, reply = reply)

if __name__ == '__main__':  
    app.run()