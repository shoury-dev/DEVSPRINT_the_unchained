import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
     speak('Good morning')
    
    elif hour>=12 and hour<18:
     speak('Good afternoon')

    else:
     speak('Good evening') 
speak('Hi, this is Bunty. How can I help you')

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening... ")
        r.pause_threshold = 2
        
























    




