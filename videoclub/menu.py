from os import system
from socio import Socio
from videoclub import Videoclub
from pelicula import Pelicula

class Menu:
    def __init__(self, videoclub):
        self.videoclub = videoclub

    def adicionar_socio(self):
        print('Adicionar Socio')
        codigo = input('Digite el codigo del socio: ')
        nombre = input('Digite el nombre del socio: ')
        telefono = input('Digite el telefono del socio: ')
        domicilio = input('Digite el domicilio del socio: ')

        socio = Socio(codigo, nombre, telefono, domicilio)
        
        if self.videoclub.adicionar_socio(socio):
            print('Registro exitoso')
            input()
        
        else:
            print('Registro fail')

    def listar_socio(self):
        system("clear")
        print('*********')
        print('Listar socios')

        self.videoclub.listar_socio()
        input()

    def eliminar_socio(self):
        system("clear")
        print('*******')
        print('Eliminar Socios')

        codigo = input('Digite el numero del socio: ')
        if self.videoclub.eliminar_socio(codigo):
            print('El socio fue eliminado')
        else:
            print('El socio no fue eliminado')

    #============PELICULA===============#

    def adicionar_pelicula(self):
        print('Agregar Pelicula')
        codigo = input('Digite el codigo de la pelicula: ')
        nombre = input('Digite el nombre de la pelicula: ')
        genero = input('Digite el genero de la pelicula: ')
        
        pelicula = Pelicula(codigo, nombre, genero)
        
        if self.videoclub.adicionar_pelicula(pelicula):
            print('Registro exitoso')
            input()
        
        else:
            print('Registro fail')
            input()

    def listar_pelicula(self):
        system("clear")
        print('*********')
        print('Listar peliculas')

        self.videoclub.listar_pelicula()
        input()

    def eliminar_pelicula(self):
        system("clear")
        print('*******')
        print('Eliminar pelicula')

        codigo = input('Digite el numero de la pelicula: ')
        if self.videoclub.eliminar_pelicula(codigo):
            print('La pelicula fue eliminada')
            input()
        else:
            print('La pelicula no fue eliminada')
            input()

    def alquilar_pelicula(self):
        codigo_pelicula = input('Ingrese el codigo de la pelicula: ')
        codigo_socio = input('Ingrese el codigo de la socio: ')

        if self.videoclub.alquilar_pelicula(codigo_pelicula, codigo_socio):
            print('Alquilada corretamente')
            input()
        else:
            print('La pelicula no se puede alquilar')
            input()

    def devolver_pelicula(self):
        codigo_pelicula = input('Ingrese el codigo de la pelicula: ')
        codigo_socio = input('Ingrese el codigo de la socio: ')

        if self.videoclub.devolver_pelicula(codigo_pelicula, codigo_socio):
            print('La pelicula se devolvio corretamente')
            input()
        else:
            print('La pelicula no se puede devolver')
            input()



    #=============MENU===============#

    def mostrar_menu_principal(self):
        
        while True:
            system("clear") 
            print('********')
            print('Menu Principal')
            print('1: Crear Socio')
            print('2: Listar Socios')
            print('3: Eliminar socio')
            print('4: Crear Pelicula')
            print('5: Listar Peliculas')
            print('6: Eliminar Pelicula')
            print('7: Prestar Pelicula')
            print('8: Devolver Pelicula')
            print('9: Salir')

            try:
                op = int(input('Digite la opcion: '))

                if op == 1:
                    self.adicionar_socio()
                
                elif op == 2:
                    self.listar_socio()

                elif op == 3:
                    self.eliminar_socio()
                
                elif op == 4:
                    self.adicionar_pelicula()
                
                elif op == 5:
                    self.listar_pelicula()

                elif op == 6:
                    self.eliminar_pelicula()
                
                elif op == 7:
                    self.alquilar_pelicula()

                elif op == 8:
                    self.devolver_pelicula()

                elif op == 9:
                    break

                else:
                    print('Digite una opcion valida')
                    input()
            
            except ValueError:
                print('Digite un numero entero')
                input()

if __name__ == '__main__':
    videoclub = Videoclub('Silencio')
    menu = Menu(videoclub)
    menu.mostrar_menu_principal()
                    