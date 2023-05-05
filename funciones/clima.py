import requests
from dotenv import load_dotenv
import os

load_dotenv()

# buscar el clima
api_clima = os.getenv('OPEN_WEATHER_MAP')


def pronostico(recognize_speech, speak):

    speak("en que ciudad de colombia quieres el reporte")

    ciudad = recognize_speech()

    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + \
        ciudad + ',CO&lang=es&units=metric&appid=' + api_clima
    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        temperature = "Temperatura" + \
            ciudad, data["main"]["temp"], "grados Celsius"
        humedad = "Humedad en" + ciudad, data["main"]["humidity"], "%"
        description = "Descripción del clima en " + \
            ciudad, data["weather"][0]["description"]

        speak(temperature)
        print(temperature)

        speak(humedad)
        print(humedad)

        speak(description)
        print(description)

    else:
        speak('actualmente no puedo obtener la respuesta me disculpo')
        print("Error al realizar la solicitud a la API:", response.status_code)
