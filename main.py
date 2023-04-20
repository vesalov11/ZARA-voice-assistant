import time
import ec as ec
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
from ecapture import ecapture as ec

# Глас
engine = pyttsx3.init()
engine.setProperty('rate', 135)
engine.setProperty('voice', 'bulgarian')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

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

def engine_talk(text):
 engine.say(text)
 engine.runAndWait()



# Функции
def hangle_message(message, engine=None):
    message = message.lower()


    if "зара" in message:
        if "чао" in message:
            print("довиждане, приятен ден!!")
            exit()

        elif 'коя си ти' in message:
            print('Аз съм гласов асистент зара')

        elif "благодаря" in message:
            print("Пак заповядай")


        elif "здравей" in message:
            print("Здравей как мога да бъда полезна?")

        elif "кой те е създал" in message or "кой те е направил" in message:
            print("Аз съм направена от ученик на ПГЕЕ гр. Банско, който се казва Мехмед Весалов")

################################################

        elif "къде се намирам" in command:
            url = "https://www.google.com/maps/search/Where+am+I+?/"
            webbrowser.get().open(url)


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
            print('Днешната дата е:   '+ date_str)
            engine.runAndWait()

        elif 'часът' in message:
            engine = pyttsx3.init()
            now = datetime.datetime.now()
            time_str = now.strftime("%I:%M %p")
            print('chasat e'+ time_str)
            engine.runAndWait()


        elif "снимка" in message or "направи снимка" in message:
            ec.capture(0, "Jarvis Camera ", "img.jpg")



        elif 'пусни' in message or "пуснеш" in message:
            music_dir = "C:\\Users\\ИсуфМВесалов\\Music"

            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[1]))


        elif 'изключи' in message:
            time_left = 2
            while time_left > 0:
                print(f"shutting down in {time_left} seconds...")
                time_left -= 1
                time.sleep(1)
            os.system("shutdown /s /t 1")




  ################################################################################################


        elif 'кой' in command:
            search = 'https://bg.wikipedia.org/wiki/%D0%9D%D0%B0%D1%87%D0%B0%D0%BB%D0%BD%D0%B0_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0' + command
            engine_talk('резултат от търсенето')
            webbrowser.open(search)

        elif "търси" in command or "потърси" in command:
           if "как" in command:
            search = 'https://www.google.com/search?q=' + command
            engine_talk('tarsene')
            webbrowser.open(search)


if name == 'main':
    print('test')
    while True:
        command = listen()
        hangle_message(command)