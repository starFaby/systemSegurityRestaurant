import speech_recognition as sr
import pyttsx3
import pywhatkit

class Voice():
    voicesTotal = []
    voicePerson = 4
    def __init__(self):
        pass

    def voice():
        countVoice = 0
        voices = engine.getProperty('voices')
        for voice in voices:
        countVoice += 1
        voicesTotal.append(f' { countVoice } { voice.name}'.format())

        for g in voicesTotal:
            print(g)

        engine.setProperty('voice', voices[voicePerson].id)

    def talk(text):
        engine.say(text)
        engine.runAndWait()
    
prueba = Voice():
prueba.talk('hola faby star')
