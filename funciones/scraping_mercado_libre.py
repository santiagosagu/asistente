from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time as time_module
import pprint
from funciones.utils import speak, volumen_down
import json


def scraping_mercado_libre(product, recognize_speech):
    # Configurar el driver de Selenium
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    # driver = Chrome()

    # Definir el producto a buscar
    producto = None

    if product is None:
        speak('No pude entender el producto que quieres buscar, me lo repites por favor')
        volumen_down(True)
        producto = recognize_speech()
    else:
        producto = product

    volumen_down(False)

    # Navegar a la página de búsqueda de Mercado Libre
    driver.get(f"https://listado.mercadolibre.com.co/{producto}")

    # Crear una lista vacía para almacenar los resultados
    resultados = set()

    numero_paginas = driver.find_element(
        By.CLASS_NAME, 'andes-pagination__page-count')

    total_paginas = int(numero_paginas.text.split('de ')[1])

    boton_cookies = driver.find_element(
        By.CLASS_NAME, 'cookie-consent-banner-opt-out__action--key-accept')

    boton_cookies.click()

    for pagina_actual in range(1, total_paginas + 1):

        try:
            time_module.sleep(2)

            # Obtenemos el botón siguiente y hacemos clic en él
            # boton = driver.find_element(
            #     By.CLASS_NAME, 'andes-pagination__button--next')

            # boton_siguiente = boton.get_attribute('title')

            print(pagina_actual, total_paginas)

            items = driver.find_elements(
                By.CLASS_NAME, 'ui-search-layout__item')

            print('aqui entre')

            for item in items:

                result_link = item.find_element(By.CLASS_NAME, 'ui-search-result__wrapper').find_element(By.CLASS_NAME, 'andes-card').find_element(
                    By.CLASS_NAME, 'shops__result-content-wrapper').find_element(By.CLASS_NAME, 'ui-search-item__group').find_element(By.CLASS_NAME, 'ui-search-link')

                name = result_link.get_attribute('title')
                link = result_link.get_attribute('href')

                result_price = item.find_element(By.CLASS_NAME, 'ui-search-result__wrapper').find_element(By.CLASS_NAME, 'andes-card').find_element(
                    By.CLASS_NAME, 'shops__result-content-wrapper').find_element(By.CLASS_NAME, 'ui-search-result__content-columns').find_element(By.CLASS_NAME, 'shops__content-columns-left').find_element(By.CLASS_NAME, 'ui-search-item__group__element').find_element(By.CLASS_NAME, 'ui-search-price').find_element(By.CLASS_NAME, 'ui-search-price__second-line').find_element(By.CLASS_NAME, 'shops__price-part').find_element(By.CLASS_NAME, 'price-tag-text-sr-only')

                price = float(result_price.text.replace('pesos', ''))

                resultados.add(json.dumps(
                    {'enlace': link, 'precio': price, 'nombre': name}))

            if pagina_actual < total_paginas:
                time_module.sleep(3)

                boton = driver.find_element(
                    By.CLASS_NAME, 'andes-pagination__button--next')

                if boton:
                    boton.click()
                else:

                    print(
                        f'El botón siguiente no está presente en la página {pagina_actual}')
                    continue

                # time_module.sleep(2)

                # boton.click()

        except NoSuchElementException:
            # Si no se encuentra el botón siguiente, salimos del loop
            # print(
            #     f'Finalizamos en la página {pagina_actual} porque no se encontró el botón siguiente')

            # speak(
            #     'listo he terminado, estos son los 10 productos mas baratos de tu busqueda')
            continue

    resultados_ordenados = sorted(
        resultados, key=lambda x: json.loads(x)["precio"])

    contador = 0
    for resultado in resultados_ordenados:
        producto = json.loads(resultado)
        pprint.pprint(
            f"Precio: ${producto['precio']:.2f} - Enlace: {producto['enlace']} - Nombre: {producto['nombre']}")
        contador += 1
        if contador == 20:
            break

    resultados.clear()  # Vaciar el conjunto de resultados
