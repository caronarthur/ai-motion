import pandas as pd
import numpy as np
import os
import seaborn as sns
import librosa
from data import merge_data

## pay attention to the path it can change, depends where you're running the code.
def saving_spect_image(path, image_id):
    emotion_df = merge_data()
    fig = plt.figure()
    data, sample_rate = librosa.load(path)
    fourier = librosa.stft(data)
    amp = librosa.amplitude_to_db(abs(fourier))
    librosa.display.specshow(amp, sr=sample_rate, x_axis="time", y_axis="log")
    plt.axis('off')
    filename = "../speech_emotion_reco/data/images/"+image_id
    plt.savefig(filename)
    plt.close()
    del filename, data, sample_rate,fourier, fig




