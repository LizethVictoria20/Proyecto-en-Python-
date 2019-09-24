class PeliculaPrestada():
    def __init__(self, nombre):
        self.nombre = nombre
        self.peliculas = []

    def buscar_pelicula(self, codigo):
        for i in range(len(self.peliculas)):
            if self.peliculas[i].codigo == codigo:
                return i
        return -1

    def adicionar_pelicula(self, pelicula):
        if self.buscar_pelicula(pelicula.codigo) == -1:
            self.peliculas.append(pelicula)
            return True
        return False

    def listar_pelicula(self):
        for pelicula in self.peliculas:
            print('*******')
            pelicula.mostrar_pelicula()

    def eliminar_pelicula(self, codigo):
        pos = self.buscar_pelicula(codigo)

        if pos != -1:
            del(self.peliculas[pos])
            return True
        return False
