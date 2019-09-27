class Colegio:

    def __init__(self, nombre):
        self.__nombre = nombre
        self.__estudiantes = []
        self.__laboratorios = []
        self.__asistencias = []

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self, nombre):
        self.__nombre = nombre

    
    def buscar_estudiante(self, estudiante_codigo):
        for i in range(len(self.__estudiantes)):
            if self.__estudiantes[i].get_codigo == estudiante_codigo:
                return i
        return -1

    def agregar_estudiante(self, estudiante):
        if self.buscar_estudiante(estudiante.get_codigo()) == -1:
            self.__estudiantes.append(estudiante)
            return True
        return False


    #=============LABORATORIO=============#
    
    def buscar_laboratorio(self, codigo_laboratorio):
        for i in range(len(self.__laboratorios)):
            if self.__laboratorios[i].get_codigo == codigo_laboratorio:
                return i
        return -1
    
    def agregar_laboratorio(self, laboratorio):
        if self.buscar_laboratorio(laboratorio.get_codigo()) == -1:
            self.__laboratorios.append(laboratorio)
            return True
        return False

    

    


