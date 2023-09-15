from collections import Counter

class Cancion:
    def __init__(self, nombre, genero, año, autores=[], cantantes=[], letra=[]):
        # Inicializo los atributos de la canción
        self.nombre = nombre
        self.genero = genero
        self.año = año
        self.autores = autores
        self.cantantes = cantantes
        self.letra = letra

        # Añado esta canción a la lista de canciones de cada autor y cantante involucrado
        for autor in autores:
            autor.añadir_cancion(self)
        for cantante in cantantes:
            cantante.añadir_cancion(self)

    def añadir_autor(self, autor):
        # Añado un autor a la lista de autores de la canción
        self.autores.append(autor)
        autor.añadir_cancion(self)

    def eliminar_autor(self, autor):
        # Elimino un autor de la lista de autores de la canción
        self.autores.remove(autor)
        autor.eliminar_cancion(self)

    def añadir_cantante(self, cantante):
        # Añado un cantante a la lista de cantantes de la canción
        self.cantantes.append(cantante)
        cantante.añadir_cancion(self)

    def eliminar_cantante(self, cantante):
        # Elimino un cantante de la lista de cantantes de la canción
        self.cantantes.remove(cantante)
        cantante.eliminar_cancion(self)

    def imprimir_letra(self):
        # Imprimo cada línea de la letra de la canción
        for linea in self.letra:
            print(linea)

    def histograma_palabras(self):
        # Creo un histograma con las 10 palabras más comunes en la letra de la canción
        palabras = " ".join(self.letra).split()
        conteo_palabras = Counter(palabras)
        return conteo_palabras.most_common(10)
