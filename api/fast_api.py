from fastapi import FastAPI
from joblib import load
from pydantic import  BaseModel
import subprocess
from speech_emotion_reco.mateo_preprocess import sound_to_number
from speech_emotion_reco.raph_data import get_array
from fastapi import FastAPI, File, UploadFile
from speech_emotion_reco.combine_models import combine_predict
import librosa 
import shutil 
import io

def convert_mp3(path_myrecording):
    # convert mp3 to wav file
    subprocess.call(['ffmpeg', '-i', path_myrecording,
             'samples/converted_to_wav_file.wav'])
    
    X_1 = sound_to_number("samples/converted_to_wav_file.wav")
    
    X_2 = get_array("samples/converted_to_wav_file.wav")
    
    return X_1, X_2

# initiate API

app = FastAPI()

@app.post("/upload/")
async def create_upload_file(file: UploadFile = File(...)):
    buf= io.BytesIO()
    with open ("sound.mp3","wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    a,b = convert_mp3("sound.mp3")
    
    prediction = combine_predict(a,b)
    return prediction
   

    
