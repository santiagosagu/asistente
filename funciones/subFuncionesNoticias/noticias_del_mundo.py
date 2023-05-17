import requests
from translate import Translator
from mtranslate import translate
from funciones.utils import speak
import time as time_module
import os
import datetime
import locale

# Crea una instancia del traductor
traductor = Translator(from_lang='en', to_lang='es')

idioma_destino = 'es'  # Idioma al que se desea traducir

locale.setlocale(locale.LC_ALL, 'es_ES')
hoy = time_module.strftime("%Y-%m-%d")

key_news = os.getenv('NEWS')


locale.setlocale(locale.LC_ALL, 'es_ES')

# Obtener la fecha de hoy
hoy = datetime.date.today()

# Obtener la fecha de ayer
ayer = hoy - datetime.timedelta(days=1)

# Formatear la fecha de ayer
fecha_ayer = ayer.strftime("%Y-%m-%d")
fecha_hoy = hoy.strftime("%Y-%m-%d")


def get_news_mundo():

    speak("Aquí están las últimas noticias del mundo. ")

    url = f"https://newsapi.org/v2/top-headlines?language=en&apiKey={key_news}"
    response = requests.get(url)
    news_data = response.json()
    articles = news_data["articles"]
    titulo = ""
    descripcion = None
    for article in articles:
        titulo = article["title"]
        url = article["url"]
        if article["description"]:
            descripcion = article["description"]
            text = translate(f'{titulo}. {descripcion}. ',
                             to_language=idioma_destino)
            speak(text)
            print(titulo, url)

    speak('Esas son todas las noticias')


def get_news_espn_fox():

    speak("Aquí están las últimas noticias de deportes. ")

    url = f"https://newsapi.org/v2/everything?sources=espn,fox-sports&language=en&from={fecha_ayer}&to={fecha_hoy}&apiKey={key_news}"
    response = requests.get(url)
    news_data = response.json()
    articles = news_data["articles"]
    titulo = ""
    descripcion = None
    for article in articles:
        titulo = article["title"]
        url = article["url"]
        if article["description"]:
            descripcion = article["description"]
            text = translate(f'{titulo}. {descripcion}. ',
                             to_language=idioma_destino)
            speak(text)
            print(titulo, url)

    speak('Esas son todas las noticias')


def get_news_video_juegos():

    speak("Aquí están las últimas noticias del mundo geimer. ")

    url = f"https://newsapi.org/v2/everything?sources=polygon&language=en&from={fecha_ayer}&to={fecha_hoy}&apiKey={key_news}"
    response = requests.get(url)
    news_data = response.json()
    articles = news_data["articles"]
    titulo = ""
    descripcion = None
    for article in articles:
        titulo = article["title"]
        url = article["url"]
        if article["description"]:
            descripcion = article["description"]
            text = translate(f'{titulo}. {descripcion}. ',
                             to_language=idioma_destino)
            speak(text)
            print(titulo, url)

    speak('Esas son todas las noticias')


def get_news_tecnologia():

    speak("Aquí están las últimas noticias de tecnologia. ")

    url = f"https://newsapi.org/v2/everything?sources=the-next-web,techradar,techcrunch,engadget&language=en&from={fecha_ayer}&to={fecha_hoy}&apiKey={key_news}"
    response = requests.get(url)
    news_data = response.json()
    articles = news_data["articles"]
    titulo = ""
    descripcion = None
    for article in articles:
        titulo = article["title"]
        url = article["url"]
        if article["description"]:
            descripcion = article["description"]
            text = translate(f'{titulo}. {descripcion}. ',
                             to_language=idioma_destino)
            speak(text)
            print(titulo, url)

    speak('Esas son todas las noticias')
