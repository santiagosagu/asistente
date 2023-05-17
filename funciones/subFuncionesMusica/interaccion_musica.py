

def pausar_reproducir_cancion(x, y, screen, pantalla_principal, width_ventana_in_pantalla_principal, segunda_pantalla, width_ventana_segunda_pantalla, youtube_music_app_dialog):
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


def siguiente_canción(x, y, screen, pantalla_principal, width_ventana_in_pantalla_principal, segunda_pantalla, width_ventana_segunda_pantalla, youtube_music_app_dialog):
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


def anterior_canción(x, y, screen, pantalla_principal, width_ventana_in_pantalla_principal, segunda_pantalla, width_ventana_segunda_pantalla, youtube_music_app_dialog):
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

    youtube_music_app_dialog.double_click_input(coords=(x, y))


def repetir_canción(x, y, screen, pantalla_principal, width_ventana_in_pantalla_principal, segunda_pantalla, width_ventana_segunda_pantalla, youtube_music_app_dialog):
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


def dar_me_gusta(x, y, screen, pantalla_principal, width_ventana_in_pantalla_principal, segunda_pantalla, width_ventana_segunda_pantalla, youtube_music_app_dialog):
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
