print("Calculadora con una sola variable\n")

print("********************")
print("* Menu de opciones *")
print("********************")

print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. División entera")
print("6. Exponente")
print("7. Modulo o resto\n")

option =int(input("Elige la opción de acuerdo a la operación que deseas realizar: "))

if option == 1:
    print("Elegiste la operación suma\n")
    numero = int(input("Ingresa el primer número: "))
    numero += int(input("Ingresa el segundo número: "))
    print("El resultado de la suma es: ", numero)
elif option == 2:
    print("Elegiste la operación resta\n")
    numero = int(input("Ingresa el primer número: "))
    numero -= int(input("Ingresa el segundo número: "))
    print("El resultado de la resta es: ", numero)
elif option == 3:
    print("Elegiste la operación multiplicación\n")
    numero = int(input("Ingresa el primer número: "))
    numero *= int(input("Ingresa el segundo número: "))
    print("El resultado de la multiplicación es: ", numero)
elif option == 4:
    print("Elegiste la operación división\n")
    numero = int(input("Ingresa el primer número: "))
    numero /= int(input("Ingresa el segundo número: "))
    print("El resultado de la división es: ", numero)
elif option == 5:
    print("Elegiste la operación división entera\n")
    numero = int(input("Ingresa el primer número: "))
    numero //= int(input("Ingresa el segundo número: "))
    print("El resultado de la división entera es: ", numero)
elif option == 6:
    print("Elegiste la operación potencia\n")
    numero = int(input("Ingresa el número: "))
    numero **= int(input("Ingresa ingresa el exponente al que deseas elevarlo: "))
    print("El resultado de la potencia es: ", numero)
elif option == 7:
    print("Elegiste la operación modulo o resto\n")
    numero = int(input("Ingresa el número: "))
    numero %= int(input("Ingresa el segundo número: "))
    print("El resultado del modulo o resto es: ", numero)
else:
    print("La opción que ingresaste no es valida.")