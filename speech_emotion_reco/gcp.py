from google.cloud import storage

def download_blob():
    """Downloads a blob."""
    client = storage.Client().bucket('ai-motion-bucket')
    
    storage_location_1 = 'mlp_model.joblib'
    blob = client.blob(storage_location_1)
    blob.download_to_filename('models/model.joblib')
    
    storage_location_2 = 'CNN_model.hdf5'
    blob = client.blob(storage_location_2)
    blob.download_to_filename('models/CNN_model.hdf5')
    

    
