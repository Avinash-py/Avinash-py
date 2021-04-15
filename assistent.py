import datetime
import wikipedia
import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import smtplib
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int (datetime.datetime .now().hour)
    if hour >= 0 and hour <12:
        speak ("Good Morning")

    elif hour >12  and hour<18 :
        speak (" good noon")
    else :
        speak ("good evening")

    speak (" wellcome sir i am ur assistent how can  i help  u ")

def takecommand():
    #it take microphon  input from user and return string
    r = sr. Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=.5 #while speaking it pause  while
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language= 'en-in')
        print(f'user said: {query}\n')
    except Exception as e :
        print(e)

        print("Sorry ! say again")
        return "none"
    return query


def sendEmail(to ,content):
    sever = smtplib.SMTP('smtp.gmail.com', 587)
    sever.ehlo()
    sever.starttls()
    sever.login("avi941416@gmail.com", "9452805113")
    sever.sendmail( "avi941416@gmail.com", to , content)

if __name__== "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        #logic for  executing task
        if "wikipedia" in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)

            speak("According to wikipedia")
            print(result)
            speak((result))
        elif "open youtube" in query:
            webbrowser.open ("youtube.com")
        elif "open google" in query:
            webbrowser.open ("google.com")
        elif "open facebook" in query:
            webbrowser.open ("facebook.com")

        elif "play music" in query:
            music_dir ="C:\\Users\\AVINASH\\Desktop\\soundeffect\\15-Free-Ambient-Sound-Effects\\15 Free Ambient Sound Effects"
            song = os.listdir(music_dir)
            print(song)
            os.startfile(os.path.join(music_dir,song[0]))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak (f"sir the time is {strTime}")
            print(strTime)
        elif "open pycharm" in query:
            path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.1\\bin\\pycharm64.exe"
            os.startfile(path)

        elif  " send email" in query:
            try:
                speak(" say")
                content = takecommand()
                to = "avinash5.kushwaha71@gmail.com"
                sendEmail (to, content)
                speak ("email sent")
            except Exception as e :
                print(e)
                speak ("sorry")