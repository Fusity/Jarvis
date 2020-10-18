import pyttsx3 #pip3 install pyttsx3
import speech_recognition as sr #pip3 install speechRecognition
import datetime
import wikipedia #pip3 install wikipedia
import webbrowser
import os
import smtplib

print("Initialising Jarvis")


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Speak function will pronouce the string wich is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    print(hour)

speak("Initialising Jarvis...")
speak("Fusity est le plus beau !")

wishMe()
