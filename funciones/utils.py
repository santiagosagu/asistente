import win32gui
import pyautogui
import pyttsx3
import cv2
import pytesseract
import numpy as np
from PIL import Image
from pycaw.pycaw import AudioUtilities
import json
import random

engine = pyttsx3.init()


# Función para hablar
def speak(text):
    engine.say(text)
    engine.runAndWait()

# obtener la posicion


def get_window_position(hwnd):
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    width = rect[2] - x
    height = rect[3] - y
    return (x, y, width, height)


# obtener la posicion relativa de la ventana
def get_window_position_relative(left, top):
    pos_x, pos_y = pyautogui.position()
    pos_x -= left
    pos_y -= top

    print(f"Posición en pantalla: ({pos_x}, {pos_y})")
    speak('ya obtuve la posición actual del cursor')

    return (pos_x, pos_y)


# bajar el volumen cuando se espera el comando
def volumen_down(asistente_activado):

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


def screenshot_window(dialog):
    screenshot = dialog.capture_as_image()

    gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)
    image = Image.fromarray(gray)

    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    pytesseract.pytesseract.TESSDATA_PREFIX = 'C:\\Program Files\\Tesseract-OCR\\tessdata'

    result = pytesseract.image_to_data(
        image, output_type=pytesseract.Output.DICT, lang='spa')

    return result


def obtener_coordenadas_de_palabras(result, wordUser, comand):
    print(result['text'])

    for i, word in enumerate(result['text']):
        word = word.lower()
        if word == wordUser:
            x = result['left'][i]
            y = result['top'][i]
            w = result['width'][i]
            h = result['height'][i]
            print(x, y, w, h)
            # youtube_app_dialog.click_input(coords=(x, y))

            # return True
            return (x, y, w, h, word, comand)

    # Imprime el valor de x para verificar si se encontró la palabra o no
    # print(f"Valor de x: {x}")


def obtener_palabra_en_coordenadas(result, x, y):
    words = []
    for i, word in enumerate(result['text']):
        word = word.lower()
        word_x = result['left'][i]
        word_y = result['top'][i]
        word_w = result['width'][i]
        word_h = result['height'][i]
        words.append({'word': word, 'x': word_x,
                      'y': word_y, 'w': word_w, 'h': word_h})

    # Busca si hay una palabra en las coordenadas dadas
    for word_info in words:
        if word_info['x'] == x and word_info['y'] == y:
            return word_info['word']

    # Si no se encontró ninguna palabra en las coordenadas dadas, devuelve None
    return None


def generar_numeros_random():
    numeros = []
    for i in range(5):
        numeros.append(random.randint(1, 100))
    return ' '.join(map(str, numeros))


def verification_user(recognize_speech):
    # Leer el archivo JSON existente
    with open('config.json', 'r') as f:
        data = json.load(f)

    if 'False' == data['user']['user_confirmado']:

        speak('Parece que es tu primera vez. Me presento, soy tu nuevo asistente, me llamo a sis, estoy para ayudarte en tus tareas. Puedes ver todas mis funcionalidades en mi documentacion en la siguiente pagina web')

        print('https://www.facebook.com/')

        speak('Bueno para comenzar necesito configurar tu primer nombre, para saber como guardare tus comandos, recordatorios y demas')

        speak('Como te llamas:')

        nombre_user = recognize_speech()

        # numeros_aleatorios_str = generar_numeros_random()

        data['user']['name'] = f'{nombre_user}-{random.randint(1, 1000)}'

        data['user']['user_confirmado'] = 'True'

        with open('config.json', 'w') as f:
            json.dump(data, f)

        speak(f'Listo tu nombre se ha guardado como {nombre_user}')

        print(data)

        return (data['user']['name'], data['user']['user_confirmado'])

    else:
        return (data['user']['name'], data['user']['user_confirmado'])
