import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import io
from google.cloud import storage
from tensorflow.keras.models import load_model
import joblib
import pandas as pd

def get_array(audio_file):
    data, sample_rate = librosa.load(audio_file, sr=44100)
    fig = plt.figure
    sgram = librosa.stft(data)
    sgram_mag, _ = librosa.magphase(sgram)
    sample_rate = 44100
    mel_scale_sgram = librosa.feature.melspectrogram(S=sgram_mag, sr=sample_rate)
    mel_sgram = librosa.amplitude_to_db(mel_scale_sgram, ref=np.min)
    librosa.display.specshow(mel_sgram, sr=sample_rate, x_axis='time', y_axis='mel')
    plt.axis('off') 
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image = Image.open(buf).convert('RGB') 
    resized_image = image.resize((256,256))
    X_sample = np.array(resized_image)
    X_sample = np.expand_dims(X_sample, axis = 0)
    return X_sample 
    
def sound_to_number(sound):

    data, sample_rate = librosa.load(sound, duration=2.5, offset=0.6)
    result = np.array([])
    zcr = np.mean(librosa.feature.zero_crossing_rate(y=data).T, axis=0)
    result = np.hstack((result, zcr)) # stacking horizontally

    # Chroma_stft
    stft = np.abs(librosa.stft(data))
    chroma_stft = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T, axis=0)
    result = np.hstack((result, chroma_stft)) # stacking horizontally

    # MFCC
    mfcc = np.mean(librosa.feature.mfcc(y=data, sr=sample_rate).T, axis=0)
    result = np.hstack((result, mfcc)) # stacking horizontally
    
    # Root Mean Square Value
    rms = np.mean(librosa.feature.rms(y=data).T, axis=0)
    result = np.hstack((result, rms)) # stacking horizontally

    # MelSpectogram
    mel = np.mean(librosa.feature.melspectrogram(y=data, sr=sample_rate).T, axis=0)
    result = np.hstack((result, mel)) # stacking horizontally
    
    return result

def download_blob():
    """Downloads a blob."""
    client = storage.Client().bucket('ai-motion-bucket')
    
    storage_location_1 = 'mlp_model.joblib'
    blob = client.blob(storage_location_1)
    blob.download_to_filename('models/model.joblib')
    
    storage_location_2 = 'CNN_model.hdf5'
    blob = client.blob(storage_location_2)
    blob.download_to_filename('models/CNN_model.hdf5')
    
def combine_predict(X_1, X_2):
    X_1 = pd.DataFrame(X_1)

    download_blob()
    model_1 = joblib.load("models/mlp_model.joblib")
    model_2 = load_model("models/CNN_model.hdf5")
    proba1 = pd.DataFrame(model_1.predict_proba(X_1.T))
    proba2 = pd.DataFrame(model_2.predict(X_2))

    proba1.rename(columns={0: "angry", 1: "disgust",2: "fear",3: "happy",4: "neutral",5: "sad"}, inplace=True)
    proba2.rename(columns={0: "happy", 1: "sad",2: "fear",3: "disgust",4: "angry",5: "neutral"}, inplace=True)
    
    combined_proba = (proba1+proba2)/2
    combined_proba.sort_values(by=0,ascending=False, axis=1, inplace=True)
    proba_first_three= combined_proba.iloc[:,0:3]
    proba_dict = {"emotion1":[proba_first_three.columns[0],proba_first_three.iloc[0,0]],
                  "emotion2":[proba_first_three.columns[1],proba_first_three.iloc[0,1]],
                  "emotion3":[proba_first_three.columns[2],proba_first_three.iloc[0,2]]}
    
    return proba_dict

def convert_wav(path_myrecording):
    X_1 = sound_to_number(path_myrecording)
    X_2 = get_array(path_myrecording)
    
    return X_1, X_2
  



