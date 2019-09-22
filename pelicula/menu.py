from pelicula import Pelicula
from peliculaPrestada import PeliculaPrestada


class Menu():
    def __init__(self, PeliculaPrestada):
        self.peliculaPrestada = PeliculaPrestada


    def adicionar_pelicula(self):
        print('Agrega una pelicula')
        codigo = input('Agrega el codigo de la pelicula: ')
        nombre = input('Agrega el nombre de la pelicula: ')

        pelicula = Pelicula(codigo, nombre)

        if self.peliculaPrestada.adicionar_pelicula(pelicula):
            print('Registro exitoso')
        else:
            print('Registro fail')

    
    def listar_peliculas(self):
        print('Listar Socios')
        self.peliculaPrestada.listar_peliculas()
        input()
    
    
    def eliminar_pelicula(self):
        print('Eliminar Pelicula')
        codigo = print('Digite el codigo de la pelicula')

        if self.peliculaPrestada.eliminar_pelicula(codigo):
            print('La pelicula fue eliminada exitosamente')
        else:
            print('La pelicula no pudo ser eliminada')

    
    def menu_principal(self):
        while True:
            print('Menu Principal')
            print('1: Agregar pelicula')
            print('2: Listar pelicula')
            print('3: Eliminar pelicula')
            print('4: Salir')

            try:
                opcion = print('Digite la opcion: ')

                if opcion == 1:
                    self.adicionar_pelicula()

                elif opcion == 2:
                    self.listar_peliculas()

                elif opcion == 3:
                    self.eliminar_pelicula()
                
                elif opcion == 4:
                    break

            except ValueError:
                print('Digite un numero entero')


if __name__ == '__main__':
    peliculaPrestada = PeliculaPrestada('...')
    menu = Menu(peliculaPrestada)
    menu.menu_principal()




