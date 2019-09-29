from estudiante import Estudiante
from laboratorio import Laboratorio
from fecha import Fecha


class AsistenciaLaboratorio:

    def __init__(self, fecha, laboratorio, codigo):
        self.__fecha = fecha
        self.__laboratorio = laboratorio
        self.__codigo = codigo
        self.__estudiantes = []

    def get_codigo(self):
        return self.__codigo
    
    def get_fecha(self):
        return self.__fecha

    def get_estudiante(self):
        return self.__estudiantes

    def get_laboratorios(self):
        return self.__laboratorio


    def buscar_estudiante(self, estudiante):
        for item_estudiante in self.__estudiantes:
            if item_estudiante.get_codigo() == estudiante.get_codigo():
                return True
        return -1

    def adicionar_estudiante(self, estudiante):
        if self.buscar_estudiante(estudiante) == -1:
            self.__estudiantes.append(estudiante)
            return True
        return False

    def visualizar_asistencia(self):
        print('Codigo: %s' %(self.__codigo))
        self.__fecha.visualizar_fecha()
        print('Laboratorio: %s' %(self.__laboratorio.nombre))

        for estudiante in self.__estudiantes:
            estudiante.visualizar_estudiante()

    
