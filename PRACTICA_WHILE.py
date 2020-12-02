'''edad =int(input("Ingrese la edad: "))

while edad<=5 or edad>100:
    print("Ha ingresado una edad incorrecta, intente nuevamente")
    edad =int(input("Ingrese la edad: "))
print("Gracias.")
print(f"Edad del aspirante: {edad}")'''

import math

print("programa para calcular la raiz cuadrada")
numero = int(input("Ingrese el numero: "))

intentos=0

while numero<0:
    print("¡No se puede hallar la raiz de un numero negativo!")
    
    if intentos==2:
        print("Has intentado demasiadas veces")
        break;
    numero = int(input("Ingrese el numero: "))
    if numero<0:
        intentos=intentos+1
if intentos<2:
    solucion=math.sqrt(numero)
    print(f"La raiz cuadrada de {numero} es {solucion}")