import locale
import pprint
import time as time_module
from playsound import playsound
import datetime
import pygame
import dateparser
import wit
from dotenv import load_dotenv
import os

load_dotenv()

# Crea un cliente de Wit con tu token
wit_client = os.getenv('WIT_API')

client = wit.Wit(wit_client)

# Obtener la hora


def hora_local(speak):
    locale.setlocale(locale.LC_TIME, "es_ES.utf8")
    current_time = time_module.strftime("%H:%M")
    speak(f"Son las {current_time}")

# Obtener la fecha


def fecha_local(speak):
    locale.setlocale(locale.LC_ALL, 'es_ES')
    speak("Hoy es " + time_module.strftime("%A %d de %B de %Y"))


# Crear Recordatorios
pygame.init()

pausado = True

recordatorios = []


def agregar_recordatorio(recognize_speech, speak):

    speak("que mensaje le quieres poner al recordatorio ")

    mensaje = recognize_speech(10)

    speak('Para que fecha quieres agendar el recordatorio')
    fecha_hora = recognize_speech(10)

    resultado = client.message(fecha_hora)

    entidades = resultado.get("entities")

    pprint.pprint(entidades)

    fecha_hora = None

    if "wit$datetime:datetime" in entidades:

        if "value" in entidades["wit$datetime:datetime"][0]:
            fecha_hora = entidades["wit$datetime:datetime"][0]["value"]
            fecha = datetime.datetime.strptime(
                fecha_hora, "%Y-%m-%dT%H:%M:%S.%f%z")
            recordatorio = (mensaje, fecha)
            print(recordatorio)

            speak('listo, se ha creado el recordatorio')

            return recordatorio

        elif len(entidades["wit$datetime:datetime"]) > 0 and "values" in entidades["wit$datetime:datetime"][0]:
            fecha_hora = entidades["wit$datetime:datetime"][0]["values"][0]['to']['value']
            fecha = datetime.datetime.strptime(
                fecha_hora, "%Y-%m-%dT%H:%M:%S.%f%z")
            recordatorio = (mensaje, fecha)
            print(recordatorio)

            speak('listo se ha creado el recordatorio')

            return recordatorio

        else:
            speak(
                'Lo siento, no pude entender la fecha y hora del recordatorio. Por favor, inténtalo de nuevo.')

            return None
    else:
        print("No se encontró información de fecha y hora en el comando.")

        return None


def programar_recordatorios(speak):

    pygame.mixer.music.load(
        'D:\\estudio\\asistente-con-python\\ringtone\\la-atmosfera_4.mp3')

    while True:
        ahora = datetime.datetime.now()
        for i, (mensaje, hora_recordatorio) in enumerate(recordatorios):

            # ahora_con_timezone = ahora.astimezone(datetime.timedelta(days=-1, seconds=68400))
            ahora_con_timezone = ahora.astimezone(
                datetime.timezone(datetime.timedelta(days=-1, seconds=68400)))

            if ahora_con_timezone >= hora_recordatorio:
                print("Recordatorio:", mensaje)
                pausado = False

                speak('se ha cumplido el tiempo del recordatorio:' + mensaje)
                pygame.mixer.music.play()
                speak('se ha cumplido el tiempo del recordatorio:' + mensaje)
                del recordatorios[i]

                time_module.sleep(1)
                break

                # Espera hasta que termine de reproducirse la canción
                # while pygame.mixer.music.get_busy():
                #     if pausado:
                #         pygame.mixer.music.pause()
                #     else:
                #         pygame.mixer.music.unpause()

        break


def listar_recordatorios(speak):

    speak('estos son los siguientes recordatorios pendientes')

    for recordatorio in recordatorios:
        año = recordatorio[1].year
        mes = recordatorio[1].month
        dia = recordatorio[1].day
        hora = recordatorio[1].hour
        minutos = recordatorio[1].minute

        speak(f'{recordatorio[0]}, año: {año}, mes: {mes}, dia: {dia}, hora: {hora}:{minutos}')


def prueba_escuchar_musica(recognize_speech, speak):

    speak('que quieres hacer')
    comando = recognize_speech(10)

    resultado = client.message(comando)

    entidades = resultado.get("entities")

    pprint.pprint(entidades)
