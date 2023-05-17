import time as time_module
import os
from pywinauto import Application, Desktop, findwindows, controls, win32functions

from funciones.subFuncionesMusica.reproduccion_aleatoria_me_gusta import reproduccion_aleatoria_me_gusta
from funciones.subFuncionesMusica.iniciar_radio import iniciar_radio
from funciones.subFuncionesMusica.interaccion_musica import pausar_reproducir_cancion, siguiente_canción, anterior_canción, repetir_canción
from funciones.utils import get_window_position, get_window_position_relative


def control_music(recognize_speech, speak, speech_text):

    try:
        youtube_music_window = findwindows.find_window(
            title_re=".*YouTube Music*.")

        time_module.sleep(1)

        youtube_music_app = Application().connect(handle=youtube_music_window)

    except findwindows.WindowNotFoundError:

        # webbrowser.open("https://music.youtube.com/")
        os.startfile(
            "C:\\Users\\USER\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Aplicaciones de Chrome\\YouTube Music")
        time_module.sleep(2)

        youtube_music_window = findwindows.find_window(
            title_re=".*YouTube Music*")

        time_module.sleep(1)

        youtube_music_app = Application().connect(handle=youtube_music_window)

    youtube_music_app_dialog = youtube_music_app.window(
        title_re=".*YouTube Music*.")
    youtube_music_app_dialog.set_focus()

    x = None
    y = None

    pantalla_principal = 2576
    width_ventana_in_pantalla_principal = 1265

    segunda_pantalla = 1936
    width_ventana_segunda_pantalla = 1265

    youtube_music_position = get_window_position(youtube_music_window)
    time_module.sleep(1)
    screen = youtube_music_position[2]
    left = youtube_music_position[0]
    top = youtube_music_position[1]

    print(screen)

    if "pon música" in speech_text or "pon la música" in speech_text or "pon los temas" in speech_text or "quiero" in speech_text:
        speak('vale. pondre la lista de me gusta.')
        reproduccion_aleatoria_me_gusta(x, y, screen, pantalla_principal, width_ventana_in_pantalla_principal,
                                        segunda_pantalla, width_ventana_segunda_pantalla, youtube_music_app_dialog)

        return None

    elif "pausar" in speech_text or "reproducir" in speech_text:
        pausar_reproducir_cancion(x, y, screen, pantalla_principal, width_ventana_in_pantalla_principal,
                                  segunda_pantalla, width_ventana_segunda_pantalla, youtube_music_app_dialog)

        return None

    elif "siguiente" in speech_text:
        siguiente_canción(x, y, screen, pantalla_principal, width_ventana_in_pantalla_principal,
                           segunda_pantalla, width_ventana_segunda_pantalla, youtube_music_app_dialog)

        return None

    elif "anterior" in speech_text:
        anterior_canción(x, y, screen, pantalla_principal, width_ventana_in_pantalla_principal,
                          segunda_pantalla, width_ventana_segunda_pantalla, youtube_music_app_dialog)

        return None

    elif "repetir" in speech_text:
        repetir_canción(x, y, screen, pantalla_principal, width_ventana_in_pantalla_principal,
                         segunda_pantalla, width_ventana_segunda_pantalla, youtube_music_app_dialog)

        return None

    elif "radio" in speech_text:
        iniciar_radio(x, y, screen, pantalla_principal, width_ventana_in_pantalla_principal,
                      segunda_pantalla, width_ventana_segunda_pantalla, youtube_music_app_dialog)

        return None

    elif "control" in speech_text:
        speak("quieres obtener la posicion del elemento")

        confirmacion = recognize_speech()

        print(confirmacion)

        if 'sí' in confirmacion:
            get_window_position_relative(left, top)

    else:
        speak('no puede interpretar que querias hacer')
        return None
