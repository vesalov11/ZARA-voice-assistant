import wikipedia
import speech_recognition as sr
import pyttsx3
#https://github.com/DeonCardoza/voice-assistant/blob/main/Voice%20Assistant/Voice%20Assistant.py
# Set up the text-to-speech engine
engine = pyttsx3.init()

# Set up the speech recognition engine
r = sr.Recognizer()

# Set the language to Bulgarian
language = 'bg-BG'

# Define a function to search and read out Wikipedia articles
def wikipedia_search():
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)
    try:
        # Use speech recognition to get the search term
        search_term = r.recognize_google(audio, language=language)
        print("Searching for: " + search_term)

        # Search Wikipedia for the term in Bulgarian
        wikipedia.set_lang('bg')
        page = wikipedia.page(search_term)

        # Use text-to-speech to read out the summary of the article
        summary = wikipedia.summary(search_term, sentences=2)
        print(summary)
        engine.say(summary)
        engine.runAndWait()

    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Call the Wikipedia search function
wikipedia_search()