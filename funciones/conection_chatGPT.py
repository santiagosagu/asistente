from dotenv import load_dotenv
import openai
import os


load_dotenv()

# key openIA
openai.api_key = os.getenv('OPENIA')

# Configuramos el modelo en español
model_engine = "text-davinci-003"


def search_with_openIA(recognize_speech, speak):
    speak("¿Sobre qué tema quieres que investigue?")

    while True:

        topic = recognize_speech(3)  # Obtener el tema de investigacion

        if topic == "salir":
            speak('claro señor, dejare de consultar')
            break

        if topic == "déjame escribirte":
            speak('ok señor, se ha habilitado la entrada de texto')
            texto = input()

            completado = openai.Completion.create(
                engine=model_engine, prompt=texto, max_tokens=2048, n=1,
                stop=None,
                logprobs=10
                # timeout=None,
                # presence_penalty=None,
                # frequency_penalty=None,
                # best_of=None,
            )

            respuesta = completado.choices[0].text

            speak(respuesta)
            print(respuesta)

            break

        else:

            completado = openai.Completion.create(
                engine=model_engine, prompt=topic, max_tokens=2048, n=1,
                stop=None,
                logprobs=10
                # timeout=None,
                # presence_penalty=None,
                # frequency_penalty=None,
                # best_of=None,
            )

            respuesta = completado.choices[0].text
            speak(respuesta)
            print(respuesta)

            break
