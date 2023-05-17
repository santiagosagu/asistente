from firebase import firebase
import json

firebaseUrl = firebase.FirebaseApplication(
    "https://asis-a34ad-default-rtdb.firebaseio.com/", None)

with open('config.json', 'r') as f:
    data = json.load(f)

user = None

if data['user']['name']:
    user = data['user']['name']


def crear_registro_recordatorio(recordatorio):

    if user is not None:

        firebaseUrl.post(f'/{user}/recordatorios', recordatorio)


def traer_registros_recordatorio():
    # Leer un registro de la base de datos

    if user is not None:
        result = firebaseUrl.get(f'/{user}/recordatorios', None)

        if result is not None:
            return result.items()


def eliminar_registro_recordatorio(key):
    # Eliminar un registro de la base de datos

    if user is not None:

        result = firebaseUrl.delete(f'/{user}/recordatorios', key)

        print(result)
