from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile
from speech_emotion_reco.utils import combine_predict, convert_wav
import shutil 
import io

app = FastAPI()

@app.post("/upload/")
async def create_upload_file(my_file: UploadFile = File(...)):
    buf = io.BytesIO()
    with open("sound.wav","wb") as buffer:
        shutil.copyfileobj(my_file.file, buffer)
    
    a,b = convert_wav("sound.wav")
    
    prediction = combine_predict(a,b)
    return prediction


