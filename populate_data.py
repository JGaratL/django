import requests
from bs4 import BeautifulSoup
from collections import Counter

from models.autor import Autor
from models.cancion import Cancion
from models.cantante import Cantante

def obtener_letra(url):
    # Realizo una solicitud para obtener el contenido de la página
    response = requests.get(url)
    # Parseo el contenido de la página con BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    # Busco el div que contiene la letra de la canción
    letra_div = soup.find('div', {'style': 'padding: 10px; ', 'class': 'translate'})
    if letra_div:
        # Obtengo el texto bruto de la letra y lo separo en líneas
        letra_bruto = letra_div.decode_contents()
        letra = letra_bruto.replace('<br/>', '\n').split('\n')
        letra = [linea.strip() for linea in letra if linea.strip()]
        return letra
    else:
        # Si no se encuentra el div, retorno una lista vacía
        return []

def populate_data():
    url = "https://top40-charts.com/chart.php?cid=21&date=2023-09-03"
    
    # Realizo una solicitud para obtener el contenido de la página
    response = requests.get(url)
    # Parseo el contenido de la página con BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encuentro todos los elementos que contienen información de las canciones
    canciones_elements = soup.find_all('tr', class_='latc_song')

    # Creo un diccionario para mantener un registro de los cantantes únicos
    cantantes_unicos = {}

    for cancion_element in canciones_elements:
        # Extraigo el nombre de la canción y del cantante del elemento actual
        nombre_cancion_element = cancion_element.find('a', {'style': 'padding-bottom: 1px; text-decoration: none; border-bottom: 2px solid #F17D38; font-size: 11pt;'})
        nombre_cantante_element = cancion_element.find('a', style='text-decoration: none; ')

        # Establezco valores predeterminados en caso de que no se encuentren algunos detalles
        nombre_cancion = nombre_cancion_element.text.strip() if nombre_cancion_element else "Desconocido"
        nombre_cantante = nombre_cantante_element.text.strip() if nombre_cantante_element else "Desconocido"

        # Defino valores predeterminados para el género y el año de la canción
        genero = "Desconocido"
        año = 2023
        autores = []

        # Compruebo si el cantante ya está registrado, de lo contrario, creo una nueva instancia
        if nombre_cantante not in cantantes_unicos:
            cantante = Cantante(nombre=nombre_cantante, año_nacimiento=2000)  # Año de nacimiento ficticio
            cantantes_unicos[nombre_cantante] = cantante
        else:
            cantante = cantantes_unicos[nombre_cantante]

        # Creo una nueva instancia de la clase Canción
        cancion = Cancion(nombre=nombre_cancion, genero=genero, año=año, autores=autores, cantantes=[cantante])

        # Construyo la URL para obtener la letra de la canción
        url_letra = f"https://top40-charts.com/songs/lyrics.php{nombre_cancion_element['href'].replace('song.php', '')}"

        # Obtengo y asigno la letra de la canción
        letra = obtener_letra(url_letra)
        cancion.letra = letra

        # Añado la canción a la lista de canciones del cantante
        cantante.añadir_cancion(cancion)

    return cantantes_unicos

if __name__ == "__main__":
    cantantes = populate_data()

    for cantante in cantantes.values():
        canciones_impresas = set()
        
        for cancion in cantante.canciones:
            if cancion.nombre not in canciones_impresas:
                print(f"Cantante: {cantante.nombre}")
                print(f"Canción: {cancion.nombre}")
                print("Letra:")
                for linea in cancion.letra:
                    print(linea)
                print("\n")
                
                canciones_impresas.add(cancion.nombre)

        # Calculo las 10 palabras más usadas por el cantante
        palabras_mas_usadas = Counter()
        for cancion in cantante.canciones:
            palabras_mas_usadas.update(cancion.histograma_palabras())
        
        # Imprimo las 10 palabras más usadas por el cantante
        print("Las 10 palabras más usadas en las canciones de este cantante:")
        for palabra, frecuencia in palabras_mas_usadas.most_common(10):
            print(f"{palabra}: {frecuencia}")
        print("\n")
