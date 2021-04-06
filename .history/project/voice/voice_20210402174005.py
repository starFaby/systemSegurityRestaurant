import speech_recognition as sr
import pyttsx3
import pywhatkit


class Voice():
    countVoice = 0
    voicesTotal = []
    voicePerson = 4
    def voice():
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

prueba = Voice()
prueba.talk('hola faby star')
