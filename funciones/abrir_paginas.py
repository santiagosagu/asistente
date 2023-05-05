import webbrowser


def open_website(website_name, speak):
    if "google" in website_name:
        webbrowser.open("https://www.google.com")

    elif "en prime" in website_name:
        speak("Realizando búsqueda")
        webbrowser.open("https://www.primevideo.com/search/ref=atv_nb_sug?ie=UTF8&phrase=" +
                        website_name.split('en prime')[1])

    elif "en youtube" in website_name:
        # webbrowser.open("https://www.youtube.com")
        speak("Realizando búsqueda")
        webbrowser.open("https://www.youtube.com/results?search_query=" +
                        website_name.split("en youtube ")[1])

    elif "youtube" in website_name:
        webbrowser.open("https://www.youtube.com")

    elif "facebook" in website_name:
        webbrowser.open("https://www.facebook.com")

    elif "twitter" in website_name:
        webbrowser.open("https://www.twitter.com")

    elif "en google" in website_name:
        webbrowser.open("https://www.google.com/search?q=" +
                        website_name.replace("buscar en google ", ""))

    elif "maps" in website_name:
        webbrowser.open("https://www.google.com/maps")

    elif "whatsapp" in website_name:
        webbrowser.open("https://web.whatsapp.com/")

    elif "chat" in website_name:
        webbrowser.open("https://chat.openai.com/")
    # else:
    #     speak("Lo siento, no puedo abrir ese sitio web.")
