from aritmetica import Operaciones

var1 = int(input('Ingrese el numero 1: '))
var2 = int(input('Ingrese el numero 2: '))

#Instanciar un objeto 

operacion = Operaciones(var1, var2)

print('La suma es: ', operacion.sumar(var1, var2))
print('La resta es: ', operacion.resta(var1, var2))
print('La multiplicacion es: ', operacion.multiplicacion(var1, var2))