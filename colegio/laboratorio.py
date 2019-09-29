class Laboratorio:
    def __init__(self, nombre, codigo, capacidad):
        self.nombre = nombre
        self.codigo = codigo
        self.capacidad = capacidad 

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self, nombre):
        return self.nombre 

    def set_codigo(self, codigo):
        self.codigo = codigo

    def get_codigo(self):
        return self.codigo

    def set_capacidad(self, capacidad):
        self.capacidad = capacidad
    
    def get_capacidad(self, capacidad):
        return self.capacidad 



#Laboratorio = Nombre, codigo y capacidad