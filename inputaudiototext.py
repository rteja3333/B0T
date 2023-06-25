import whisper

def converttotext():
    
    model = whisper.load_model("tiny")
    result = model.transcribe("audio.wav")
    return result["text"]



# # Testing:
# result  = converttotext()
# print(result)
        