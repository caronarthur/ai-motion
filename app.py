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
    page_icon='speech_emotion_reco/data/emoji/favicon.png',
    layout="centered", # wide
    initial_sidebar_state="auto") # collapsed


st.image('speech_emotion_reco/data/emoji/logo.png')

title = '<b style="font-family:IBM plex sans; color:#EB7B67; font-size: 40px; {text-align: left;}">Let me detect how you feel:</b>'
st.markdown(title, unsafe_allow_html=True)

dir = 'samples/'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))    

#st.image('Ai-Motion.png', width=300)

st.text("")

filename = "recording"

if st.button(f"Click to record your voice"):
    
    record_state = st.text("Recording...")
    duration = 1  # seconds
    fs = 48000
    myrecording = record(duration, fs)
    #record_state.text(f"Saving sample as {filename}.mp3")

    path_myrecording = f"./samples/{filename}.mp3"

    save_record(path_myrecording, myrecording, fs)
    record_state.text(f"Voice recorded! Please wait a moment, AI-motions is analyzing your voice...")
    st.text("")
    st.audio(read_audio(path_myrecording))
    st.text("")
    
    api_file_upload_url = 'http://127.0.0.1:8000/'
    send_files = {'audioFile': ('music.mp3', path_myrecording, 'audio/mpeg')}
    response = requests.post(api_file_upload_url, files=send_files)
    emotion1, proba1 = response['emotion1'][0], round(response['emotion1'][1],2)*100
    emotion2, proba2 = response['emotion2'][0], round(response['emotion2'][1],2)*100
    emotion3, proba3 = response['emotion3'][0], round(response['emotion3'][1],2)*100
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.image(f'speech_emotion_reco/data/emoji/{emotion1}.png')
        st.subheader(f'{emotion1} ({proba1}%)')

    with c2:
        st.image(f'speech_emotion_reco/data/emoji/{emotion2}.png')
        st.subheader(f'...or {emotion2} ({proba2}%)')
        
    with c3:
        st.image(f'speech_emotion_reco/data/emoji/{emotion3}.png')
        st.subheader(f'...or {emotion3} ({proba3}%)')
            
    record_state.text(f"Done!")

st.text("")
st.text("")
st.text("") 

#caption = '<p style="font-family:IBM plex sans; color:Grey; font-size: 10px; {text-align: center;}">This speech emotion recognition app was built by [mlorantdourte](https://github.com/mlorantdourte), [caronarthur](https://github.com/caronarthur) and [rvo1994](https://github.com/rvo1994)</p>'
#caption = <a href="https://www.w3schools.com/">Visit W3Schools.com!</a>

#st.markdown(caption, unsafe_allow_html=True)

st.caption('This speech emotion recognition app was built by [mlorantdourte](https://github.com/mlorantdourte), [caronarthur](https://github.com/caronarthur) and [rvo1994](https://github.com/rvo1994)')

    #st.caption('Check out the full project on [Github](https://github.com/caronarthur/speech_emotion_reco)')

      
    #fig = create_spectrogram(path_myrecording)
    #st.pyplot(fig)
  
    # convert mp3 to wav file
    #subprocess.call(['ffmpeg', '-i', path_myrecording,
    #         'samples/converted_to_wav_file.wav'])
    #
    #sound_number = sound_to_number("samples/converted_to_wav_file.wav")
    
    #sound_array = get_array("samples/converted_to_wav_file.wav")
    

    
    
    
    
    
    
    
    
