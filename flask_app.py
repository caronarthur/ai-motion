from flask import Flask, render_template, request
from helper import create_spectrogram, read_audio, record, save_record

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def frontend():
    if request.method == 'POST':
        if request.form.get('action1') == 'Click to record your voice':
            duration = 8
            fs = 48000
            myrecording = record(duration, fs)
            path_myrecording = f"./samples/{filename}.mp3"
            save_record(path_myrecording, myrecording, fs)
            url = "http://127.0.0.1:8000/upload"
            files = {'my_file': open(path_myrecording, 'rb')}
            response = requests.post(url, files=files).json()
            emotion1, proba1 = response['emotion1'][0], round(response['emotion1'][1]*100)
            emotion2, proba2 = response['emotion2'][0], round(response['emotion2'][1]*100)
            emotion3, proba3 = response['emotion3'][0], round(response['emotion3'][1]*100)
            print(emotion1)
            
    return render_template('content.html')

    
if __name__ == "__main__":
    app.run(debug=True)
