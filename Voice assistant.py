#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import speech_recognition as sr
import pyttsx3
import datetime


recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print("You said:", query)
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""


def perform_action(query):
    if "time" in query:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")
    elif "date" in query:
        current_date = datetime.date.today().strftime("%A, %B %d, %Y")
        speak(f"Today's date is {current_date}")
    elif "thank you" in query:
        speak("You're welcome!")
    elif "exit" in query or "quit" in query:
        speak("Goodbye!")
        exit()
    else:
        speak("I'm sorry, I don't understand that command.")


def main():
    speak("Hello! How can I assist you today?")
    while True:
        query = listen()
        if query:
            perform_action(query)

if __name__ == "__main__":
    main()
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_sphinx(audio)
        print("You said:", query)
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError as e:
        print("Recognition request failed; {0}".format(e))
        return ""


# In[ ]:





# In[ ]:




