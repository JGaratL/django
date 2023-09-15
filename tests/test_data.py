from models.autor import Autor
from models.cantante import Cantante
from models.cancion import Cancion

# Crear instancias de autores y cantantes (esto es solo un ejemplo, debes obtener datos reales)
autor1 = Autor("Autor 1", 1980)
autor2 = Autor("Autor 2", 1990)

cantante1 = Cantante("Cantante 1", 1995)
cantante2 = Cantante("Cantante 2", 2000)

# Crear instancias de canciones con los autores y cantantes creados anteriormente
cancion1 = Cancion("Canción 1", "Pop", 2023, [autor1], [cantante1], ["linea 1", "linea 2"])
cancion2 = Cancion("Canción 2", "Rock", 2023, [autor2], [cantante2], ["linea 1", "linea 2"])

# Imprimir letra de una canción
cancion1.imprimir_letra()

# Obtener histograma de palabras más usadas en la letra de una canción
print(cancion1.histograma_palabras())

# Obtener el número de canciones por cada género para un autor
print(autor1.canciones_por_genero())

# Obtener el número de canciones por cada género para un cantante
print(cantante1.canciones_por_genero())
