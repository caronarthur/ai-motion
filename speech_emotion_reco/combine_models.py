from tensorflow.keras.models import load_model
import joblib
from speech_emotion_reco.raph_data import get_array
from speech_emotion_reco.mateo_preprocess import sound_to_number
import pandas as pd

def combine_predict(X_1, X_2):

    model_1= joblib.load("../models/mlp_model.joblib")
    model_2= load_model("../models/CNN_model.hdf5")
    proba1= pd.DataFrame(model_1.predict_proba(X_1))
    proba2= pd.DataFrame(model_2.predict(X_2))

    proba1.rename(columns={0: "angry", 1: "disgust",2:"fear",3:"happy",4:"neutral",5:"sad"}, inplace=True)
    proba2.rename(columns={0: "happy", 1: "sad",2:"fear",3:"disgust",4:"angry",5:"neutral"}, inplace=True)
    
    combined_proba= proba1+proba2

    emotion_predict=combined_proba[['angry','disgust','fear',"happy",'neutral','sad']].idxmax(axis=1)
    
    return emotion_predict


