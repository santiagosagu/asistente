import speech_recognition as sr
import os
import webbrowser

# Configuración del reconocimiento de voz
r = sr.Recognizer()
mic = sr.Microphone()

# Función para abrir aplicaciones
def open_application(application):
    if "navegador" in application.lower():
        os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
    elif "notepad" in application.lower():
        os.startfile("C:\\Windows\\system32\\notepad.exe")

# Función para abrir páginas web
def open_website(url):
    webbrowser.open(url)

# Bucle infinito para escuchar comandos de voz
while True:
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("Háblame")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio, language="es-ES").lower()
        print(f"Has dicho: {command}")

        # Comandos para abrir aplicaciones
        if "abrir" in command and "aplicación" in command:
            open_application(command.split(" ")[-1])
            print(f"Abriendo {command.split(' ')[-1]}")

        # Comandos para cerrar aplicaciones
        elif "cerrar" in command and "aplicación" in command:
            os.system(f"taskkill /im {command.split(' ')[-1]}.exe /f")
            print(f"Cerrando {command.split(' ')[-1]}")

        # Comandos para abrir páginas web
        elif "abrir" in command and "página web" in command:
            open_website(f"http://{command.split(' ')[-1]}.com")
            print(f"Abriendo http://{command.split(' ')[-1]}.com")

        # Comando para salir del asistente
        elif "salir" in command:
            print("Saliendo del asistente...")
            break

    except sr.UnknownValueError:
        print("No te he entendido bien")
    except sr.RequestError:
        print("Ha ocurrido un error al tratar de procesar la petición")