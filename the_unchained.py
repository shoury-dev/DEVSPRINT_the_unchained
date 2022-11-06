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


if __name__=="__main__":
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
        elif 'How are you' in query:
            speak("I am fine. What about you")
        elif 'who made you' in query:
            speak(" my masters are the_unchained")
        elif 'when you were born' in query:
            speak("I am still in progress, I havent taken birth properly")
        elif 'Bunty tera sabun slow hai kya' in query:
            speak("mera nahi par tumhara hoga") 
        elif 'where you were born' in query:
            speak("In Schooo of computer engineering campus")  
        elif 'what do you like to do' in query:
            speak("Serving my master is the most enjoyable thing for me")
        elif 'open youtube' in query :
            speak("opening youtube")
            webbrowser.open("youtube.com") 
        elif 'open facebook' in query :
            speak("opening facebook") 
            webbrowser.open("facebook.com")
        elif 'open google' in query :
            speak("opening google")
            webbrowser.open("google.com") 
        elif 'good morning bunty' in query :
            speak("good morning, master have a beautifu day ahead")
        elif 'good afternoon bunty' in query :
            speak("good afternoon, master")    
        elif 'good evening bunty' in query :
            speak("good evening, master")           
        elif 'good night bunty' in query :
            speak("good night, master")   
        elif 'who is your favourite superhero' in query :
            speak("Iron man, love you 3000") 
        elif 'open instagram' in query :
            speak("opening instagram") 
            webbrowser.open("instagram.com")
        elif 'What is the time now' in query :
            strTime = datetime.datetime.now().strftime ("%H:%M:%S")
            speak(f"sir the time is (strfTime)")
       





        





           

               

























    




