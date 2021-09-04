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


# page conf
st.set_page_config(
    page_title="AI-motion",
    page_icon='speech_emotion_reco/data/emoji/robot.png',
    layout="centered", # wide
    initial_sidebar_state="auto") # collapsed

dir = 'samples/'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))    

#st.image('Ai-Motion.png', width=300)

st.image('speech_emotion_reco/data/emoji/robot.png')
st.header("AI-motion will predict how you feel:")
st.text("")

filename = "recording"

if st.button(f"Click to record your voice"):
    
    record_state = st.text("Recording...")
    duration = 8  # seconds
    fs = 48000
    myrecording = record(duration, fs)
    #record_state.text(f"Saving sample as {filename}.mp3")

    path_myrecording = f"./samples/{filename}.mp3"

    save_record(path_myrecording, myrecording, fs)
    record_state.text(f"Voice recorded!")
    st.text("")
    st.audio(read_audio(path_myrecording))
    st.text("")
    st.subheader("You are most-likely feeling...")
    st.text("")
    
    c1, c2, c3 = st.columns(3)
    
    c1.image('speech_emotion_reco/data/emoji/sad.png')

    with c2:
        st.image('speech_emotion_reco/data/emoji/happy.png')

    c3.image('speech_emotion_reco/data/emoji/disgust.png')     

    c1.subheader("sad (78%)")

    with c2:
        st.subheader("happy (23%)")

    c3.subheader("disgust (10%)")  
    
st.text("") 
st.text("") 
st.text("")
st.text("") 
st.caption('This speech emotion recognition app was built by [mlorantdourte](https://github.com/mlorantdourte), [caronarthur](https://github.com/caronarthur/speech_emotion_reco/commits?author=caronarthur) and [rvo1994](https://github.com/rvo1994)')
#st.caption('Check out the full project on [Github](https://github.com/caronarthur/speech_emotion_reco)')

      
    #fig = create_spectrogram(path_myrecording)
    #st.pyplot(fig)
  
    # convert mp3 to wav file
    #subprocess.call(['ffmpeg', '-i', path_myrecording,
    #         'samples/converted_to_wav_file.wav'])
    #
    #sound_number = sound_to_number("samples/converted_to_wav_file.wav")
    
    #sound_array = get_array("samples/converted_to_wav_file.wav")
    
    #api_file_upload_url = 'http://127.0.0.1:8000/'
    #send_files = {'audioFile': ('music.mp3', path_myrecording, 'audio/mpeg')}
    #r = requests.post(api_file_upload_url, files=send_files)
    
    
    
    
    
    
    
    
