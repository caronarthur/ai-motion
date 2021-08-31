import joblib
from termcolor import colored
from speech_emotion_reco.data import get_data_from_gcp, merge_data
#from speech_emotion_reco.encoders import TimeFeaturesEncoder, DistanceTransformer
from speech_emotion_reco.gcp import storage_upload
from speech_emotion_reco.params import MLFLOW_URI, EXPERIMENT_NAME, BUCKET_NAME, MODEL_VERSION, MODEL_VERSION
import pandas as pd

class Trainer(object):
    def __init__(self, X, y):
        self.pipeline = None
        self.X = X
        self.y = y
        
    def set_pipeline(self):
        """defines the pipeline as a class attribute"""
        pass
    
    def run(self):
        self.set_pipeline()
        self.mlflow_log_param("model", "Linear")
        self.pipeline.fit(self.X, self.y)
        
    def save_model_locally(self):
        """Save the model into a .joblib format"""
        joblib.dump(self.pipeline, 'model.joblib')
        print(colored("model.joblib saved locally", "green"))
        
if __name__ == "__main__":
    # Get and clean data
    #df = get_data_from_gcp()
    df = merge_data()
    df.to_csv('data/test.csv')
    print("csv created")
"""    df = clean_data(df)
    y = df["fare_amount"]
    X = df.drop("fare_amount", axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    trainer = Trainer(X=X_train, y=y_train)
    trainer.run()
    trainer.save_model_locally()
    storage_upload()"""