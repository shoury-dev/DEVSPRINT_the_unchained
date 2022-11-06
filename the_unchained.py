import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import os
import time
from bs4 import BeautifulSoup
import requests
import ecapture as ec
import pywhatkit
import pyautogui
from win10toast import ToastNotifier




engine =  pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("Good Morning!")

    elif hour>=12 and hour<18 :
        speak("Good Afternoon")

    else:
        speak("Good Evening") 

    speak("Hi this is bunti, how can I help you ?")      

def takeCommand():
    #it takes microphene input from the user and returns string output

    r  = sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening...")
        r.pause_threshhold = 1
        audio =r.listen(source)

    try  :
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')    
        print(f"User said:{query}\n")

    except Exception as e :
        #print(e)
        print("Say that again please...")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'type-password-here')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

    
if __name__ == "__main__":
    wishme()
    #while True :
    if 1:
         query = takeCommand().lower()
    #logic  for xecuting tasks
         if 'wikipedia' in query :
            speak('Searching Wikipedia...')
            query= query.replace("wikipedia", "")
            results  = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)

         
         elif 'how are u' in query:
            speak('i am good , what about u')
         elif 'i am fine, can u do something to make me feel alive ' in query:
            webbrowser.open('yes definitely sir, what can i do for u , would u like to listen some music or say something of your choice')
         elif 'open google' in query:

            webbrowser.open('google.com')
         elif 'open facebook' in query:
            webbrowser.open("facebook.com") 
      
         elif 'the time' in query :
            strTime = datetime.datetime.now().strftime("%H-%M-%D")
            speak(f"sir the time is {strTime}")

         elif 'the date' in query :
            strTime = datetime.datetime.now().strftime("%Y-%M-%D")
            speak(f"sir the date is {strTime}")


         #the function to send emails
         elif 'send mail to shouryjeet gupat' in query :
            try:
                speak("what  should i say ")
                content = takeCommand()
                to = "youremail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e :
                print(e)
                speak("Sorry dear i was not able to send the mail at the")
         elif 'open chrome' in query :
           pyttsx3.speak("opening chrome")
           print(".")
           print(".")
           os.system("C:\Program Files\Google\Chrome\Application")


          #knowing everything about followers 
         elif 'open instagram' in query:
            pyttsx3.speak("what do youu want to do on instagram")
            querye = takeCommand().lower()
            if 'number of followers' in query :
                
                print("...")

            print (".....")
            webbrowser.open("instagram.com")



            #to do anything on twitter
         elif 'open twitter' in query:
            pyttsx3.speak("opening Twitter ")
            print (".....")
            webbrowser.open("twitter.com")



            #to do anything on facebook
         elif 'open facebook' in query:
            pyttsx3.speak('where do you want to go in facebook')
            queryc = takeCommand().lower()
            if 'main' in queryc:
                pyttsx3.speak("opening Facebook ")
                print (".....")
                webbrowser.open("facebook.com")
            elif 'open friend requests' in queryc: 
                pyttsx3.speak('opening friend request list')
                print(".....")
                webbrowser.open("facebook.com/friends")



                #to  do any  thing on youtubee
         elif 'open youtube' in query:
            
            pyttsx3.speak('where do you want to go in youtube')
            queryb = takeCommand().lower()
            if 'main' in query:
                webbrowser.open("youtube.com")            
            elif 'trending page' in queryb: 
                pyttsx3.speak('showing trending page')
                print(".....")
                webbrowser.open("youtube.com/feed/trending")
            elif 'shorts' in queryb:
                pyttsx3.speak("showing shorts")
                print(".....")
                webbrowser.open("youtube.com/shorts")



                #code for system shutdown
         elif 'shutdown' in query:
            pyttsx3.speak("Shutting down")
            print('shutting down.....')
            time.sleep(5)
            os.system(r"shutdown/s/t 1")   



            #code to open any file in an system
         elif 'open java folder' in query :

          os.startfile("C:\\Users\\KIIT\\Desktop\\DOCS\\ACFrOgAqc0g0NY5gLUYmSYmM4NqDMTYBWzhmAXImpLxHk3ubm47JoSgJu_P5taKoRfQGehnGasfdStLRy9NrMAXMotalx0eMF4ve3_5YRC9E7LY5jFTbYvF3V9Gfrs6mkmJ9ifXaoD8oiykgLkd9.pdf")   

          
          
          #to search anything on google
         elif 'google search' in query or 'search' in query or 'google' in query:            
            pyttsx3.speak("say what you want to search in google")
            print("say what you want to search in google")
            queryd = takeCommand().lower()
            x=queryd.split()
            print (x)
            y=""
            for i in range (len(x)):
                if i<(len(x)-1):
                    y+=x[i]
                    y+=(r"+")
                else:
                    y+=x[i]
            z=r"google.com/search?q="
            z+=y
            pyttsx3.speak("Searching")
            print("Searching......")
            webbrowser.open(z)


            #to send whatsapp messages
         
         


                #to set a reminder
         elif 'set a reminder' in query :
            speak("setting....")
            toaster = ToastNotifier()

            Toasttitle = input("\nTitle of Remainder: ")
            msg = input("Message: ")
            minutes = float(input("How many Minutes: "))
            seconds = minutes * 60
            print("\nRemainder Set Successfully!\n")
            time.sleep(seconds)
            toaster.show_toast(Toasttitle, msg, duration=10, threaded=True)

            while toaster.notification_active:
                time.sleep     


                #to do some other ordinary things qith the bunty
          
         elif 'How are you' in query:
            speak("I am fine. What about you")
         elif 'who created you' in query:
            webbrowser.open("https://twitter.com/gdsckiit/status/1588789177898110976?t=FVcgdznp8Nt8Crf-sS_eAQ&s=08")
         elif 'when you were born' in query:
            speak("I am still in progress, I havent taken birth properly")
         elif 'Bunty tera sabun slow hai kya' in query:
            speak("mera nahi par tumhara hoga") 
         elif 'where you were born' in query:
            speak("In School of computer engineering campus")  
         elif 'what do you like to do' in query:
            speak("Serving my master is the most enjoyable thing for me")
        
         
         
         elif 'good morning bunty' in query :
            speak("good morning, master have a beautifu day ahead")
         elif 'good afternoon bunti' in query :
            speak("good afternoon, master")    
         elif 'good evening bunti' in query :
            speak("good evening, master")  
         elif 'good night bunti' in query :
            speak("good night, master")   
         elif 'who is your favourite superhero' in query :
            speak("Iron man, love you 3000") 
         
    
         elif 'which is your favourite movie' in query :
            speak("I don't watch movies very often but Interstellar is my favourite")
         elif 'open chrome' in query :
            pyttsx3.speak("opening chrome")
            print(".")
            print(".")
            os.system("chrome.exe")
         elif 'open telegram' in query :
            pyttsx3.speak("opening telegram")
            print(".")
            print(".")
            os.system("telegram.exe")
            #######
         elif 'open file explorer' in query:
            file_dr= 'Documents'
            work = os.listdr(file_dr)
            print(work)
         elif 'open youtube' in query:
            webbrowser.open('youtube.com') 
         elif 'How are you' in query:
            speak("I am fine. What about you")
         elif 'who created you' in query:
            webbrowser.open("https://twitter.com/gdsckiit/status/1588789177898110976?t=FVcgdznp8Nt8Crf-sS_eAQ&s=08")
         elif 'when you were born' in query:
            speak("I am still in progress, I havent taken birth properly")
         elif 'Bunty tera sabun slow hai kya' in query:
            speak("mera nahi par tumhara hoga") 
         elif 'where you were born' in query:
            speak("In School of computer engineering campus")  
         elif 'what do you like to do' in query:
            speak("Serving my master is the most enjoyable thing for me")
         
    
         elif 'good morning bunty' in query :
            speak("good morning, master have a beautifu day ahead")
         elif 'good afternoon bunti' in query :
            speak("good afternoon, master")    
         elif 'good evening bunti' in query :
            speak("good evening, master")           
         elif 'good night bunti' in query :
            speak("good night, master")   
         elif 'who is your favourite superhero' in query :
            speak("Iron man, love you 3000") 
        
        
         elif 'which is your favourite movie' in query :
            speak("I don't watch movies very often but Interstellar is my favourite")
         elif 'open chrome' in query :
            pyttsx3.speak("opening chrome")
            print(".")
            print(".")
            os.system("chrome.exe")
         
         elif 'open telegram' in query :
            pyttsx3.speak("opening telegram")
            print(".")
            print(".")
            os.system("telegram.exe")
            #######
         elif 'open file explorer' in query:
            file_dr= 'Documents'
            work = os.listdr(file_dr)
            print(work)
            os.startfiles(os.path.join(file_dr, work[1]))
         elif 'open mail' in query :
            pyttsx3.speak("opening mail")
            print(".")
            print(".")
            os.system("mail.exe")
         elif 'what do you do in your free time' in query :
            speak("just relax in your system")  
         elif 'open microsoft store' in query :
            pyttsx3.speak("opening windows store")
            print(".")   
            print(".")
            os.system("microsoftstore.exe")
         elif 'open wps office' in query :
            pyttsx3.speak("opening wps office")
            print(".")   
            print(".")
            os.system("wpsoffice.exe")
         elif 'do you watch anime' in query :
            speak("yes, some of my favourites are demon slayer, Attack on Titan and death note")
         elif 'open discord' in query :
            speak("opening discord")
            webbrowser.open("discord.com")
         elif 'open reddit' in query :
            speak("opening reddit") 
            webbrowser.open("reddit.com")   
                     
  