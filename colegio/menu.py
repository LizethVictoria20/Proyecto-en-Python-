from os import system
from estudiante import Estudiante
from colegio import Colegio
from laboratorio import Laboratorio


class Menu:

    def __init__(self, nombre_colegio):
        self.colegio = Colegio(nombre_colegio)


    def crear_estudiante(self):
        system('clear')
        print('Crear estudiante')

        nombre_estudiante = input('Ingrese el nombre del estudiante: ')
        apellido_estudiante = input('Ingrese el apellido del estudiante: ')
        codigo_estudiante = input('Ingrese el codigo del estudiante: ')

        estudiante = Estudiante(nombre_estudiante, apellido_estudiante, codigo_estudiante)

        self.colegio.agregar_estudiante(estudiante)
        print('El estudiante fue creado de forma exitosa')


    #======= LABORATORIO ========#

    def crear_laboratorio(self):
        system('clear')
        print('Crear laboratorio')

        nombre_laboratorio = input('Ingrese el nombre del laboratorio: ')
        codigo_laboratorio = input('Ingrese el codigo del laboratorio: ')
        capacidad_laboratorio = input('Ingrese la capacidad del laboratorio: ')

        laboratorio = Laboratorio(nombre_laboratorio, codigo_laboratorio, capacidad_laboratorio)

        self.colegio.agregar_laboratorio(laboratorio)
        print('El laboratorio fue creado de forma exitosa')
    

    #======== MENU ==========#


    def mostrar_menu(self):
        while True:
            print('***** Menu *****')
            print('1: Crear estudiante')
            print('2: Crear laboratorio')
            print('3: Salir')


            try:
                op = int(input('Digite la opcion: '))

                if op == 1:
                    self.crear_estudiante()

                elif op == 2:
                    self.crear_laboratorio()
                
                elif op == 3:
                    break

                else:
                    print('Valor incorrecto')
                    input()
            
            except ValueError:
                print('Ingrese un numero entero')


if __name__ == '__main__':
    colegio = Colegio('Tecnico PS')
    menu = Menu(colegio)
    menu.mostrar_menu()