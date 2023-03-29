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
        def mostrar_cancion(self):
        print('Nombre:', self.nombre)
        print('Compositor:', self.compositor)
        print('Cantante:', self.cantante)
        print('Álbum:', self.album)
        print('Año:', self.ano)
      
    def buscar_cancion(self, nombre_buscar):
        
        if self.nombre == nombre_buscar:
            print(f"La canción '{nombre_buscar}' existe:")
            self.mostrar_cancion()
        else:
            print(f"La canción '{nombre_buscar}' no existe.")
            
        
c1 = Cancion("Bohemian","Freddy","Queen","A night of Opera",1977)
c2 = Cancion("Mil horas","Andres Calamar","Los abuelos de la nada","Mil horas",1990)
c3 = Cancion("Smeel like teen Spirit","Kurt Cobain","Nirvana","Nevermind",1991)
c4 = Cancion("Du hast","Rammstein","Rammstein","Sehnsucht",1997)

c1.agregar_cancion()
c2.agregar_cancion()
c3.agregar_cancion()
c4.agregar_cancion()

c2.buscar_cancion("Bohemian")

c1.modificar_cancion("Bohemian REMIX","Freddy","Queen","A night of Opera",1977)
c1.mostrar_cancion()
c4.eliminar_cancion()