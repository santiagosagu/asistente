import speech_recognition as sr
import os
import webbrowser

# Definimos la función para que el asistente hable
def speak(text):
    print(text)
    # No incluimos la implementación de la función 'say' porque no funciona en Windows
    # en su lugar usaremos la librería 'pyttsx3' para hablar

    # Importamos la librería pyttsx3
    import pyttsx3

    # Creamos un objeto de la clase 'Engine'
    engine = pyttsx3.init()

    # Cambiamos la voz del asistente a una voz femenina en español
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('language', 'es')

    # El asistente habla el texto que se le pasa como parámetro
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
        else:
            speak("Lo siento, no he entendido qué página quieres abrir")
    elif "cerrar" in command:
        if "google" in command:
            os.system("taskkill /f /im chrome.exe")
            speak("Cerrando Google")
        elif "youtube" in command:
            os.system("taskkill /f /im chrome.exe")
            speak("Cerrando YouTube")
        elif "facebook" in command:
            os.system("taskkill /f /im chrome.exe")
            speak("Cerrando Facebook")
        else:
            speak("Lo siento, no he entendido qué página quieres cerrar")
    elif "adiós" in command or "chao" in command or "hasta luego" in command:
        speak("Hasta luego, ¡que tengas un buen día!")
        exit()
    else:
        speak("Lo siento, no te he entendido")

# Creamos un bucle infinito que escucha al usuario y procesa sus comandos
while True:
    command = recognize_speech().lower()
    interpret_command(command)