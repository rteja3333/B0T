from flask import Flask, request, render_template,  redirect, url_for
from flask import make_response

# Importing whisper to control audio
import whisper
model = whisper.load_model("base")

# # Importing the question answering bot 
# from answer_generator import question_answering_bot

# Importing without memeory classification model 




app = Flask(__name__)

@app.route('/')
def index():
    global transcription_data
    
    transcription_data = None
    
    if(transcription_data=="Hi"):
        return render_template('redirect.html')        

    return render_template('saving.html',transcription="Testing")

@app.route('/upload-audio', methods=['POST'])
def upload_audio():
    
    audio_file = request.files['audio']
    # Save the audio file to a desired location
    audio_file.save('audio.wav')

    text_from_audio = model.transcribe("audio.wav")   
    transcription = text_from_audio["text"]
        
    global  reply
    
    
    transcription_data = transcription
    
    transcription_data ="Hi"
    transcription="Hi"
    reply = "test"
    
    print(" reached here ")

    
    # if(transcription_data =="Hi"):
    #     print("atleast reached here ")
    #     return redirect("http://127.0.0.1:5000/sales-order")
    
    # if transcription_data == "Hi":
    #     response = make_response(redirect(url_for('sales_order_route')))
    #     response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    #     return response

    print("why are you like this")
    return render_template('redirect.html')        
    print("Why am i like this ")
    # llm_output = question_answering_bot(transcription_data)
    
    # reply = llm_output["results"]
        
    # print(reply)
    # print(transcription)


@app.route('/transcription')
def get_transcription():
    if(transcription_data==None):
        return render_template('saving.html',transcription="Ask me anything")

    return render_template('saving.html',transcription=transcription_data, reply = reply)

@app.route('/sales-order')
def sales_order_route():
    
    # Add your logic for the sales order route here
    return render_template("salesordercreation.html")

if __name__ == '__main__':  
    app.run()