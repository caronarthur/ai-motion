FROM python:3.8.6-buster

COPY api /api
COPY models /models
#COPY samples /samples
COPY speech_emotion_reco/__init__.py /speech_emotion_reco/__init__.py
COPY speech_emotion_reco/utils.py /speech_emotion_reco/utils.py

COPY requirements.txt /requirements.txt
RUN apt-get update && apt-get upgrade -y && apt-get install -y && apt-get -y install apt-utils gcc libpq-dev libsndfile1-dev
RUN pip install -r requirements.txt

CMD uvicorn api.fast_api:app --host 0.0.0.0 --port $PORT