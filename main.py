import random
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os

listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    print(text)
    engine.say(text)
    engine.runAndWait()
    


def Greet_Me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        talk('Good Morning')
    elif hour >= 12 and hour <= 16:
        talk('Good Afternoon')
    else:
        talk('Good Evening')
    talk('Hi I am Friday , How may I help you ?')

Greet_Me()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.pause_threshhold = 2
            voice = listener.listen(source)
            print("Recognizing......")
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            
    except:
        pass
    return command




def Execute_FRIDAY():
    command = take_command()
    print(command)
    if 'play' in command:
        video = command.replace('play', '')
        talk('Playing ' + video)
        pywhatkit.playonyt(video)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'i want to know about' in command:
        person = command.replace('i want to know about ', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'tell me a joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
    elif 'hello' in command:
        talk('Hello I am Friday')
    elif 'open youtube' in command:
        talk('Opening Youtube')
        webbrowser.open("youtube.com")
    elif 'open whatsapp' in command:
        talk('Opening Whatsapp')
        webbrowser.open("web.whatsapp.com")
    elif 'you are cool' in command:
        talk('Thanks for the compliment')
    elif 'search' in command:
        result = command.replace('Search', '')
        talk('Searching ' + result)
        pywhatkit.search(result)
    elif 'listen music' in command:
        music_dir = 'C:\\Users\\Mac\\Dir\\Non-Critical'
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, random.choice(songs)))
    else:
        talk('Please say the command again')



while True:
    Execute_FRIDAY()

