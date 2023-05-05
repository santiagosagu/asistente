import time as time_module
from pycaw.pycaw import AudioUtilities
import pyttsx3
import speech_recognition as sr
from funciones.abrir_paginas import open_website
from funciones.clima import pronostico
from funciones.conection_chatGPT import search_with_openIA
from funciones.control_aplicaciones import open_application, close_application
from funciones.control_musica import control_music
from funciones.info_cotidiana import hora_local, fecha_local, recordatorios, agregar_recordatorio, programar_recordatorios, listar_recordatorios, prueba_escuchar_musica
from funciones.info_noticias import get_news
import datetime
import wit
import pprint
from dotenv import load_dotenv
import os

# Variable para detectar la palabra clave "asís"
asistente_activado = False
microphone_always_on = False


wit_client = os.getenv('wit.client')

client = wit.Wit(wit_client)


# Configuración de las librerías
engine = pyttsx3.init()
r = sr.Recognizer()

# Configuración del reconocedor de voz
r.energy_threshold = 100  # Ajustar este valor según tu entorno
# Habilitar ajuste dinámico del umbral de energía
r.dynamic_energy_threshold = True


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


def recognize_speech(max_duration=3):

    global microphone_always_on  # Definir la variable como global

    with sr.Microphone() as source:
        if asistente_activado:
            volumen_down()
            print("Esperando...")

            audio = r.listen(source, phrase_time_limit=max_duration)

        else:
            print("Llamame Asís y podre ayudarte... ")
            volumen_down()

            # Grabar hasta 2 segundos como máximo
            audio = r.listen(source, phrase_time_limit=1.5)

        try:
            speech_text = r.recognize_google(audio, language="es-ES")
            print(f"Has dicho: {speech_text}")
            return speech_text.lower()

        except sr.UnknownValueError:
            # speak("Lo siento, no he entendido lo que has dicho. ¿Puedes repetirlo?")
            return None

        except sr.RequestError as e:
            print(
                f"No se pudo realizar la solicitud a Google Speech Recognition service; {e}")
            return None


WAIT_TIME = 0.5  # segundos de espera entre solicitudes
# asegurarse de que la primera solicitud se hace de inmediato
last_request_time = time_module.time() - WAIT_TIME


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

    programar_recordatorios(speak)

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

            resultado = client.message(speech_text)

            entidades = resultado.get("entities")

            pprint.pprint(entidades)

            if "adiós" in speech_text:
                asistente_activado = False
                speak("¡Hasta pronto!")
                volumen_down()
                break

            elif len(entidades) > 1:
                # el diccionario tiene más de una clave
                speak(
                    'He optenido varias opciones te recomiendo que la añadas a mi modelo o intenta decirlo de otra forma')
                continue

            elif "investiga" in speech_text:
                search_with_openIA(recognize_speech, speak)
                asistente_activado = False

            elif "listar_recordatorios:listar_recordatorios" in entidades:
                listar_recordatorios(speak)
                asistente_activado = False

            elif "wit$reminder:reminder" in entidades:
                recordatorio = agregar_recordatorio(recognize_speech, speak)
                recordatorios.append(recordatorio)
                asistente_activado = False

            elif "abrir_programa:abrir_programa" in entidades:
                open_application(speech_text, speak)
                asistente_activado = False

            elif "cerrar_programa:cerrar_programa" in entidades:
                close_application(speech_text, speak)
                asistente_activado = False

            elif "dar_la_hora:dar_la_hora" in entidades:
                hora_local(speak)
                asistente_activado = False

            elif "dar_la_fecha:dar_la_fecha" in entidades:
                fecha_local(speak)
                asistente_activado = False

            elif "dar_las_noticias:dar_las_noticias" in entidades:
                news = get_news()
                speak("Aquí están las últimas noticias. " + news)
                speak('Esas son todas las noticias')
                asistente_activado = False

            elif "dar_el_clima:dar_el_clima" in entidades:
                pronostico(recognize_speech, speak)
                asistente_activado = False

            elif "escuchar_musica:escuchar_musica" in entidades:
                speak('encontre el comando para musica')

                control_music(recognize_speech, speak)
                asistente_activado = False

            # elif "abrir" in speech_text:
            #     app_name = speech_text.split()[1]
            #     open_application(app_name, speak)
            #     asistente_activado = False
            #     continue

            # elif "cerrar" in speech_text:
            #     app_name = speech_text.split()[1]
            #     close_application(app_name, speak)
            #     asistente_activado = False
            #     continue

            elif "buscar" in speech_text:
                open_website(speech_text, speak)
                asistente_activado = False
                continue

            # elif "dime la hora" in speech_text:
            #     hora_local(speak)
            #     asistente_activado = False
            #     continue

            # elif "dime la fecha" in speech_text:
            #     fecha_local(speak)
            #     asistente_activado = False
            #     continue

            # elif "dime las noticias" in speech_text:
            #     news = get_news()
            #     speak("Aquí están las últimas noticias. " + news)
            #     asistente_activado = False

            # elif "investiga" in speech_text:
            #     search_with_openIA(recognize_speech, speak)
            #     asistente_activado = False

            # elif "ve a google" in speech_text:
            #     search_google()
            #     asistente_activado = False

            # elif "dime el clima" in speech_text:
            #     pronostico(recognize_speech, speak)
            #     asistente_activado = False

            # elif "control música" in speech_text:
            #     control_music(recognize_speech, speak)
            #     asistente_activado = False

            # elif "recordatorio" in speech_text:
            #     recordatorio = agregar_recordatorio(
            #         recognize_speech, speak)
            #     recordatorios.append(recordatorio)

                # agregar_recordatorio("Comprar leche", "0.2h")
                # asistente_activado = False

            # elif "qué tengo pendiente" in speech_text:
            #     listar_recordatorios(speak)
            #     asistente_activado = False

            elif "prueba música" in speech_text:
                prueba_escuchar_musica(recognize_speech, speak)
                asistente_activado = False

            # elif "moverme" in speech_text:
            #     movimiento_chrome()
            #     asistente_activado = False

            elif "dile a los muchachos" in speech_text:
                speak(
                    "señores mi creador esta ocupado programandome, en un momento estara disponible para jugar...")

            else:
                speak("Lo siento, no he entendido lo que has dicho")
                continue

        else:
            continue
