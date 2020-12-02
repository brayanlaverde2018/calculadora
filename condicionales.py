print("=========")
print("Conversor")
print("=========")
print("Menú de opciones:")
print("Presione 1 para convertir de numero a palabra.")
print("Presione 2 para convertir de palabra a numero.")
opcion = int(input("¿Que deseas hacer?: "))
if opcion == 1 :
  print("Conversor de numero a palabra")
  numero = int(input("¿Cual es el numero que deseas convertir?: "))
  if numero == 1:
    print("El numero es uno")
  elif numero == 2:
    print ("El numero es dos")
  elif numero == 3:
    print ("El numero es tres")
  elif numero == 4:
    print ("El numero es cuatro")
  elif numero == 5:
    print ("El numero es cinco")
  else:
    print ("Numero no disponible")
elif opcion == 2:
  print("Conversor de palabra a numero")
  palabra = input("¿Cual es la palabra que deseas convertir?: ")
  palabra = palabra.lower()
  if palabra  == "uno":
    print("La palabra es 1")
  elif palabra == "dos":
    print ("La palabra es 2")
  elif palabra == "tres":
    print ("La palabra es 3")
  elif palabra == "cuatro":
    print ("La palabra es 4")
  elif palabra == "cinco":
    print ("La palabra es 5")
  else: 
    print("Palabra no disponible")
else:
  print("Opción no valida")
print("Fin.")