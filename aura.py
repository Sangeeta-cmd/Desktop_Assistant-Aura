from cmath import e
import datetime
from email.mime import audio
import pyttsx3 # type: ignore
import speech_recognition as sr # type: ignore
import wikipedia # type: ignore
import webbrowser
import os
import random 
from requests import get # type: ignore
import pywhatkit as kit # type: ignore
import smtplib
import sys 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[2].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<=18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")           

    speak("I am Aura,  Please tell me how may I help you")

def takecommand():    
# It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...") 
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        speak("Know you say that again please...")
        return "None"
    return query

#to send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',  587)
    server.ehlo()
    server.starttls()
    server.login('abhishekwalaki6361@gmail.com', 'abhi1234#@')
    server.sendmail('abhishekwalaki6361@gmail.com', to, content )
    server.close()

if __name__=="__main__":
    wishme()
    while True:
    #if 1:    
        query = takecommand().lower()

         # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'Music'
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S:")
            speak(f"sir, the time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\abhis\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")
            print(e)

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif "send message" in query:
            kit.sendwhatmsg("+919353822732", "hii",1,1) 

        elif "play songs on youtube" in query:
            kit.playonyt("see you again")       
                
        elif "email to prathamesh" in query:
            try:
                speak("what should i say?")
                content = takecommand().lower()
                to = "ppujarineelsnk9071@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent to prathamesh") 

            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to sent this mail to prathemesh")  

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")                 

        elif 'open movies' in query:
            webbrowser.open("movies.com")   

        elif 'open twitter' in query:
            webbrowser.open("twitter.com")     

        elif 'open snapchat' in query:
            webbrowser.open("snapchat.com")    
           
           


        elif  "no thanks" in query:
            speak("thanks for using me sir, Have a good day.")
            sys.exit()

        speak("do you have any other work")    
