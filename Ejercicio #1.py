print("========================")
print("Sistema Vacacional Rappi")
print("========================\n")

nom_empleado = input("Por favor ingresa tu nombre: ")
clave_departamento = int(input("Por favor ingresa la clave de tu departamento: "))
anios_laborados = float(input("Por favor ingresa el numeero de años que has laborado junto a la compañia: "))

if clave_departamento == 1:
    print("\nPerteneces al departamento de Atención al cliente")
    if anios_laborados <= 1.9 and anios_laborados > 1:
        print("Felicitaciones " + nom_empleado + " Tu periodo de vacaciones es de 6 días.")
    elif anios_laborados >= 2 and anios_laborados <= 6:
        print("Felicitaciones " + nom_empleado + " Tu periodo de vacaciones es de 14 días.")
    elif anios_laborados >= 7:
        print("Felicitaciones " + nom_empleado + " Tu periodo de vacaciones es de 20 días.")
    else:
        print ("Aún no puedes disfrutar de tus vacaciones.")
elif clave_departamento == 2:
    print("\nPerteneces al departamento de Logistica")
    if anios_laborados <= 1.9 and anios_laborados > 1:
        print("Felicitaciones " + nom_empleado + " Tu periodo de vacaciones es de 7 días.")
    elif anios_laborados >= 2 and anios_laborados <= 6:
        print("Felicitaciones " + nom_empleado + " Tu periodo de vacaciones es de 15 días.")
    elif anios_laborados >= 7:
        print("Felicitaciones " + nom_empleado + " Tu periodo de vacaciones es de 22 días.")
    else:
        print ("Aún no puedes disfrutar de tus vacaciones.")
elif clave_departamento == 3:
    print("\nPerteneces al departamento de Gerencia")
    if anios_laborados <= 1.9 and anios_laborados > 1:
        print("Felicitaciones " + nom_empleado + " Tu periodo de vacaciones es de 10 días.")
    elif anios_laborados >= 2 and anios_laborados <= 6:
        print("Felicitaciones " + nom_empleado + " Tu periodo de vacaciones es de 20 días.")
    elif anios_laborados >= 7:
        print("Felicitaciones " + nom_empleado + " Tu periodo de vacaciones es de 30 días.")
    else:
        print ("Aún no puedes disfrutar de tus vacaciones.")
else:
    print("La clave de departamento ingresada no es valida.")