import speech_recognition as sr
import os
import webbrowser
import psutil
import pyttsx3

# Definimos la función para que el asistente hable
def speak(text):
    print(text)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('language', 'es')
    engine.say(text)
    engine.runAndWait()

# Creamos un objeto de la clase 'Recognizer'
r = sr.Recognizer()

# Definimos la función que recoge el audio y lo procesa
def recognize_speech():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("¿En qué puedo ayudarte?")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language='es-ES')
            print(f"Has dicho: {text}")
            return text
        except:
            print("Lo siento, no te he entendido")
            return ""

# Definimos la función que interpreta los comandos del usuario
def interpret_command(command):
    if "abrir" in command:
        if "google" in command:
            speak("Abriendo Google")
            webbrowser.open("https://www.google.com")
        elif "youtube" in command:
            speak("Abriendo YouTube")
            webbrowser.open("https://www.youtube.com")
        elif "facebook" in command:
            speak("Abriendo Facebook")
            webbrowser.open("https://www.facebook.com")
        elif "editor de texto" in command:
            speak("Abriendo el editor de texto")
            os.startfile("notepad.exe")
        elif "calculadora" in command:
            speak("Abriendo la calculadora")
            os.startfile("calc.exe")
        elif "chrome" in command:
            speak("Abriendo chrome")
            os.startfile("chrome.exe")
        else:
            speak("Lo siento, no he entendido qué quieres abrir")
    elif "cerrar" in command:
        if "google" in command:
            speak("Cerrando Google")
            os.system("taskkill /f /im chrome.exe")
        elif "youtube" in command:
            speak("Cerrando YouTube")
            os.system("taskkill /f /im chrome.exe")
        elif "facebook" in command:
            speak("Cerrando Facebook")
            os.system("taskkill /f /im chrome.exe")
        elif "editor de texto" in command:
            speak("Cerrando el editor de texto")
            os.system("taskkill /f /im notepad.exe")
        elif "calculadora" in command:
            speak("Cerrando la calculadora")
            os.system("taskkill /f /im calc.exe")
        elif "chrome" in command:
            speak("Cerrando chrome")
            os.system("taskkill /f /im chrome.exe")
        else:
            speak("Lo siento, no he entendido qué quieres cerrar")
    elif "adiós" in command or "chao" in command or "hasta luego" in command:
        speak("Hasta luego, ¡que tengas un buen día!")
        exit()
    else:
        speak("Lo siento, no te he entendido")

# Creamos un bucle infinito que escucha al usuario y procesa sus comandos
while True:
    command = recognize_speech().lower()
    interpret_command(command)

