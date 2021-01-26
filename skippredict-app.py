import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

st.write("""
# Spotify Skip Prediction App

This app predict whether the song will be skipped or not

""")

st.sidebar.header('User input features')

def user_input_features():
    session_position = st.sidebar.slider('Session position',1.0,20.0,5.0)
    session_length = st.sidebar.slider('Session position',10.0,20.0,5.0)
    no_pause_before_play = st.sidebar.slider('No pause before play', 0.0,1.0,1.0)
    short_pause_before_play = st.sidebar.slider('short pause before play', 0.0,1.0,0.0)
    long_pause_before_play = st.sidebar.slider('Long pause before play', 0.0,1.0,0.0)
    hist_user_behavior_n_seekfwd  = st.sidebar.slider('User behavior seekfwd', 0.0,38.0,0.0)
    hist_user_behavior_n_seekback  = st.sidebar.slider('User behavior seekback', 0.0,73.0,0.0)
    hour_of_day = st.sidebar.slider('Hour of day', 0.0,23.0,0.0)
    context_type = st.sidebar.selectbox('Context type',('editorial_playlist', 'user_collection', 'charts', 'catalog',
       'radio', 'personalized_playlist'))
    hist_user_behavior_reason_start = st.sidebar.selectbox('User behavior reason start',('trackdone', 'fwdbtn', 'backbtn', 'clickrow', 'appload', 'playbtn',
       'remote', 'endplay', 'trackerror'))

    data = {'session_position': session_position,
            'session_length': session_length,
            'no_pause_before_play': no_pause_before_play ,
            'short_pause_before_play': short_pause_before_play,
            'long_pause_before_play': long_pause_before_play,
            'hist_user_behavior_n_seekfwd': hist_user_behavior_n_seekfwd,
            'hist_user_behavior_n_seekback': hist_user_behavior_n_seekback,
            'hour_of_day': hour_of_day,
            'context_type': context_type,
            'hist_user_behavior_reason_start': hist_user_behavior_reason_start}
    features = pd.DataFrame(data, index=[0])
    return features
input_df = user_input_features()


main = pd.read_csv('technocolabs training set.csv',low_memory=False)
feat = pd.read_csv('tf_000000000000.csv',low_memory=False)
main.rename(columns = {'track_id_clean':'track_id'},inplace=True)
dataf = pd.merge(main,feat)
df = dataf[['session_position','session_length','no_pause_before_play','short_pause_before_play','long_pause_before_play','hist_user_behavior_n_seekfwd','hist_user_behavior_n_seekback','hour_of_day','context_type','hist_user_behavior_reason_start']]
df = pd.concat([input_df,df],axis=0)

encode = ['context_type','hist_user_behavior_reason_start']
for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df,dummy], axis=1)
    del df[col]
df = df[:1]

st.subheader('User Input features')

st.write(df)

load_clf = pickle.load(open('skip_prediction.pkl', 'rb'))

prediction = load_clf.predict(df)
st.subheader('Prediction')
skip = np.array(['Not','Skipped'])
st.write(skip[prediction])
