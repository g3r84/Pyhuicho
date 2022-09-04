#!/usr/bin/python3

from gtts import gTTS
import playsound
import speech_recognition as sr

# global variables #
R = sr.Recognizer()


def speak(text):
    # process text-to-speech #
    tts = gTTS(text, lang='es', tld='com.mx')
    tts.save('tts.mp3')
    playsound.playsound('tts.mp3')

def listen():
    # get audio from microphone to audio object #
    with sr.Microphone(device_index=0) as source:
        playsound.playsound('beeping.mp3')
        R.adjust_for_ambient_noise(source)
        audio = R.listen(source)
    return audio

def transcript(audio):
    # recognize speech using Google Speech Recognition
    try:
        print("Google Speech Recognition entendio:  " + r.recognize_google(audio, language='es_PE'))
    except sr.UnknownValueError:
        print("Google Speech Recognition no entendio el audio")
    except sr.RequestError as e:
        print("No conecto con Google Speech Recognition ; {0}".format(e))

if __name__ == "__main__":
    speak('hello world')
    transcript(listen())
