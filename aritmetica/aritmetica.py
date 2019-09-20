class Operaciones():
    #constructor 
    def __init__(self, var1, var2):
        self.num1 = var1 #self__num1 => Es una variable privada
        self.num2 = var2 

    def sumar(self, var1, var2):
        resultado = var1 + var2
        return resultado

    def resta(self, var1, var2):
        resultado = var1 - var2
        return resultado

    def multiplicacion(self, var1, var2):
        resultado = var1 * var2
        return resultado