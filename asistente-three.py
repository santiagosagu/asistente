import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import time as time_module
import locale
import requests
import openai
from dotenv import load_dotenv
from pywinauto import Application, Desktop, findwindows, controls, win32functions
import pyautogui
import webbrowser
from pycaw.pycaw import AudioUtilities
import win32api
import win32con
import win32gui


def get_window_position(hwnd):
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    width = rect[2] - x
    height = rect[3] - y
    return (x, y, width, height)


load_dotenv()

# Configuración de las librerías
engine = pyttsx3.init()
r = sr.Recognizer()

# Configuración del reconocedor de voz
r.energy_threshold = 100  # Ajustar este valor según tu entorno
r.dynamic_energy_threshold = True  # Habilitar ajuste dinámico del umbral de energía

# Variable para detectar la palabra clave "asís"
asistente_activado = False
microphone_always_on = False

# Configurar idioma español
locale.setlocale(locale.LC_ALL, 'es_ES')

# key openIA
openai.api_key = os.getenv('OPENIA')

# Función para hablar
def speak(text):
    engine.say(text)
    engine.runAndWait()


def volumen_down():

    sessions = AudioUtilities.GetAllSessions()
    
    for session in sessions:
        volume = session.SimpleAudioVolume
        if session.Process and session.Process.name() == "chrome.exe" and asistente_activado == True:
            # print("\tProcess name:", session.Process.name())
            # print("\tVolume:", volume.GetMasterVolume())
            # print("\tMuted:", volume.GetMute())
            volume.SetMasterVolume(0.1, None)
            continue
        else:
            volume.SetMasterVolume(1.0, None)

    # else:
    #     print("No hay audio en reproducción.")

# Función para reconocer el comando de voz
def recognize_speech(max_duration=4):

    global microphone_always_on  # Definir la variable como global

    with sr.Microphone() as source:
        if asistente_activado:
            volumen_down()
            print("Esperando...")

            audio = r.listen(source, phrase_time_limit= max_duration)


        else: 
            print("Llamame Asís y podre ayudarte... ")
            volumen_down()
  
            audio = r.listen(source, phrase_time_limit=1.7) # Grabar hasta 2 segundos como máximo


        try:
            speech_text = r.recognize_google(audio, language="es-ES")
            print(f"Has dicho: {speech_text}")
            return speech_text.lower()
        
        except sr.UnknownValueError:
            # speak("Lo siento, no he entendido lo que has dicho. ¿Puedes repetirlo?")
            return None
        
        except sr.RequestError as e:
            print(f"No se pudo realizar la solicitud a Google Speech Recognition service; {e}")
            return None

# Función para abrir aplicaciones
def open_application(application_name):
    if "chrome" in application_name:
        speak("Abriendo chrome")
        os.startfile("chrome.exe")

    elif "calculadora" in application_name:
            speak("Abriendo la calculadora")
            os.startfile("calc.exe")

    elif "notepad" in application_name:
          os.startfile("notepad.exe")
          speak("abriendo notepad")

    elif "visual" in application_name:
        speak('Abriendo visual')
        os.startfile('C:\\Users\\USER\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe')
    # else:
    #     speak("Lo siento, no puedo abrir esa aplicación.")

# Función para cerrar aplicaciones
def close_application(application_name):
    if "chrome" in application_name:
        speak("Cerrando chrome")
        os.system("taskkill /f /im chrome.exe")

    elif "calculadora" in application_name:
        speak("Cerrando calcular")
        os.system("taskkill /f /im calc.exe")

    elif "notepad" in application_name:
        os.system("taskkill /f /im notepad.exe")
        speak("cerrando notepad")

    elif "visual" in application_name:
        os.system("taskkill /f /im C:\\Users\\USER\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe")

    # elif "excel" in application_name:
    #     subprocess.Popen(["C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"])
    # else:
    #     speak("Lo siento, no puedo abrir esa aplicación.")


# Función para abrir páginas web
def open_website(website_name):
    if "google" in website_name:
        webbrowser.open("https://www.google.com")

    elif "en prime" in website_name:
        speak("Realizando búsqueda")
        webbrowser.open("https://www.primevideo.com/search/ref=atv_nb_sug?ie=UTF8&phrase=" + website_name.replace("buscar en prime ", ""))

    elif "en youtube" in website_name:
        # webbrowser.open("https://www.youtube.com")
        speak("Realizando búsqueda")
        webbrowser.open("https://www.youtube.com/results?search_query=" + website_name.replace("buscar en youtube ", ""))

    elif "youtube" in website_name:
        webbrowser.open("https://www.youtube.com")

    elif "facebook" in website_name:
        webbrowser.open("https://www.facebook.com")

    elif "twitter" in website_name:
        webbrowser.open("https://www.twitter.com")

    elif "en google" in website_name:
        webbrowser.open("https://www.google.com/search?q=" + website_name.replace("buscar en google ", ""))   

    elif "maps" in website_name:
        webbrowser.open("https://www.google.com/maps")

    elif "whatsapp" in website_name:
        webbrowser.open("https://web.whatsapp.com/")

    elif "chat" in website_name:
        webbrowser.open("https://chat.openai.com/")
    # else:
    #     speak("Lo siento, no puedo abrir ese sitio web.")

#funcion para buscar las noticias
def get_news():
    url = "https://newsapi.org/v2/top-headlines?country=co&apiKey=6a22b9fffa3b44ed9ba394da947101da"
    response = requests.get(url)
    news_data = response.json()
    articles = news_data["articles"]
    headlines = ""
    for article in articles:
        headlines += article["title"] + ". "
    return headlines


# Configuramos el modelo en español
model_engine = "text-davinci-003"
# model_engine = "gpt-3.5-turbo"

#Buscar con chat GPT
def search_with_openIA():
    speak("¿Sobre qué tema quieres que investigue?")
    
    while True: 

        topic = recognize_speech(3)  # Obtener el tema de investigacion

        if topic == "salir":
            # speak('claro señor, dejare de consultar a chatGPT')
            break

        if topic == "déjame escribirte":
            speak('ok señor, se ha habilitado la entrada de texto')
            texto = input()

            completado = openai.Completion.create(
            engine=model_engine ,prompt=texto, max_tokens=2048, n=1,
            stop=None,
            logprobs=10
            # timeout=None,
            # presence_penalty=None,
            # frequency_penalty=None,
            # best_of=None,
            )

            respuesta = completado.choices[0].text

            speak(respuesta)
            print(respuesta)



            # break

        else:

            completado = openai.Completion.create(
            engine=model_engine ,prompt=topic, max_tokens=2048, n=1,
            stop=None,
            logprobs=10
            # timeout=None,
            # presence_penalty=None,
            # frequency_penalty=None,
            # best_of=None,
            )
            
            respuesta = completado.choices[0].text
            speak(respuesta)
            print(respuesta)


            # break

        
#usar segunda opcion
# Enviar la solicitud inicial al modelo
def segunda_opcion():

    speak("¿Sobre qué tema quieres que investigue?")

    topic = recognize_speech()

    while True: 
        if topic == "salir":
            # speak('claro señor, dejare de consultar a chatGPT')
            break
    
        # Define la URL de la solicitud y los parámetros
        url = "https://api.openai.com/v1/engines/text-davinci-003/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {openai.api_key}",
            "Transfer-Encoding": "chunked"
        }
        data = {
            "prompt": topic,
            "temperature": 0,
            "max_tokens": 2048,
            "n": 1,
            "stream": True
        }

        # Realiza la solicitud usando el método `request` de la biblioteca `requests`
        response = requests.post(url, headers=headers, json=data)

        # content = response.json()
        # print(content)
        # Imprime la respuesta
        for chunk in response.iter_content(chunk_size=None):
            if chunk:
                print(chunk.decode())
        
        break

#investigar en google
def search_google():

    speak("cual es tu consulta en google")

    query = recognize_speech()
    webbrowser.open("https://www.google.com/search?q=" + query)

#buscar el clima
api_clima = os.getenv('OPEN_WEATHER_MAP')

def pronostico():

    speak("en que ciudad de colombia quieres el reporte")

    ciudad = recognize_speech()

    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + ciudad + ',CO&appid=' + api_clima
    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        temperature = "Temperatura" + ciudad, data["main"]["temp"], "grados Celsius"
        humedad = "Humedad en" + ciudad, data["main"]["humidity"], "%"
        description = "Descripción del clima en " + ciudad, data["weather"][0]["description"]

        speak(temperature)
        print(temperature)

        speak(humedad)
        print(humedad)

        speak(description)
        print(description)
    
    else:
         speak('actualmente no puedo obtener la respuesta me disculpo')
         print("Error al realizar la solicitud a la API:", response.status_code)


def escuchar_music():

    # youtube_music_position = None

    try:
        youtube_music_window = findwindows.find_window(title_re=".*YouTube Music*.")

        time_module.sleep(2)

        youtube_music_app = Application().connect(handle=youtube_music_window)


    except findwindows.WindowNotFoundError:
        
        # webbrowser.open("https://music.youtube.com/")
        os.startfile("C:\\Users\\USER\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Aplicaciones de Chrome\\YouTube Music")
        time_module.sleep(2)
       
        youtube_music_window = findwindows.find_window(title_re=".*YouTube Music*.")

        time_module.sleep(1)

        youtube_music_app = Application().connect(handle=youtube_music_window)


    youtube_music_app_dialog = youtube_music_app.window(title_re=".*YouTube Music*.")
    youtube_music_app_dialog.set_focus()
    youtube_music_position = get_window_position(youtube_music_window)

    screen = youtube_music_position[2]

    print(screen)    

    time_module.sleep(1)  # Esperar para asegurarse de que el control esté cargado

    speak('Que accion quieres realizar')

    comand = recognize_speech()

    x = None
    y = None
    doble = False

    pantalla_principal = 2576

    # 2576

    if comand == 'primera de vuelve a escucharlo':
        # Haz clic el la primera eleccion de la lista 
        x = 731 if screen == pantalla_principal else 429 # -302 diferencia
        y = 509 if screen == pantalla_principal else 515 # +6 diferencia
        

    elif comand == 'segunda de vuelve a escucharlo':
        x = 1156 if screen == pantalla_principal else 854
        y = 514  if screen == pantalla_principal else 520

    elif comand == 'volver al inicio':
        x = 66
        y = 132

    elif comand == 'pausar canción' or comand == 'reproducir canción':
        x = 78 if screen == pantalla_principal else 80
        y = 1357 if screen == pantalla_principal else 1000

    elif comand == 'siguiente canción':
        x = 141 if screen == pantalla_principal else 143
        y = 1352 if screen == pantalla_principal else 1000 

    elif comand == 'anterior canción':
        x = 30 if screen == pantalla_principal else 30
        y = 1356 if screen == pantalla_principal else 1000
        doble = True

    elif comand == 'dar me gusta':
        x = 1545 if screen == pantalla_principal else 1242
        y = 1356 if screen == pantalla_principal else 1000

    elif comand == 'pestaña 1':
        x = 66 
        y = 10

    elif comand == 'obtener elemento' or comand == 'tener elemento':

        # Obtener la posición actual del cursor del mouse
        posicion_actual = pyautogui.position()

        print("La posición actual del cursor del mouse es:", posicion_actual)
        speak('ya obtuve la posición actual del cursor')

    else:
        speak('no pude entender lo que dices')


    if x != None and y != None:
        if doble == False:
            youtube_music_app_dialog.click_input(coords=(x, y))
        else:
            youtube_music_app_dialog.double_click_input(coords=(x, y))


# def movimiento_chrome():
#     windows = findwindows.find_windows()

#     app = Application(backend='uia')
#     app.connect(title_re=".*- Google Chrome -*")
#     windows = app.windows()
#     for w in windows:
#         print(w.texts())
    
#         w.set_focus()



def movimiento_chrome():

    windows = findwindows.find_windows()

    app = Application(backend='uia')
    app.connect(title_re=".* - Google Chrome -*", found_index=0)
    windows = app.windows()
    for w in windows:
        print(w.texts())
    
        w.set_focus()

        speak('a cual tab te quieres mover')

        tab = recognize_speech()

        if tab == 'uno':

            w.click_input(coords=(60, 10))

        elif tab == 'dos' or tab == "2":
            
            w.click_input(coords=(400, 10))
        
        break

    # "C:\Users\USER\Desktop\YouTube Music.lnk"


WAIT_TIME = 0.5 # segundos de espera entre solicitudes
last_request_time = time_module.time() - WAIT_TIME # asegurarse de que la primera solicitud se hace de inmediato

def activate_asistente():
    global asistente_activado
    asistente_activado = True
    speak("¿En qué puedo ayudarte?")

# Función para desactivar el asistente
def deactivate_asistente():
    global asistente_activado
    asistente_activado = False
    speak("Hasta pronto")

while True:

    current_time = time_module.time()
    elapsed_time = current_time - last_request_time

    if elapsed_time > WAIT_TIME:
         last_request_time = current_time

    if not asistente_activado:
        speech_text = recognize_speech()

        if speech_text:
            if "asís" in speech_text:
                asistente_activado = True
                speak("¡Hola! ¿En qué puedo ayudarte?")
                continue
            else:
                continue
    else:
        speech_text = recognize_speech()
        if speech_text:
            if "adiós" in speech_text:
                asistente_activado = False
                speak("¡Hasta pronto!")
                volumen_down()
                break

            elif "abrir" in speech_text:
                app_name = speech_text.split()[1]
                open_application(app_name)
                asistente_activado = False
                continue

            elif "cerrar" in speech_text:
                app_name = speech_text.split()[1]
                close_application(app_name)
                asistente_activado = False
                continue

            elif "buscar" in speech_text:
                open_website(speech_text)
                asistente_activado = False
                continue

            elif "dime la hora" in speech_text:
                locale.setlocale(locale.LC_TIME, "es_ES.utf8")
                current_time = time_module.strftime("%H:%M")
                speak(f"Son las {current_time}")
                asistente_activado = False
                continue

            elif "dime la fecha" in speech_text:
                locale.setlocale(locale.LC_ALL, 'es_ES')
                speak("Hoy es " + time_module.strftime("%A %d de %B de %Y"))
                asistente_activado = False
                continue

            elif "dime las noticias" in speech_text:
                news = get_news()
                speak("Aquí están las últimas noticias. " + news)
                asistente_activado = False
            
            elif "investiga" in speech_text:
                search_with_openIA()
                # segunda_opcion()
                asistente_activado = False

            elif "ve a google" in speech_text:
                search_google()
                asistente_activado = False


            elif "dime el clima" in speech_text:
                pronostico()
                asistente_activado = False
            
            elif "control música" in speech_text:
                escuchar_music()
                asistente_activado = False

            elif "moverme" in speech_text:
                movimiento_chrome()
                asistente_activado = False

            elif "dile a los muchachos" in speech_text:
                speak("señores mi creador esta ocupado programandome, en un momento estara disponible para jugar...")

            else:
                speak("Lo siento, no he entendido lo que has dicho")
                continue

        else:
            continue

        

    