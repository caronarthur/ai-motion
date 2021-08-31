import streamlit as st
import librosa
import glob
import os
from pydub import AudioSegment
from ffprobe import FFProbe
from helper import draw_embed, create_spectrogram, read_audio, record, save_record

dir = 'samples/'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))    

st.sidebar.image('Ai-Motion.png', width=300)

st.header("Record your own voice")

filename = st.text_input("Choose a filename: ")

if st.button(f"Click to Record"):
    if filename == "":
        st.warning("Choose a filename.")
    else:
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
        
        # convert wav to mp3                                                            
        sound = AudioSegment.from_mp3(path_myrecording)
        sound.export("/samples/file.wav", format="wav")
        
        
