import os
from ai_handler import get_ai_response
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f'You said: {query}')
            return query
        except Exception:
            return "Some error occurred, maybe you were not audible!"

if __name__ == '__main__':
    say("Welcome Sir!")
    say('I am Snow, your AI assistant! How can I help you?')
    while True:
        print("Listening....")
        query = takeCommand()

        ai_reply = get_ai_response(query)
        print(f"AI: {ai_reply}")
        say(ai_reply)

        sites = [
            ['Youtube', 'https://www.youtube.com'],
            ['Google', 'https://www.google.com'],
            ['Netflix', 'https://www.netflix.com'],
            ['Amazon', 'https://www.amazon.com'],
            ['LeetCode', 'https://www.leetcode.com'],
            ['Instagram', 'https://www.instagram.com'],
            ['Spotify', 'https://www.spotify.com'],
        ]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} Sir.....")
                webbrowser.open(site[1])

        if "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            minute = datetime.datetime.now().strftime("%M")
            say(f'Sir, the time is {hour} hour and {minute} minutes')
