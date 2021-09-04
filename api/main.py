from fastapi import FastAPI
from joblib import load
from pydantic import  BaseModel
import subprocess
from ..speech_emotion_reco.mateo_preprocess import sound_to_number
from ..speech_emotion_reco.raph_data import get_array
from fastapi import FastAPI, File, UploadFile
from ..speech_emotion_reco.combine_models import combine_predict


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
def create_upload_file(file: UploadFile = File(...)):
    a,b = convert_mp3(file.file)
    
    prediction = combine_predict(a,b)
    return prediction