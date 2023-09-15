from collections import Counter

class Cantante:
    def __init__(self, nombre, año_nacimiento):
        # Inicializo el nombre y el año de nacimiento del cantante
        self.nombre = nombre
        self.año_nacimiento = año_nacimiento
        self.canciones = []

    def añadir_cancion(self, cancion):
        # Añado una canción a la lista de canciones del cantante
        self.canciones.append(cancion)

    def eliminar_cancion(self, cancion):
        # Elimino una canción de la lista de canciones del cantante
        self.canciones.remove(cancion)

    def canciones_por_genero(self):
        # Creo una lista de los géneros de todas las canciones del cantante
        generos = [cancion.genero for cancion in self.canciones]
        # Devuelvo un contador con la cantidad de canciones por género
        return Counter(generos)
