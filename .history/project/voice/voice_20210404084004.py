import speech_recognition as sr
import pyttsx3
import pywhatkit

class Voice():
    listener = sr.Recognizer()
    engine = pyttsx3.init()

    def messague(self):
        print("hola star")

    def voz(self):
        pass
    
res = Voice()
res.messague()