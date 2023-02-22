import pyttsx3
import speech_recognition as sr
import webbrowser
import pyaudio
import datetime
import wikipedia as wikipedia

# Глас
engine = pyttsx3.init()
engine.setProperty('rate', 135)
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
            print('стартитаме you tube')
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


def кой():
    wikipedia.set_lang('bg')
    page = wikipedia.page()

    # Use text-to-speech to read out the summary of the article
    summary = wikipedia.summary(sentences=2)
    print(summary)
    engine.say(summary)
    engine.runAndWait()


if __name__ == 'main':
    print('test')
    while True:
        command = listen()
        hangle_message(command)