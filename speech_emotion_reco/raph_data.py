import librosa
import librosa.display
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image
import io

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
    
