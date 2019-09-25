class Pelicula():
    def __init__(self, codigo, nombre, genero):
        self.codigo = codigo
        self.nombre = nombre
        self.genero = genero

        self.alquilada = None
       

    def mostrar_pelicula(self):
        print('Codigo: %s' %(self.codigo))
        print('Nombre: %s' %(self.nombre))
        print('Genero: %s' %(self.genero))
        if self.alquilada == None:
            print('Estado: Disponible')
        else:
            print('Estado: Alquilada')