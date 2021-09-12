import streamlit as st
import os
from helper import create_spectrogram, read_audio, record, save_record
import subprocess
from speech_emotion_reco.mateo_preprocess import sound_to_number
from speech_emotion_reco.raph_data import get_array
import requests
import base64

# page conf
st.set_page_config(
    page_title="AI-motion",
    page_icon='speech_emotion_reco/data/emoji/favicon.png',
    initial_sidebar_state="auto") # collapsed

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
                    
local_css("style.css")

st.markdown(
    f"""
    <div class="container">
        <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open("speech_emotion_reco/data/emoji/logo.png", "rb").read()).decode()}">
    </div>
    """,
    unsafe_allow_html=True
)

st.text("")

title = '<b style="font-family:IBM plex sans; font-size: 25px; {text-align: center;}">Let\'s see how you feel:</b>'
st.markdown(title, unsafe_allow_html=True)

dir = 'samples/'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))    

#st.image('Ai-Motion.png', width=300)

filename = "recording"

if st.button(f"Record your voice"):
    
    record_state = st.text("Recording...")
    duration = 8  # seconds
    fs = 48000
    myrecording = record(duration, fs)
    #record_state.text(f"Saving sample as {filename}.mp3")

    path_myrecording = f"./samples/{filename}.mp3"
    #path_converted = f"./samples/{filename}.wav"

    save_record(path_myrecording, myrecording, fs)
    record_state.text(f"Voice recorded! Please wait a moment, AI-motion is analyzing your voice...")
    st.audio(read_audio(path_myrecording))
    
    url = "https://ai-motion-api-g6zof5oyea-ew.a.run.app/upload/"
    files = {'my_file': open(path_myrecording, 'rb')}
    #r= requests.post(url, files=files)
    
    #subprocess.call(['ffmpeg', '-i', path_myrecording,path_converted])  
    #url = "https://ai-motion-api-g6zof5oyea-ew.a.run.app/upload"
    #files = {'my_file': open(path_converted, 'rb')}

    #st.text(requests.post(url, files=files))
    response = requests.post(url, files=files).json()
    emotion1, proba1 = response['emotion1'][0], round(response['emotion1'][1]*100)
    emotion2, proba2 = response['emotion2'][0], round(response['emotion2'][1]*100)
    emotion3, proba3 = response['emotion3'][0], round(response['emotion3'][1]*100)
    
    title = '<b style="font-family:IBM plex sans; font-size: 25px; {text-align: center;}">You are most-likely feeling:</b>'
    st.markdown(title, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    
    with c1:
        #st.image(f'speech_emotion_reco/data/emoji/{emotion1}.png')
        st.markdown(
        f"""
        <div class="container">
        <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(f"speech_emotion_reco/data/emoji/{emotion1}.png", "rb").read()).decode()}">
        </div>
        """,
        unsafe_allow_html=True)
        st.subheader(f'{emotion1} ({proba1}%)')

    with c2:
        #st.image(f'speech_emotion_reco/data/emoji/{emotion2}.png')
        st.markdown(
        f"""
        <div class="container">
        <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(f"speech_emotion_reco/data/emoji/{emotion2}.png", "rb").read()).decode()}">
        </div>
        """, 
        unsafe_allow_html=True)
        st.subheader(f'...or {emotion2} ({proba2}%)')
        
    with c3:
        #st.image(f'speech_emotion_reco/data/emoji/{emotion3}.png')
        st.markdown(
        f"""
        <div class="container">
        <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(f"speech_emotion_reco/data/emoji/{emotion3}.png", "rb").read()).decode()}">
        </div>
        """,
        unsafe_allow_html=True)
        st.subheader(f'...or {emotion3} ({proba3}%)')

    record_state.text(f"Done!")

st.text("")
st.text("")

caption = '<smaller style="font-family:IBM plex sans; color:#8F8E9A; font-size: 15px; {text-align: center;}">This speech emotion recognition app was built by [mlorantdourte](https://github.com/mlorantdourte), [caronarthur](https://github.com/caronarthur) and [rvo1994](https://github.com/rvo1994).</smaller>'
st.markdown(caption, unsafe_allow_html=True)


    #st.caption('Check out the full project on [Github](https://github.com/caronarthur/speech_emotion_reco)')

      
    #fig = create_spectrogram(path_myrecording)
    #st.pyplot(fig)
  
    # convert mp3 to wav file
    #subprocess.call(['ffmpeg', '-i', path_myrecording,
    #         'samples/converted_to_wav_file.wav'])
    #
    #sound_number = sound_to_number("samples/converted_to_wav_file.wav")
    
    #sound_array = get_array("samples/converted_to_wav_file.wav")
    

    
    
    
    
    
    
    
    

    

    
    
    
    
    
    
    
    
