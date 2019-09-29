from os import system
from estudiante import Estudiante
from colegio import Colegio
from laboratorio import Laboratorio
from fecha import Fecha
from asistenciaLaboratorio import AsistenciaLaboratorio

from archivoColegio import ArchivoColegio



class Menu:

    def __init__(self, nombre_colegio, archivoColegioNombre):
        self.colegio = Colegio(nombre_colegio)
        self.archivoColegio = ArchivoColegio(archivoColegioNombre)

    #======== ESTUDIANTE ==========#

    def adicionar_estudiante(self):
        system('clear')
        print('Crear estudiante')

        nombre_estudiante = input('Ingrese el nombre del estudiante: ')
        apellido_estudiante = input('Ingrese el apellido del estudiante: ')
        codigo_estudiante = input('Ingrese el codigo del estudiante: ')

        estudiante = Estudiante(nombre_estudiante, apellido_estudiante, codigo_estudiante)

        if self.colegio.adicionar_estudiante(estudiante):

            print('El estudiante fue creado de forma exitosa')
            input()


    #======= LABORATORIO ========#

    def agregar_laboratorio(self):
        system('clear')
        print('Crear laboratorio')

        nombre_laboratorio = input('Ingrese el nombre del laboratorio: ')
        codigo_laboratorio = input('Ingrese el codigo del laboratorio: ')
        capacidad_laboratorio = input('Ingrese la capacidad del laboratorio: ')

        laboratorio = Laboratorio(nombre_laboratorio, codigo_laboratorio, capacidad_laboratorio)

        if self.colegio.agregar_laboratorio(laboratorio):
            print('El laboratorio fue creado de forma exitosa')
            input()

    #=========ASISTENCIA LABORATORIO============#
    def crear_asistencia_laboratorio(self):
        system('clear')
        print('Crear asistencia laboratorio')

        codigo_laboratorio = input('Ingrese el codigo del laboratorio: ')
        pos_laboratorio = self.colegio.buscar_laboratorio(codigo_laboratorio)

        if pos_laboratorio != -1:
            try:
                dia = int(input('Digite el dia: '))
                mes = int(input('Digite el mes: '))
                anio = int(input('Digite el anio: '))
                fecha = Fecha(anio, mes, dia)
                codigo_asistencia = int(input('Digite el codigo de la asistencia: '))
                asistencia_laboratorio = AsistenciaLaboratorio(fecha, self.colegio.get_laboratorio(pos_laboratorio), codigo_asistencia)

                while True:
                    print('Asistencia Estudiante')
                    print('1: Ingresar la asistencia del estudiante')
                    print('2: Salir')

                    op = input('Digite la opcion: ')
                    
                    if op == 1:
                        codigo_estudiante = input('Digite el codigo del estudiante')
                        pos_estudiante = self.colegio.buscar_estudiante(codigo_estudiante)

                        if pos_estudiante != -1:
                            asistencia_laboratorio.adicionar_estudiante(self.colegio.get_estudiante(pos_estudiante))
                        else: 
                            print('El estudiante no existe')
                    
                    elif op == 2:
                        break
                        
                    else:
                        print('Opcion no valida')
                        input()
                self.colegio.adicionar_asistencia(asistencia_laboratorio)

            except ValueError:
                print('Digite un numero entero')

        else:
            print('El laboratorio no existe')

    
    def listar_estudiantes(self):
        system('clear')
        print('Listar Estudiantes')

        for estudiante in self.colegio.get_estudiantes():
            print('Codigo: %s' %(estudiante.get_codigo()))
            print('Nombre: %s' %(estudiante.get_nombre()))
            print('Apellido: %s' %(estudiante.get_apellido()))
            print('**************')
        input()

    def listar_laboratorios(self):
        system('clear')
        print('Listar Laboratorios')

        for laboratorio in self.colegio.get_laboratorios():
            print('Nombre: %s' %(laboratorio.nombre))
            print('Codigo: %s' %(laboratorio.codigo))
            print('Capacidad: %s' %(laboratorio.capacidad))
            print('**************')
        input()
    
    def listar_asistencias(self):
        system('clear')
        print('Listar asistencias')
        for asistencia in self.colegio.get_asistencias():
            asistencia.visualizar_asistencia()
            print('**************')
        input()

    def listar_asistencia_laboratorio(self):
        system('clear')
        print('Listar asistencia por laboratorio')

        codigo_laboratorio = input('Digite el codigo del laboratorio: ')
        pos = self.colegio.buscar_laboratorio(codigo_laboratorio)

        if pos != -1:
            for asistencia in self.colegio.get_asistencia_laboratorio(codigo_laboratorio):
                asistencia.visualizar_asistencia()
                print('************+')
            input()

        else:
            print('EL laboratorio no existe')
            input()

    
    def listar_asistencia_laboratorio_estudiante(self):
        system('clear')
        print('Listar asistencia laboratorio del estudiante')

        codigo_estudiante = input('Digite el codigo del estudiante: ')
        pos = self.colegio.buscar_estudiante(codigo_estudiante)

        if pos != -1:
            for asistencia in self.colegio.get_asistencia_laboratorio_estudiante(codigo_estudiante):
                asistencia.visualizar_asistencia()
                print('************')
            input()

        else:
            print('El laboratorio no existe')
            input()

    
    

    #======== MENU ==========#


    def mostrar_menu(self):
        while True:
            print('***** Menu *****')
            print('1: Crear estudiante')
            print('2: Crear laboratorio')
            print('3: Registrar asistencia al laboratorio')
            print('4: Listar estudiantes')
            print('5: Listar laboratorios')
            print('6: Listar asistencias')
            print('7: Listar asistencia por laboratorio')
            print('8: Listar asistencia por laboratorio del estudiante')
            print('9: Salir')


            try:
                op = int(input('Digite la opcion: '))
                self.archivoColegio.guardar(self.colegio)

                if op == 1:
                    self.adicionar_estudiante()

                elif op == 2:
                    self.agregar_laboratorio()

                elif op == 3:
                    self.crear_asistencia_laboratorio()
                
                elif op == 4:
                    self.listar_estudiantes()

                elif op == 5:
                    self.listar_laboratorios()
                
                elif op == 6:
                    self.listar_asistencias()

                elif op == 7:
                    self.listar_asistencia_laboratorio()

                elif op == 8:
                    self.listar_asistencia_laboratorio_estudiante()
                
                elif op == 9:
                    break

                else:
                    print('Valor incorrecto')
                    input()
            
            except ValueError:
                print('Ingrese un numero entero')


if __name__ == '__main__':
    menu = Menu('TPS', 'colegio.data')
    data = menu.archivoColegio.cargar()

    if data is not  None:
        menu.colegio = menu.archivoColegio.cargar

    menu.mostrar_menu()