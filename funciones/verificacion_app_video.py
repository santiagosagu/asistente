import time as time_module
from pywinauto import Application, Desktop, findwindows, controls, win32functions
import os
import webbrowser

from funciones.control_youTube import control_youTube


def verificacion_app_video(speech_text, recognize_speech):
    print(speech_text)

    youtube_window = None
    prime_window = None
    star_window = None
    hbo_window = None

    if not 'prime' in speech_text and not 'star' in speech_text and not 'hbo' in speech_text:

        try:
            youtube_window = findwindows.find_window(title_re=".*YouTube -*")

            if youtube_window:
                youtube_app = Application().connect(handle=youtube_window)

                control_youTube(youtube_app, youtube_window,
                                speech_text, recognize_speech)
                return

        except (findwindows.ElementNotFoundError, findwindows.WindowNotFoundError):
            pass

    if not youtube_window and not 'youtube' in speech_text and not 'star' in speech_text and not 'hbo' in speech_text:
        try:
            prime_window = findwindows.find_window(title_re=".*Prime Video -*")

            if prime_window:
                prime_app = Application().connect(handle=prime_window)

                print(prime_app)
                return

        except (findwindows.ElementNotFoundError, findwindows.WindowNotFoundError):
            pass

    if not youtube_window and not prime_window and not 'youtube' in speech_text and not 'prime' in speech_text and not 'hbo' in speech_text:
        try:
            star_window = findwindows.find_window(title_re=".*Star+ -*")

            if star_window:
                star_app = Application().connect(handle=star_window)

                print(star_app)
                return

        except (findwindows.ElementNotFoundError, findwindows.WindowNotFoundError):
            pass

    if not youtube_window and not prime_window and not star_window and not 'youtube' in speech_text and not 'prime' in speech_text and not 'star' in speech_text:

        try:
            hbo_window = findwindows.find_window(title_re=".*HBO Max -*")

            if hbo_window:
                hbo_app = Application().connect(handle=hbo_window)

                print(hbo_app)
                return

        except (findwindows.ElementNotFoundError, findwindows.WindowNotFoundError):
            pass

    if not youtube_window and not prime_window and not star_window and not hbo_window:

        if 'youtube' in speech_text:

            os.startfile(
                "C:\\Users\\USER\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Aplicaciones de Chrome\\YouTube")
            time_module.sleep(2)

            youtube_window = findwindows.find_window(title_re=".*YouTube -*")

            time_module.sleep(3)

            youtube_app = Application().connect(handle=youtube_window)

            control_youTube(youtube_app, youtube_window,
                            speech_text, recognize_speech)

            return

        if "prime" in speech_text:
            print('aqui cai')

            webbrowser.open('https://www.primevideo.com/')
            time_module.sleep(2)

            prime_window = findwindows.find_window(title_re=".*Prime Video -*")

            time_module.sleep(1)

            prime_app = Application().connect(handle=prime_window)

            print(prime_app)
            return

        if "star" in speech_text:

            webbrowser.open('https://www.starplus.com/es-419/home')
            time_module.sleep(2)

            star_window = findwindows.find_window(title_re=".*Star+ -*")

            time_module.sleep(1)

            star_app = Application().connect(handle=star_window)

            print(star_app)
            return

        if "hbo" in speech_text:

            webbrowser.open('https://play.hbomax.com/signIn')
            time_module.sleep(3)

            hbo_window = findwindows.find_window(title_re=".*HBO Max -*")

            time_module.sleep(1)

            hbo_app = Application().connect(handle=hbo_window)

            print(hbo_app)
            return
