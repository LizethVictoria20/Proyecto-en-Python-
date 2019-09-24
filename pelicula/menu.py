from os import system
from pelicula import Pelicula
from peliculaPrestada import PeliculaPrestada

class Menu:
    def __init__(self, peliculaPrestada):
        self.peliculaPrestada = peliculaPrestada

    def adicionar_pelicula(self):
        print('Agregar Pelicula')
        codigo = input('Digite el codigo de la pelicula: ')
        nombre = input('Digite el nombre de la pelicula: ')
        
        pelicula = Pelicula(codigo, nombre)
        
        if self.peliculaPrestada.adicionar_pelicula(pelicula):
            print('Registro exitoso')
            input()
        
        else:
            print('Registro fail')

    def listar_pelicula(self):
        system("clear")
        print('*********')
        print('Listar peliculas')

        self.peliculaPrestada.listar_pelicula()
        input()

    def eliminar_pelicula(self):
        system("clear")
        print('*******')
        print('Eliminar pelicula')

        codigo = input('Digite el numero de la pelicula: ')
        if self.peliculaPrestada.eliminar_pelicula(codigo):
            print('La pelicula fue eliminada')
        else:
            print('La pelicula no fue eliminada')


    def menu_principal(self):
        
        while True:
            system("clear") 
            print('********')
            print('Menu Principal')
            print('1: Crear Pelicula')
            print('2: Listar Peliculas')
            print('3: Eliminar Pelicula')
            print('4: Salir')

            try:
                op = int(input('Digite la opcion: '))

                if op == 1:
                    self.adicionar_pelicula()
                
                elif op == 2:
                    self.listar_pelicula()

                elif op == 3:
                    self.eliminar_pelicula()

                elif op == 4:
                    break

                else:
                    print('Digite una opcion valida')
                    input()
            
            except ValueError:
                print('Digite un numero entero')
                input()

if __name__ == '__main__':
    peliculaPrestada = PeliculaPrestada('...')
    menu = Menu(peliculaPrestada)
    menu.menu_principal()
                    