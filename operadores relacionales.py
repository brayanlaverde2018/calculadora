print("Introduce dos números para comparar\n")
num_uno = int(input("Ingrese el primer numero: "))
num_dos = int(input("Ingrese el segundo numero: "))
num_uno = str(num_uno)
num_dos = str(num_dos)
print("\nLos numeros a comparar son: " + num_uno + " y " + num_dos + "\n")
if num_uno != num_dos:
    print("Son diferentes")
else:
    print("Son iguales")
if num_uno > num_dos:
    print(num_uno + " Es mayor que " + num_dos)
else:
    print(num_uno + " No es mayor que " + num_dos)
if num_uno < num_dos:
    print(num_uno + " Es menor que " + num_dos)
else:
    print(num_uno + " No es menor que " + num_dos)
if num_uno >= num_dos:
    print(num_uno + " Es mayor o igual que " + num_dos)
else:
    print(num_uno + " No es mayor o igual que " + num_dos)
if num_uno <= num_dos:
    print(num_uno + " Es menor o igual que " + num_dos)
else:
    print(num_uno + " No es menor o igual que " + num_dos)