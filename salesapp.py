from flask import Flask, request, render_template

# Importing whisper to control audio
import whisper
model = whisper.load_model("base")

# # Importing the question answering bot 
# from answer_generator import question_answering_bot

from createsalesorder import SalesOrder

new_order =  SalesOrder()


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('sales.html',transcription="Testing")

@app.route('/upload-audio', methods=['POST','GET'])
def upload_audio():
    
    audio_file = request.files['audio']
    # Save the audio file to a desired location
    audio_file.save('audio.wav')

    text_from_audio = model.transcribe("audio.wav")   
    transcription = text_from_audio["text"]
    
    global transcription_data
    
    
    transcription_data = transcription
    # llm_output = question_answering_bot(transcription_data)
    
    # reply = llm_output["results"]
        
    # print(reply)
    print(transcription)
    return "Audio input successful"


@app.route('/transcription')
def get_transcription():
    
    global new_order
    
    if(transcription_data==None):
        return render_template('sales.html',transcription="Ask me anything")
        
    # Sales order creation steps : 
    
    transcript_1 = "Sure, Let me help you in creating a sales order; I need some information regarding it, Can you provide me the details of the order type, Sales organizaiton and the Distribution Channel : "
    transcript_2 = "Great, I now need the details of the Sold-to-Party, Ship-to-Party and PO-reference-Number :  "
    transcript_3 = "Great, I finally need the order quantity, Material, Plant and Storage location so that I can start creating the order :  "

    return render_template('sales.html',transcription=transcript_1, sales_order = new_order)

if __name__ == '__main__':  
    app.run()