print("**************************************************")
print("* Programa para identificar el numero mas grande *")
print("**************************************************\n")

num_uno = float(input("Ingrese el primer numero: "))
num_dos = float(input("Ingrese el segundo numero: "))
num_tres = float(input("Ingrese el tercer numero: "))

if num_uno > num_dos and num_uno > num_tres:
    print("El numero mayor es ", num_uno)
elif num_dos > num_tres:
    print("El numero mayor es ", num_dos)
else:
    print ("El numero mas grande es ", num_tres)