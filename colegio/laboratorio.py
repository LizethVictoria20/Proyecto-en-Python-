class Laboratorio:
    def __init__(self, nombre, codigo, capacidad):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__capacidad = capacidad 

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self, nombre):
        return self.__nombre 

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_codigo(self):
        return self.__codigo

    def set_capacidad(self, capacidad):
        self.__capacidad = capacidad
    
    def get_capacidad(self, capacidad):
        return self.__capacidad 



#Laboratorio = Nombre, codigo y capacidad