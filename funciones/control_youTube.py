import time as time_module
from funciones.utils import get_window_position, obtener_palabra_en_coordenadas, obtener_coordenadas_de_palabras, screenshot_window, speak

from funciones.subFuncionesYoutube.utils_youtube import nuevo_comando_youtube, agregar_nueva_resolucion_youtube

from firebaseClient import enpoints_youtube


def control_youTube(youtube_app, youtube_window, speech_text, recognize_speech):

    youtube_app_dialog = youtube_app.window(
        title_re=".*YouTube -*.")

    youtube_app_dialog.set_focus()

    pantalla_principal = 2576
    width_ventana_in_pantalla_principal = 1265

    segunda_pantalla = 1936
    width_ventana_segunda_pantalla = 1265

    youtube_position = get_window_position(youtube_window)
    time_module.sleep(1)
    screen = youtube_position[2]
    height = youtube_position[3]
    left = youtube_position[0]
    top = youtube_position[1]

    print(screen, 'screen')

    if youtube_app_dialog is not None:

        result = screenshot_window(youtube_app_dialog)

        x_coord = 81
        y_coord = 501

        # word = obtener_palabra_en_coordenadas(
        #     result, x_coord, y_coord)

        # controls = [{'word': 'premium', 'comand': 'premium'}, {'word': 'suscripciones', 'comand': 'suscripciones'}, {'word': 'mibiblioteca', 'comand': 'mi biblioteca'}, {
        #     'word': 'historial', 'comand': 'historial'}, {'word': 'misvídeos', 'comand': 'mis vídeos'}, {'word': 'vermástarde', 'comand': 'ver más tarde'}, {'word': 'descargas', 'comand': 'descargas'}]
        # control_coord = []

        # for control in controls:

        #     word_position = obtener_coordenadas_de_palabras(
        #         result, control['word'].lower(), control['comand'].lower())

        #     if word_position:
        #         print(word_position[0], word_position[1], word_position[4])
        #         control_coord.append(
        #             {'word': word_position[4], 'x': word_position[0], 'y': word_position[1], 'comand': word_position[5]})

        # print(control_coord)

        # youtube_app_dialog.click_input(
        #     coords=(x_coord, y_coord))

        # 1936
        # config.crear_registro()
        data = enpoints_youtube.traer_registros()

        if 'configuración' in speech_text:

            speak('vale estoy lista para guardar tus configuraciones. Aqui puedes agregar un nuevo comando a alguna ventana de youtube que ya tengas configurada, o añadir una nueva resolucion de la ventana de youtube. Recuerda que si es tu primera vez o quieres agregar un comando a una resolucíon nueva de la ventana de youtube primero debes agregar una ventana')

            speak('Si quieres agregar un nuevo comando, por favor di, nuevo comando')

            speak(
                'si quieres agregar una nueva resolucíon a la ventana de youtube, di nueva ventana')

            time_module.sleep(1)

            speak('que accion quieres realizar')

            word = recognize_speech()

            if word == 'nuevo comando':
                nuevo_comando_youtube(recognize_speech, left, top, screen)

            if word == 'nueva ventana':
                agregar_nueva_resolucion_youtube(
                    screen, left, top, recognize_speech)

            return None

        if data is None:
            print('No hay datos')
            speak('Parece que aun no has creado tus comandos, di configuración youTube y podras crear tu primer configuracion de youtube')

            return None

        speak('que accion quieres realizar')

        word = recognize_speech()

        for screen_list in data:

            if screen_list['screen'] == screen:

                for comand in screen_list['comands']:
                    if comand['comand'] in word:
                        youtube_app_dialog.click_input(
                            coords=(comand['x'], comand['y']))
                        print('accion realizada')
                        return None

                    else:
                        print('ocurrio un error')

    return None
