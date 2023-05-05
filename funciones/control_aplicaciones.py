import os
from funciones.abrir_paginas import open_website


def open_application(application_name, speak):

    # abrir programa
    if "chrome" in application_name:
        speak("Abriendo chrome")
        os.startfile("chrome.exe")

    elif "calculadora" in application_name:
        speak("Abriendo la calculadora")
        os.startfile("calc.exe")

    elif "notepad" in application_name:
        os.startfile("notepad.exe")
        speak("abriendo notepad")

    elif "visual" in application_name:
        speak('Abriendo visual')
        os.startfile(
            'C:\\Users\\USER\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe')
    # else:
    #     speak("Lo siento, no puedo abrir esa aplicación.")

    # abrir pagina
    elif "en prime" in application_name or "en youtube" in application_name or "youtube" in application_name or "facebook" in application_name or "en google" in application_name or "maps" in application_name or "chat" in application_name:
        open_website(application_name, speak)


def close_application(application_name, speak):
    if "chrome" in application_name:
        speak("Cerrando chrome")
        os.system("taskkill /f /im chrome.exe")

    elif "calculadora" in application_name:
        speak("Cerrando calcular")
        os.system("taskkill /f /im calc.exe")

    elif "notepad" in application_name:
        os.system("taskkill /f /im notepad.exe")
        speak("cerrando notepad")

    elif "visual" in application_name:
        os.system(
            "taskkill /f /im C:\\Users\\USER\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe")

    # elif "excel" in application_name:
    #     subprocess.Popen(["C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"])
    # else:
    #     speak("Lo siento, no puedo abrir esa aplicación.")
