import pandas as pd
import numpy as np
import os 
import seaborn as sns
import librosa
import librosa.display

#get the data from a sound 
def get_data(file):
    data, sampling_rate = librosa.load(file)
    return data


# Create functions to import each dataset
def create_data_savee():
    savee="data/savee/"
    list_files_savee= os.listdir(savee)
    emotion_savee=[]
    path_savee=[]
    for file in list_files_savee:
        if file[2:4]=="_a":
            emotion_savee.append('angry')
        elif file[2:4]=="_d":
            emotion_savee.append('disgust')
        elif file[2:4]=="_f":
            emotion_savee.append('fear')
        elif file[2:4]=="_h":
            emotion_savee.append('happy')
        elif file[2:4]=="_n":
            emotion_savee.append('neutral')
        elif file[2:5]=="_sa":
            emotion_savee.append('sad')
        elif file[2:5]=="_su":
            emotion_savee.append('surprise')
        else:
            emotion_savee.append('unknown')
        path_savee.append(savee+file)

    # create data frame
    savee_df= pd.DataFrame(emotion_savee, columns=["emotion"])
    savee_df= pd.concat([savee_df, pd.DataFrame(path_savee, columns=["path"])],axis=1)    
    savee_df.insert(0, 'gender', 'male')
    savee_df['duration'] = savee_df['path'].apply(get_data).apply(librosa.get_duration)
    return savee_df

def create_data_ravdess():
    ravdess= "data/ravdess/"
    list_files_ravdess= os.listdir(ravdess)
    emotion_ravdess=[]
    gender_ravdess=[]
    path_ravdess=[]

    for file in list_files_ravdess:
        part=file.split('.')[0].split('-')
        emotion_ravdess.append(int(part[2]))
        gend= int(part[6])
        if gend%2==0:
            gend="female"
        else:
            gend="male"
        gender_ravdess.append(gend)
        path_ravdess.append(ravdess+file)
    ravdess_df= pd.DataFrame(emotion_ravdess)
    dict_emotions={1:'neutral', 2:'neutral', 3:'happy', 4:'sad', 5:'angry', 6:'fear', 7:'disgust', 8:'surprise'}
    ravdess_df.replace(dict_emotions, inplace= True)
    ravdess_df= pd.concat([pd.DataFrame(gender_ravdess), ravdess_df], axis=1)
    ravdess_df.columns=["gender","emotion"]
    ravdess_df=pd.concat([ravdess_df, pd.DataFrame(path_ravdess, columns=["path"])], axis=1)
    ravdess_df['duration'] = ravdess_df['path'].apply(get_data).apply(librosa.get_duration)
    return ravdess_df

def create_data_tess():
    tess= "data/tess/"
    list_files_tess= os.listdir(tess)
    emotion_tess=[]
    path_tess=[]

    for directory in list_files_tess:
        file_name_3=os.listdir(tess+directory)
        for file in file_name_3:
            if directory=="OAF_angry" or directory=="YAF_angry":
                emotion_tess.append("female_angry")
            elif directory=="OAF_disgust" or directory=="YAF_disgust":
                emotion_tess.append("female_disgust")
            elif directory=="OAF_Fear" or directory=="YAF_fear":
                emotion_tess.append("female_fear")
            elif directory=="OAF_happy" or directory=="YAF_happy":
                emotion_tess.append("female_happy")
            elif directory=="OAF_neutral" or directory=="YAF_neutral":
                emotion_tess.append("female_neutral")
            elif directory=="OAF_Pleasant_surprise" or directory=="YAF_pleasant_surprise":
                emotion_tess.append("female_surprise")
            elif directory=="OAF_Sad" or directory=="YAF_sad":
                emotion_tess.append("female_sad")
            else:
                emotion_tess.append("Unknown")
            path_tess.append(tess+directory+"/"+file)
    tess_df= pd.DataFrame(emotion_tess, columns=["emotion"])
    tess_df= pd.concat([tess_df, pd.DataFrame(path_tess, columns=["path"])], axis=1)
    tess_df.insert(0, 'gender', 'female')
    tess_df['duration'] = tess_df['path'].apply(get_data).apply(librosa.get_duration)
    return tess_df

def create_data_crema():
    crema= "data/crema/"
    list_files_crema= os.listdir(crema)
    female = [1002,1003,1004,1006,1007,1008,1009,1010,1012,1013,1018,1020,1021,1024,1025,1028,1029,1030,1037,1043,1046,1047,1049,
          1052,1053,1054,1055,1056,1058,1060,1061,1063,1072,1073,1074,1075,1076,1078,1079,1082,1084,1089,1091]
    gender_crema=[]
    path_crema=[]
    emotion_crema=[]
    for file in list_files_crema:
        part=file.split("_")
        if int(part[0]) in female:
            gend= "female"
        else:
            gend="male"
        gender_crema.append(gend)
        if part[2]=="SAD":
            emotion_crema.append("sad")
        elif part[2]=="ANG":
            emotion_crema.append("angry")
        elif part[2]=="DIS":
            emotion_crema.append("disgust")
        elif part[2]=="FEA":
            emotion_crema.append("fear")
        elif part[2]=="HAP":
            emotion_crema.append("happy")
        elif part[2]=="NEU":
            emotion_crema.append("neutral")
        else:
            emotion_crema.append("unknown")
        path_crema.append(crema+file)
    crema_df= pd.DataFrame(emotion_crema, columns=["emotion"])
    crema_df= pd.concat([pd.DataFrame(gender_crema, columns=["gender"]), crema_df,pd.DataFrame(path_crema, columns=["path"])], axis=1)
    crema_df['duration'] = crema_df['path'].apply(get_data).apply(librosa.get_duration)
    return crema_df

def merge_data():
    emotion_df = pd.concat([create_data_savee(), create_data_ravdess()])
    emotion_df= pd.concat([emotion_df,create_data_tess()])
    emotion_df= pd.concat([emotion_df,create_data_crema()])
    return emotion_df



if __name__ == '__main__':
    emo = merge_data()