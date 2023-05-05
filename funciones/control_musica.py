
from pywinauto import Application, Desktop, findwindows, controls, win32functions
import time as time_module
import os
import win32gui
import pyautogui


def get_window_position(hwnd):
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    width = rect[2] - x
    height = rect[3] - y
    return (x, y, width, height)


def control_music(recognize_speech, speak):

    # youtube_music_position = None

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
            title_re=".*YouTube Music*.")

        time_module.sleep(1)

        youtube_music_app = Application().connect(handle=youtube_music_window)

    youtube_music_app_dialog = youtube_music_app.window(
        title_re=".*YouTube Music*.")
    youtube_music_app_dialog.set_focus()

    speak('Que accion quieres realizar')

    while True:

        youtube_music_position = get_window_position(youtube_music_window)

        screen = youtube_music_position[2]
        left = youtube_music_position[0]
        top = youtube_music_position[1]

        print(screen)

        # Esperar para asegurarse de que el control esté cargado
        time_module.sleep(1)

        comand = recognize_speech(8)

        x = None
        y = None
        doble = False

        pantalla_principal = 2576
        width_ventana_in_pantalla_principal = 1265

        segunda_pantalla = 1936
        width_ventana_segunda_pantalla = 1265

        if comand == 'vuelve a escucharlo':

            if screen == pantalla_principal:
                x = 730
                y = 434

            elif screen == width_ventana_in_pantalla_principal:

                x = 279
                y = 390

            elif screen == segunda_pantalla:
                x = 410
                y = 439

            elif screen == width_ventana_segunda_pantalla:
                x = 270
                y = 392

            youtube_music_app_dialog.click_input(coords=(x, y))

            break

        elif comand == 'volver al inicio':

            if screen == pantalla_principal:
                x = 60
                y = 63
            elif screen == width_ventana_in_pantalla_principal:
                x = 68
                y = 63
            elif screen == segunda_pantalla:
                x = 76
                y = 66
            elif screen == width_ventana_segunda_pantalla:
                x = 78
                y = 64

            youtube_music_app_dialog.click_input(coords=(x, y))

            break

        elif comand == 'pausar canción' or comand == 'reproducir canción':
            if screen == pantalla_principal:
                x = 91
                y = 1358
            elif screen == width_ventana_in_pantalla_principal:
                x = 93
                y = 995
            elif screen == segunda_pantalla:
                x = 90
                y = 1003
            elif screen == width_ventana_segunda_pantalla:
                x = 93
                y = 990

            youtube_music_app_dialog.click_input(coords=(x, y))

            break

        elif comand == 'siguiente canción' or comand == 'canción siguiente':
            if screen == pantalla_principal:
                x = 146
                y = 1365
            elif screen == width_ventana_in_pantalla_principal:
                x = 149
                y = 992
            elif screen == segunda_pantalla:
                x = 145
                y = 1004
            elif screen == width_ventana_segunda_pantalla:
                x = 146
                y = 994

            youtube_music_app_dialog.click_input(coords=(x, y))

            break

        elif comand == 'anterior canción' or comand == 'canción anterior':
            if screen == pantalla_principal:
                x = 34
                y = 1366
            elif screen == width_ventana_in_pantalla_principal:
                x = 36
                y = 994
            elif screen == segunda_pantalla:
                x = 32
                y = 1004
            elif screen == width_ventana_segunda_pantalla:
                x = 34
                y = 992

            doble = True
            youtube_music_app_dialog.double_click_input(coords=(x, y))

            break

        elif comand == 'repetir canción':
            if screen == pantalla_principal:
                x = 34
                y = 1366
            elif screen == width_ventana_in_pantalla_principal:
                x = 36
                y = 994
            elif screen == segunda_pantalla:
                x = 32
                y = 1004
            elif screen == width_ventana_segunda_pantalla:
                x = 34
                y = 992

            youtube_music_app_dialog.click_input(coords=(x, y))

            break

        elif comand == 'dar me gusta':
            if screen == pantalla_principal:
                x = 1504
                y = 1362
            elif screen == width_ventana_in_pantalla_principal:
                x = 823
                y = 998
            elif screen == segunda_pantalla:
                x = 1185
                y = 1004
            elif screen == width_ventana_segunda_pantalla:
                x = 825
                y = 997

            youtube_music_app_dialog.click_input(coords=(x, y))

            break

        elif comand == 'iniciar radio':
            if screen == pantalla_principal:
                x = 1558
                y = 1365
            elif screen == width_ventana_in_pantalla_principal:
                x = 823
                y = 998
            elif screen == segunda_pantalla:
                x = 1185
                y = 1004
            elif screen == width_ventana_segunda_pantalla:
                x = 825
                y = 997

            youtube_music_app_dialog.click_input(coords=(x, y))

            if screen == pantalla_principal:
                x = 1636
                y = 868
            elif screen == width_ventana_in_pantalla_principal:
                x = 823
                y = 998
            elif screen == segunda_pantalla:
                x = 1185
                y = 1004
            elif screen == width_ventana_segunda_pantalla:
                x = 825
                y = 997

            youtube_music_app_dialog.click_input(coords=(x, y))

            break

        elif comand == 'baja':
            youtube_music_app_dialog.click_input(coords=(76, 310))
            pyautogui.scroll(-560)

        elif comand == 'obtener elemento' or comand == 'tener elemento':

            # Calculamos la posición en la pantalla relativa a la ventana
            pos_x, pos_y = pyautogui.position()
            pos_x -= left
            pos_y -= top

            # Imprimimos la posición en la pantalla
            print(f"Posición en pantalla: ({pos_x}, {pos_y})")
            speak('ya obtuve la posición actual del cursor')

            break

        else:
            speak('no pude entender lo que dices')
