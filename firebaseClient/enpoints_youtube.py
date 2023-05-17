from firebase import firebase
import json

firebaseUrl = firebase.FirebaseApplication(
    "https://asis-a34ad-default-rtdb.firebaseio.com/", None)

with open('config.json', 'r') as f:
    data = json.load(f)


# user = None

# if data['user']['name']:
    user = data['user']['name']


def crear_registro(comands):

    # if user is not None:

    firebaseUrl.post(f'/{user}/comands_youtube', comands)


def traer_registros():
    # Leer un registro de la base de datos
    # if user is not None:
    result = firebaseUrl.get(f'/{user}/comands_youtube', None)

    if result is None:
        return None
    else:

        return result.values()


def agregar_nuevo_comando(screen, nuevo_comando):
    # Obtener el registro con la pantalla especificada
    # if user is not None:
    registros = firebaseUrl.get(f'/{user}/comands_youtube', None)

    registro = None
    for key, value in registros.items():
        if value['screen'] == screen:
            registro = value
            print('key', key)
            break

    if registro is None:
        # Si no se encontró el registro, imprimir un mensaje de error y salir de la función
        print(f"No se encontró ningún registro con la pantalla {screen}")
        return

    # Agregar el nuevo comando al registro existente
    registro['comands'].append(nuevo_comando)

    print("Registros", registro)

    # Actualizar el registro en la base de datos
    firebaseUrl.put(f'/{user}/comands_youtube', key, registro)
