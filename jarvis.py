import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning Sir!")
    elif hour>=12 and hour<18:
        speak("Good afternoon Sir!")
    elif hour>=18 and hour<21:
        speak("Good evening Sir!")
    else:
        speak("Good night Sir!")    

    speak("I am Jain. on your service")            

def takeCommand():
    #it takes microphones input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source)
        r.pause_threshold = 1
        r.energy_threshold = 600

    try:
        print("recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print(e) 
        print("say that again please...")
        return "none"       
    return query

if __name__ == "__main__":
    speak("hello")
    wishMe()
    while True:
        query = takeCommand().lower()
        #logic for executing task based on query
        if 'wikipedia' in query:
            speak('searching wikipedia........')
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'quit' in query:
            speak("Quiting sir, Thank you!")
            exit()  

        elif 'hello jain' in query:
            print("Hello Rony")
            speak("Hello Rony")      
        
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("https://www.youtube.com")
            exit()

        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("https://www.google.com")    
            exit()

        elif 'play music' in query:
            music_dir = 'D:\\Music\\sound'
            songs = os.listdir(music_dir)
            print(songs)
            speak("playing music")
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime  = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is :{strTime}")
            speak(f"Sir, The time is {strTime}")

        elif "thank you" in query:
            speak("Your welcome, sir!")   

        elif "open code" in query:
            codepath = "C:\\Users\\Rony\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
            speak("opening visual studio code, please wait")
            os.startfile(codepath)        

        elif "ok bye" in query or "good bye" in query or "stop" in query:
            speak("Your personal assistant jain is shutting down, Good Bye!")
            print("Your personal assistant jain is shutting down, Good Bye!")


        elif 'ask' in query:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question = takeCommand()
            app_id = "paste your unique id here"
            Client = wolframalpha.Client('QL6WQ8-5RUWJVH9VK')
            res = Client.query(question)
            answer = next(res.results).text
            print(answer) 
            speak(answer)
               

        else:
            speak("unable to respose.")
            print("sorry sir")
            speak("sorry sir")      