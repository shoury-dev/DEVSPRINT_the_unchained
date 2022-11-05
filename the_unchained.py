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

        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")    
    except Exception as e:
        speak('Say that again please....')
        return "None"
    return query      


if __name__=="_main_":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 5)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com') 
        elif'How are you' in query:
            speak("I am fine. What about you")
        elif' who made you' in query:
            speak(" my masters are the_unchained")
            
           

               

























    




