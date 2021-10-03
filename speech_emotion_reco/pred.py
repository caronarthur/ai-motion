from speech_emotion_reco.utils import combine_predict, convert_wav
import os
from pydub import AudioSegment
from pydub.utils import make_chunks

def get_emotions_over_time(file_path):
    """"takes the path of a wav file as input, slides the wav file into chunks of 8 seconds and return a dictionary
    containing a prediction of the emotion (top 3 with probability) for every chunk"""
    myaudio = AudioSegment.from_file(file_path, "wav") 
    chunk_length_ms = 8000 # pydub calculates in millisec
    chunks = make_chunks(myaudio, chunk_length_ms) # make chunks of ten seconds
    emotions = {}
    # export all of the individual chunks as wav files
    for i, chunk in enumerate(chunks):
        chunk_name = "chunks/chunk{0}.wav".format(i)
        print(f"exporting {chunk_name}")
        chunk.export(chunk_name, format="wav")
    chunks = os.listdir('chunks')
    for index, path in enumerate(chunks):
            a,b = convert_wav(f'chunks/{path}')
            pred = combine_predict(a,b)
            emotions[index] = pred
            os.remove(f'chunks/{path}')
    return emotions

if __name__ == "__main__":
    path = 'speech_emotion_reco/data/test.wav'
    print(get_emotions_over_time(path))
