import speech_recognition as sr
import pyttsx3
import pywhatkit

listener = sr.Recognizer()
engine = pyttsx3.init()
class Voice():
    def __init__(self):
        pass
    @classmethod
    def messague(self):
        print("hola star")
    @classmethod
    def voz(self):
        voices = engine.getProperty('voices')

res = Voice()
res.messague()