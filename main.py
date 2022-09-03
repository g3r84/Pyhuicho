#!/usr/bin/python3

from gtts import gTTS
import playsound
import speech_recognition as sr


r = sr.Recognizer()


def speak(text):
    tts = gTTS(text, lang='es', tld='com.mx')
    tts.save('tts.mp3')
    playsound.playsound('tts.mp3')

def listen():
    with sr.Microphone(device_index=0) as source:
        playsound.playsound('beeping.mp3')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    return audio

def transcript(audio):
    # recognize speech using Google Speech Recognition
    try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        print("Google Speech Recognition entendio:  " + r.recognize_google(audio, language='es_PE'))
    except sr.UnknownValueError:
        print("Google Speech Recognition no entendio el audio")
    except sr.RequestError as e:
        print("No conecto con Google Speech Recognition ; {0}".format(e))


speak('hello world')
transcript(listen())
