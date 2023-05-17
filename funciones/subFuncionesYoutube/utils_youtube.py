import time as time_module
from firebaseClient import enpoints_youtube
from funciones.utils import speak
from funciones.utils import get_window_position_relative


def nuevo_comando_youtube(recognize_speech, left, top, screen):

    speak('ok, necesitare obtener varias cosas, una es el nombre que le pondras al comando, luego el comando que diras, y por ultimo la posicion del maus dentro de ventana de youTube, por lo cual cuando te diga obtendre la posicion del maus, te esperare 2 segundos para que logres poner el maus, por favor ten claro el nombre y el comando')

    speak('empecemos...')

    speak('dime el nombre del nuevo comando')

    nuevo_comando = {}

    nombre_comando = recognize_speech()

    nuevo_comando['word'] = nombre_comando

    speak('ahora dime frase quieres decir para ejecutar este comando, ejemplo pausar video')

    nombre_comando = recognize_speech()

    nuevo_comando['comand'] = nombre_comando

    speak('vale, ahora obtendre la posición del mous te voy a esperar 2 segundos para que pongas el maus encima de donde quieres que de click, hazlo ahora')

    time_module.sleep(2)

    position = get_window_position_relative(left, top)

    nuevo_comando['x'] = position[0]
    nuevo_comando['y'] = position[1]

    print('tu comando es:', nuevo_comando)

    speak('quieres guardar este comando? response si o no')

    confirmacion = recognize_speech()

    if 'sí' in confirmacion:
        enpoints_youtube.agregar_nuevo_comando(screen, nuevo_comando)
    else:
        speak('se ha cancelado el nuevo comando')
        return None


def agregar_nueva_resolucion_youtube(screen, left, top, recognize_speech):

    speak('vale, lo primero que necesitamos es que ajustes la ventana de youtube a la posicion que desees registrar en los comandos')

    speak('te dare 5 segundos para que la ajustes, apartir de ya...')

    time_module.sleep(5)

    speak('ok, luego necesitamos agregar 1 comando, necesito que pienses un nombre y un comando que agregaras ejemplo pausar youtube, despues de esto tendras que poner el maus encima de donde quieres que de click, te dare 3 segundos para que pienses la palabra y como quieres que funcione el comando.')

    time_module.sleep(3)

    speak('vale estamos listos, para agregar el comando')

    speak('dime el nombre del nuevo comando')

    nuevo_comando = {}

    nombre_comando = recognize_speech()

    nuevo_comando['word'] = nombre_comando

    speak('ahora dime frase quieres decir para ejecutar este comando, ejemplo pausar video')

    nombre_comando = recognize_speech()

    nuevo_comando['comand'] = nombre_comando

    speak('vale, ahora obtendre la posición del mous te voy a esperar 2 segundos para que pongas el maus encima de donde quieres que de click, hazlo ahora')

    time_module.sleep(2)

    position = get_window_position_relative(left, top)

    nuevo_comando['x'] = position[0]
    nuevo_comando['y'] = position[1]

    print('tu comando es:', nuevo_comando)

    nuevo_screen = {'screen': screen, 'comands': [nuevo_comando]}

    enpoints_youtube.crear_registro(nuevo_screen)
