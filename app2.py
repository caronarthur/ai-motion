import streamlit as st
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
        <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open("images/logo.png", "rb").read()).decode()}">
    </div>
    """,
    unsafe_allow_html=True
)

st.text("")

title = '<b style="font-family:IBM plex sans; color:#EB7B67; font-size: 25px; {text-align: center;}">Let\'s see how you feel:</b>'
st.markdown(title, unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload Files",type=['wav'])

if uploaded_file is not None:
    files = {'my_file': uploaded_file}
    url = "https://ai-motion-api-g6zof5oyea-ew.a.run.app/upload/"
    st.audio(uploaded_file)
    response = requests.post(url, files=files).json()
    emotion1, proba1 = response['emotion1'][0], round(response['emotion1'][1]*100)
    emotion2, proba2 = response['emotion2'][0], round(response['emotion2'][1]*100)
    emotion3, proba3 = response['emotion3'][0], round(response['emotion3'][1]*100)
    title = '<b style="font-family:IBM plex sans; color:#EB7B67; font-size: 25px; {text-align: center;}">You are most-likely feeling:</b>'
    st.markdown(title, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)  
    
    with c1:
        #st.image(f'speech_emotion_reco/data/emoji/{emotion1}.png')
        st.markdown(
        f"""
        <div class="container">
        <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(f"images/{emotion1}.png", "rb").read()).decode()}">
        </div>
        """,
        unsafe_allow_html=True)
        st.subheader(f'{emotion1} ({proba1}%)')

    with c2:
        #st.image(f'speech_emotion_reco/data/emoji/{emotion2}.png')
        st.markdown(
        f"""
        <div class="container">
        <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(f"images/{emotion2}.png", "rb").read()).decode()}">
        </div>
        """, 
        unsafe_allow_html=True)
        st.subheader(f'...or {emotion2} ({proba2}%)')
        
    with c3:
        #st.image(f'speech_emotion_reco/data/emoji/{emotion3}.png')
        st.markdown(
        f"""
        <div class="container">
        <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(f"images/{emotion3}.png", "rb").read()).decode()}">
        </div>
        """,
        unsafe_allow_html=True)
        st.subheader(f'...or {emotion3} ({proba3}%)')

st.text("")
st.text("")

caption = '<smaller style="font-family:IBM plex sans; color:#8F8E9A; font-size: 15px; {text-align: center;}">This speech emotion recognition app was built by [mlorantdourte](https://github.com/mlorantdourte), [caronarthur](https://github.com/caronarthur) and [rvo1994](https://github.com/rvo1994).</smaller>'
st.markdown(caption, unsafe_allow_html=True)

    
    