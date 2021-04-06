import speech_recognition as sr
import pyttsx3
import pywhatkit

class Voice():
    def __init__(self):
        pass
    @classmethod
    def messague(self):
        print("hola star")
    @classmethod
    def voz(self, text):
        engine = pyttsx3.init()
        voicePerson = 4
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[voicePerson].id)
        engine.say(text)
        engine.runAndWait()
res = Voice()
res.voz("hola star")