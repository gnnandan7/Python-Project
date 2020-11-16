import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r=sr.Recognizer()

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio=r.listen(source)
        voice_data=''
        try:
            voice_data=r.recognize_google(audio)
        except sr.UnknownValueError:
            speak('Sorry, I did not get that')
        except sr.RequestError:
            speak('Sorry, My speech service is down')
        return voice_data
    
def speak(audio_string):
    tts=gTTS(text=audio_string,lang='en')
    r=random.randint(1,10000000)
    audio_file='audio-'+str(r) +'.mp3'
    tts.save(audio_file)  
    playsound.playsound(audio_file)
    print(audio_string) 
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        speak('My name is Nandan')
        
    if 'what is current date and time' in voice_data:
        speak(ctime())
            
    if 'search' in voice_data:
        search=record_audio('What i need to search for')    
        url='https://www.google.com/search?q=' + search
        webbrowser.get().open(url) 
        speak("Here is What i found!" + search)
        
    if 'location' in voice_data:
        location=record_audio('Find the location')    
        url='https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url) 
        speak("Here the location" + location)
        
    if 'exit' in voice_data:
        exit()
        
time.sleep(0.1) 
speak('Hello! Nandan How Can i Help You')
while 0.1:
    voice_data=record_audio()
    respond(voice_data)