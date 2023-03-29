print("Primera prueba de canciones en python")
class Cancion:
    lista_canciones = []
    
    def __init__(self, nombre, compositor, cantante, album, ano):
        self.nombre = nombre
        self.compositor = compositor
        self.cantante = cantante
        self.album = album
        self.ano = ano
        
    def agregar_cancion(self):
        Cancion.lista_canciones.append(self)
        
    def eliminar_cancion(self):
        Cancion.lista_canciones.remove(self)
        
    def modificar_cancion(self, nombre=None, compositor=None, cantante=None, album=None, ano=None):
        if nombre is not None:
            self.nombre = nombre
        if compositor is not None:
            self.compositor = compositor
        if cantante is not None:
            self.cantante = cantante
        if album is not None:
            self.album = album
        if ano is not None:
            self.ano = ano