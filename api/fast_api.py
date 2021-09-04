from fastapi import FastAPI
from joblib import load
from pydantic import  BaseModel
import subprocess
from speech_emotion_reco.mateo_preprocess import sound_to_number
from speech_emotion_reco.raph_data import get_array
from fastapi import FastAPI, File, UploadFile
import librosa 


# load model
clf = load('/model/model_1.joblib')

def convert_mp3(path_myrecording):
    # convert mp3 to wav file
    subprocess.call(['ffmpeg', '-i', path_myrecording,
             'samples/converted_to_wav_file.wav'])
    
    sound_number = sound_to_number("samples/converted_to_wav_file.wav")
    
    sound_array = get_array("samples/converted_to_wav_file.wav")
    
    return sound_array, sound_number

def get_prediction(param1, param2):
    
    x = [[param1, param2]]

    y = clf.predict(x)[0]  # just get single value
    prob = clf.predict_proba(x)[0].tolist()  # send to list for return

    return {'prediction': int(y), 'probability': prob}


# initiate API

app = FastAPI()

@app.post("/upload/")
async def create_upload_file(file: UploadFile = File(...)):
    a,b = convert_mp3(file.file)
    return a,b

if __name__ == "__main__":
    # load model
    model = load_model("trained_heartbeat_classifier.h5")

classify_file = sys.argv[1]
x_test = []
x_test.append(create_upload_file(classify_file, 0.5))
x_test = np.asarray(x_test)
x_test = x_test.reshape(x_test.shape[0], x_test.shape[1], x_test.shape[2], 1)
pred = model.predict(x_test, verbose=1)
# print(pred)

pred_class = model.predict_classes(x_test)
if pred_class[0]:
    print("\nNormal heartbeat")
    print("confidence:", pred[0][1])
else:
    print("\nAbnormal heartbeat")
    print("confidence:", pred[0][0])