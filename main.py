import pyttsx3
import speech_recognition as sr
import webbrowser
import pyaudio
import datetime
import wikipediaapi
import wikipedia as wikipedia
import time
import os
import json

import requests
from bs4 import BeautifulSoup

# Глас
engine = pyttsx3.init()
engine.setProperty('rate', 135)
engine.setProperty('voice', 'bulgarian')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("hi im your voices asisstent Zara")
engine.say("kak da pomogna")

engine.runAndWait()
engine.stop()


# Взимаме аудиото
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as sourse:
        print("Кажете команда")
        engine = pyttsx3.init()
        engine.runAndWait()
        audio = r.listen(sourse)
        try:
            speech = r.recognize_google(audio, language='bg')
            print(speech)
            return (speech)
        except sr.UnknownValueError:
            return "error"
        except sr.RequestError:
            return "error"


# Функции
def hangle_message(message):
    message = message.lower()
    if "зара" in message:
        if "чао" in message:

            exit()


        elif "youtube" in message:
            print('стартитаме  YouTube')
            webbrowser.open_new_tab('https://www.youtube.com')
            engine = pyttsx3.init()
            engine.say("startiram YouTube")
            engine.runAndWait()

        elif "netflix" in message:
            print('Стартираме Netflix')
            webbrowser.open_new_tab('https://www.netflix.com')
            engine = pyttsx3.init()
            engine.say("startiram Netflix")
            engine.runAndWait()

        elif "facebook" in message:
            print('отваряме facebook')
            webbrowser.open_new_tab('https://www.facebook.com')
            engine = pyttsx3.init()
            engine.say("отваряме facebook ")
            engine.runAndWait()

        elif "времето" in message:
            print('отваряме времето')
            webbrowser.open_new_tab(
                'https://www.google.com/search?client=opera&q=времето&sourceid=opera&ie=UTF-8&oe=UTF-8')
            engine = pyttsx3.init()
            engine.say("vremeto e")
            engine.runAndWait()

        elif "календар" in message:
            print('отваряме календара')
            webbrowser.open_new_tab('https://календар.com/kalendar-2023.html')
            engine = pyttsx3.init()
            engine.say("отваряме календара")
            engine.runAndWait()

        elif "spotify" in message:
            print('отваряме календара')
            webbrowser.open_new_tab('https://open.spotify.com/playlist/06S64oWn7uGnfGrwjh5IWb')
            engine = pyttsx3.init()
            engine.say("отваряме календара")
            engine.runAndWait()

        elif "страшни филми" in message:
            print('отваряме календара')
            webbrowser.open_new_tab('https://www.filmi2k.com/category/ujasi/kabirtech.net?host=www.filmi2k.com')
            engine = pyttsx3.init()
            engine.say("Резъктат от търсенето на страшни филм")
            engine.runAndWait()

        elif 'дата' in message:
            engine = pyttsx3.init()
            now = datetime.datetime.now()
            date_str = now.strftime("%A, %B %d, %Y")
            engine.say(f"dnes sme {date_str}")
            engine.runAndWait()

        elif 'часът' in message:
            engine = pyttsx3.init()
            now = datetime.datetime.now()
            time_str = now.strftime("%I:%M %p")
            engine.say(f"chasat e  {time_str}")
            engine.runAndWait()

        elif 'изключи' in message:
            time_left = 5
            while time_left > 0:
                print(f"shutting down in {time_left} seconds...")
                time_left -= 1
                time.sleep(1)
            os.system("shutdown /s /t 1")

        elif 'какво' in message:

            api_key = "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"
            url = f"https://api.openweathermap.org/data/2.5/weather?q={new yourk}&appid={api_key}"
            response = requests.get(url)
            data = json.loads(response.text)
            temperature = round(data["main"]["temp"] - 273.15, 2)
            description = data["weather"][0]["description"]
            engine.say(f"The temperature in {city} is {temperature} degrees Celsius with {description}")
            engine.runAndWait()
        elif 'кой' in message:
            engine = pyttsx3.init()

            r = sr.Recognizer()
            language = 'bg-BG'
            with sr.Microphone() as source:
                print("Speak now...")
                audio = r.listen(source)
            try:
                search_term = r.recognize_google(audio, language=language)
                print("Searching for: " + search_term)

                wikipedia.set_lang('bg')
                page = wikipedia.page(search_term)

                summary = wikipedia.summary(search_term, sentences=2)
                print(summary)
                engine.say(summary)
                engine.runAndWait()

            except sr.UnknownValueError:
                print("Sorry, I didn't understand that.")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == '__main__':
    print('test')
    while True:
        command = listen()
        hangle_message(command)