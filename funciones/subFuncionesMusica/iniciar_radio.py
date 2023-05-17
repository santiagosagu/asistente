import time as time_module


def iniciar_radio(x, y, screen, pantalla_principal, width_ventana_in_pantalla_principal, segunda_pantalla, width_ventana_segunda_pantalla, youtube_music_app_dialog):
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

    time_module.sleep(2)

    if screen == pantalla_principal:
        x = 1596
        y = 776
    elif screen == width_ventana_in_pantalla_principal:
        x = 863
        y = 402
    elif screen == segunda_pantalla:
        x = 1236
        y = 363
    elif screen == width_ventana_segunda_pantalla:
        x = 898
        y = 360

    youtube_music_app_dialog.click_input(coords=(x, y))
