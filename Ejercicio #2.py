print("****************************************************")
print("* Sistema para identificar numeros pares o impares *")
print("****************************************************\n")

numero = int(input("Ingrese el numero que desse identificar: "))

resultado = numero % 2

if resultado == 0:
    print("El número ", numero, "es par.")
else:
    print("El número ", numero, "es impar.")

