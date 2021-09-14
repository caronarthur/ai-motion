import requests

url = "https://ai-motion-api-g6zof5oyea-ew.a.run.app/upload/"
files = {'my_file': open("speech_emotion_reco/data/crema/1001_DFA_ANG_XX.wav", 'rb')}
r= requests.post(url, files=files)
print(r.json())

