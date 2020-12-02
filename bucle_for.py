contador = 0

dir_email = input("Ingrese su correo: ")

for i in dir_email:
    if (i=="@" or i=="."):
        contador = contador+1

if contador == 2:
    print("el email " + dir_email + " es correcto")
else:
    print("El email " + dir_email + " es incorrecto")
    