class Pelicula():
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
       

    def mostrar_pelicula(self):
        print('Codigo: %s' %(self.codigo))
        print('Nombre: %s' %(self.nombre))