import time as time_module


def reproduccion_aleatoria_me_gusta(x, y, screen, pantalla_principal, width_ventana_in_pantalla_principal, segunda_pantalla, width_ventana_segunda_pantalla, youtube_music_app_dialog):
    if screen == pantalla_principal:
        x = 1328
        y = 73

    elif screen == width_ventana_in_pantalla_principal:
        x = 671
        y = 62

    elif screen == segunda_pantalla:
        x = 1011
        y = 67
    elif screen == width_ventana_segunda_pantalla:
        x = 672
        y = 64

    # dar click en biblioteca
    youtube_music_app_dialog.click_input(coords=(x, y))

    time_module.sleep(2)

    if screen == pantalla_principal:
        x = 538
        y = 282

    elif screen == width_ventana_in_pantalla_principal:
        x = 179
        y = 280

    elif screen == segunda_pantalla:
        x = 217
        y = 286

    elif screen == width_ventana_segunda_pantalla:
        x = 180
        y = 282

    # dar click en Contenido que te gusta
    youtube_music_app_dialog.click_input(coords=(x, y))

    time_module.sleep(2)

    if screen == pantalla_principal:
        x = 911
        y = 388

    elif screen == width_ventana_in_pantalla_principal:
        x = 449
        y = 343

    elif screen == segunda_pantalla:
        x = 599
        y = 389

    elif screen == width_ventana_segunda_pantalla:
        x = 450
        y = 345

    # dar click en aleatorio
    youtube_music_app_dialog.click_input(coords=(x, y))
