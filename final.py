# -*- coding: utf-8 -*-

!pip install streamlit==1.20.0

!pip install pyttsx3
!apt-get install espeak

# Commented out IPython magic to ensure Python compatibility.
%%writefile app.py
import streamlit as st
import os 
import pyttsx3
import pickle


#Setup the app layout and styling
st.set_page_config(page_title="Emotion-Based TTS", page_icon=":microphone:", layout="centered", initial_sidebar_state="expanded")
st.markdown('<style>body{background-color: #F0F2F6;}h1{color: #1F2937;}</style>', unsafe_allow_html=True)
 
 
#App title
st.title('Emotion-Based Text-to-Speech :microphone:')
 
 
# create engine instance
engine = pyttsx3.init()
 
 
# get the list of available voices
voices = engine.getProperty('voices')


with open('tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)
    model_sent = tf.keras.models.load_model('model.h5')


def decode_sentiment(score, include_neutral=True):
     HAPPY = "happy"
     SAD = "sad"
     NEUTRAL = "neutral"
     SENTIMENT_THRESHOLDS = (0.4, 0.7)
     if include_neutral:        
         label = NEUTRAL
         if score <= SENTIMENT_THRESHOLDS[0]:
             label = SAD
         elif score >= SENTIMENT_THRESHOLDS[1]:
             label = HAPPY
         return label
     else:
         return SAD if score < 0.5 else HAPPY
 
#creating a function when automatic emotion  is selected
 
def predict(text, include_neutral=True):
     x_test = pad_sequences(tokenizer.texts_to_sequences([text]), maxlen=300)
     score = model_sent.predict([x_test])[0]
     label = decode_sentiment(score, include_neutral=include_neutral)
     return label
 
 
#creating the function to convert the text with required emotion


def convert_to_audio(text,emotion,gender):
   if emotion=='auto':
     emotion = predict(text)
   if gender.upper() == 'M':#
       engine.setProperty('voice', voices[0].id) # set to male voice
       if emotion == "happy":
           engine.setProperty('rate', 150)
           engine.setProperty('volume', 1)
           engine.setProperty('pitch', 2.0)
       elif emotion == "sad":
           engine.setProperty('rate', 90)
           engine.setProperty('volume', 0.6)
           engine.setProperty('pitch', 0.7)
       else:
           engine.setProperty('rate', 120)
           engine.setProperty('volume', 0.9)
           engine.setProperty('pitch', 1.0)
   else:
       engine.setProperty('voice', voices[1].id) #set to female voice
       if emotion == "happy":
         engine.setProperty('rate', 150)
         engine.setProperty('volume', 1)
         engine.setProperty('pitch', 3.0)
       elif emotion == "sad":
         engine.setProperty('rate', 90)
         engine.setProperty('volume', 0.6)
         engine.setProperty('pitch', 0.7)
       else:
         engine.setProperty('rate', 120)
         engine.setProperty('volume', 0.9)
         engine.setProperty('pitch', 1.0)
   engine.say(text)
   engine.runAndWait()

#Taking the inputs from user
text = st.text_area("Enter your text:", height=100)
col1, col2 = st.columns(2)
gender = col1.selectbox("Select voice gender:", ["female", "male"])
emotion = col2.selectbox("Select emotion (optional):", ["auto", "happy", "sad", "neutral"])
 
#creating the convert button
if st.button("Convert to audio"):
    if emotion == "":
        emotion = None
       convert_to_audio(text, emotion, gender)
 
 
 
# App description and instructions
st.markdown("""
 ## :information_source: About the app
 
 This app converts the input text to speech based on the selected gender and emotion. If no emotion is selected, the app will automatically detect the emotion from the text.
 
 ## :arrow_forward: How to use
 
 1. Enter your text in the provided text box.
 2. Select the desired voice gender (female or male).
 3. Optionally, select an emotion (happy, sad, or neutral). If you leave it blank, the app will auto-detect the emotion.
 4. Click on the "Convert to audio" button to listen to the synthesized speech.
 """)

!streamlit run app.py & npx localtunnel --port 8501


