import streamlit as st
import librosa
import glob
import os
from pydub import AudioSegment
from helper import draw_embed, create_spectrogram, read_audio, record, save_record
from pydub import AudioSegment
import subprocess
from speech_emotion_reco.mateo_preprocess import sound_to_number
from speech_emotion_reco.raph_data import get_array
import requests

dir = 'samples/'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))    

st.sidebar.image('Ai-Motion.png', width=300)

st.header("Record your own voice")

filename = "recording"

if st.button(f"Click to Record"):
    
    record_state = st.text("Recording...")
    duration = 8  # seconds
    fs = 48000
    myrecording = record(duration, fs)
    record_state.text(f"Saving sample as {filename}.mp3")

    path_myrecording = f"./samples/{filename}.mp3"

    save_record(path_myrecording, myrecording, fs)
    record_state.text(f"Done! Saved sample as {filename}.mp3")

    st.audio(read_audio(path_myrecording))

    fig = create_spectrogram(path_myrecording)
    st.pyplot(fig)
  
    # convert mp3 to wav file
    #subprocess.call(['ffmpeg', '-i', path_myrecording,
    #         'samples/converted_to_wav_file.wav'])
    #
    #sound_number = sound_to_number("samples/converted_to_wav_file.wav")
    
    #sound_array = get_array("samples/converted_to_wav_file.wav")
    
    api_file_upload_url = 'http://127.0.0.1:8000/'
    send_files = {'audioFile': ('music.mp3', path_myrecording, 'audio/mpeg')}
    r = requests.post(api_file_upload_url, files=send_files)
    
    
    
    
    
    
    
    
