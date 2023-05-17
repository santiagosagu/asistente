import speech_recognition as sr
import os
import pprint
import time as time_module
import wit
from dotenv import load_dotenv

from funciones.abrir_paginas import open_website
from funciones.clima import pronostico
from funciones.conection_chatGPT import search_with_openIA
from funciones.control_aplicaciones import open_application, close_application
from funciones.control_musica import control_music
from funciones.info_cotidiana import hora_local, fecha_local, recordatorios, agregar_recordatorio, programar_recordatorios, listar_recordatorios, prueba_escuchar_musica
from funciones.info_noticias import get_news
from funciones.verificacion_app_video import verificacion_app_video
from funciones.utils import speak, volumen_down, verification_user
from firebaseClient.enpoints_recordatorios import crear_registro_recordatorio
from funciones.scraping_mercado_libre import scraping_mercado_libre
from funciones.subFuncionesNoticias.noticias_del_mundo import get_news_mundo, get_news_espn_fox, get_news_video_juegos, get_news_tecnologia

# Variable para detectar la palabra clave "asís"
asistente_activado = False


load_dotenv()

wit_client = os.getenv('WIT_API')

client = wit.Wit(wit_client)


# Configuración de las librerías
r = sr.Recognizer()

# Configuración del reconocedor de voz
r.energy_threshold = 100  # Ajustar este valor según tu entorno
# Habilitar ajuste dinámico del umbral de energía
r.dynamic_energy_threshold = True


def recognize_speech(max_duration=3):

    with sr.Microphone() as source:
        if asistente_activado:
            volumen_down(asistente_activado)
            print("Esperando...")

            audio = r.listen(source, phrase_time_limit=max_duration)

        else:
            print("Llamame Asís y podre ayudarte... ")
            volumen_down(asistente_activado)

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


def activate_asistente():
    global asistente_activado
    asistente_activado = True
    speak("¿En qué puedo ayudarte?")


def deactivate_asistente():
    global asistente_activado
    asistente_activado = False
    speak("Hasta pronto")


while True:

    # get_news_mundo()
    # get_news_espn_fox()
    # get_news_video_juegos()
    # get_news_tecnologia()

    user = verification_user(recognize_speech)

    if user[0] is not None:
        programar_recordatorios(speak)

    if not asistente_activado:
        speech_text = recognize_speech()

        if speech_text:
            if "asís" in speech_text or "así" in speech_text:
                asistente_activado = True
                speak(
                    f"¡Hola {user[0].split('-')[0]}!  ¿En qué puedo ayudarte?")
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
                volumen_down(asistente_activado)
                break

            # elif len(entidades) > 1:
            #     # el diccionario tiene más de una clave
            #     speak(
            #         'He optenido varias opciones te recomiendo que la añadas a mi modelo o intenta decirlo de otra forma')
            #     continue

            elif "buscar_ofertas:buscar_ofertas" in entidades:
                comand = entidades['buscar_ofertas:buscar_ofertas'][0]['value']

                product = None

                if "busqueda_ofertas:busqueda_ofertas" in entidades:
                    product = entidades['busqueda_ofertas:busqueda_ofertas'][0]['value']

                print(comand)
                print(product)

                # volumen_down(False)

                scraping_mercado_libre(product, recognize_speech)
                asistente_activado = False

            elif "investiga" in speech_text:
                search_with_openIA(recognize_speech, speak)
                asistente_activado = False

            elif "listar_recordatorios:listar_recordatorios" in entidades:
                listar_recordatorios(speak)
                asistente_activado = False

            elif "wit$reminder:reminder" in entidades:
                recordatorio = agregar_recordatorio(recognize_speech, speak)
                crear_registro_recordatorio(recordatorio)
                # recordatorios.append(recordatorio)
                asistente_activado = False

            elif "abrir_programa:abrir_programa" in entidades:
                open_application(speech_text, recognize_speech)
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

                control_music(recognize_speech, speak, speech_text)
                asistente_activado = False

            elif "control_video:control_video" in entidades:
                verificacion_app_video(speech_text, recognize_speech)

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

            elif "prueba mercado" in speech_text:
                asistente_activado = False

                volumen_down(False)

                scraping_mercado_libre(speech_text)

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
