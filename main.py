#SAMYAK PANDEY's F.R.I.D.A.Y.

print("Initializing F.R.I.D.A.Y.")

import random
import speech_recognition as sr
import pyttsx3
import pywhatkit # or import pywhatkit as kit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os
import sys
import PyPDF2

listener = sr.Recognizer()
engine = pyttsx3.init('sapi5') # You can use dummy , espeak or nsss accordingly in place of sapi5
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female Voice

def talk(text):
    print(text)
    engine.say(text) 
    engine.runAndWait()

def Greet_Me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk('Good Morning')
    elif hour >= 12 and hour < 16:
        talk('Good Afternoon')
    elif hour >= 16 and hour != 0:
        talk('Good Evening')
    else:
        pass
    talk('Hi I am FRIDAY , How may I help you ?')
Greet_Me()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening.......')
            listener.pause_threshhold = 2
            voice = listener.listen(source)
            print('Recognizing......')
            command = listener.recognize_google(voice, language = 'en-in')
            command = command.lower()
    except:
        talk('I did not get it !')
        talk('Try writing the Command.......')
        command = str(input("Write Here : "))
    return command

def Execute_FRIDAY():
    command = take_command()
    print(command)
    if 'what can you do' in command:
        talk('I can play video on youtube , get current time , send whatsapp message , get information in wikipedia , tell a joke , play music and much more')
    elif 'play' in command:
        video = command.replace('play', '')
        talk('Playing ' + video)
        pywhatkit.playonyt(video)    
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'send a message' in command:
        try:
                def send_what_msg():
                    try:
                        num = str(input("Number : "))
                    except:
                        talk('Invalid Number')
                    talk('What should I say ?')
                    msg = str(take_command())
                    talk('What hour ?')
                    hours = int(take_command())
                    talk('What minute ?')
                    minute = int(take_command())
                    pywhatkit.sendwhatmsg(num , msg , hours , minute)
        except:
            talk('I am not able to send message at this moment')

        send_what_msg()
    elif 'reader book' in command:
        talk('Reading.........')
        book = open('As Your Wish.pdf', 'rb')
        pdfReader = PyPDF2.PdfFileReader(book)
        pages = pdfReader.numPages
        for num in range(7, pages):
            page = pdfReader.getPage(num)
            text = page.extractText()
            talk(text)
    elif 'i want to know about' in command:
        person = command.replace('i want to know about', '')
        info = wikipedia.summary(person, 4)
        talk('According to Wikipedia......')
        talk(info)
    elif 'tell me a joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)
    elif 'hello' in command:
        talk('Hello I am FRIDAY')
    elif 'open youtube' in command:
        talk('Opening Youtube')
        pywhatkit.search("youtube.com")
    elif 'open whatsapp' in command:
        talk('Opening Whatsapp')
        pywhatkit.search("web.whatsapp.com")
    elif 'you are cool' in command:
        talk('Thanks for the compliment')
    elif 'good work' in command:
        talk('Thank You')
    elif 'nice work' in command:
        talk('Thank You')
    elif 'listen to music' in command:
        music_dir = 'music_file_path'
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, random.choice(songs)))
    elif 'open app' in command:
        App_Location = 'app_file_path'
        os.startfile(App_Location)
        talk('Opening App')
    elif 'open cmd' in command:
        os.system('start cmd')
    elif 'how to' in command:
        videos = command.replace('how to ', '')
        talk('I got it how to '+ videos)
        pywhatkit.search(videos)
    elif 'sleep friday' in command:
        talk('As you wish !')
        sys.exit()
    elif 'thank you' in command:
        talk('My Pleasure')
    else:
        talk('Let me search from Google!')
        pywhatkit.search(command)

    talk('Next Command Please.......... ')
    take_command()

while True:
    Execute_FRIDAY()


