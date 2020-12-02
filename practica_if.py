"""print("Programa de evaluación")

nota_alumno=input("Ingrese su nota:")

def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="suspendido"
    return valoracion
print (evaluacion(int(nota_alumno)))"""

'''print("Verificación de acceso")

nota_alumno = int(input("Ingrese su nota: "))

if nota_alumno < 5:
    print("Insuficiente")
elif nota_alumno <6:
    print("Suficiente")
elif nota_alumno <7:
    print("Bien")
elif nota_alumno <9:
    print("Notable")
else:
    print("Sobresaliente")
print("El programa ha finalizado")'''

'''salario_presidente=int(input("Introduzca el salario del presidente: "))
print("Salario presidente: ", str(salario_presidente))

salario_director=int(input("Introduzca el salario del director: "))
print("Salario director: " + str(salario_director))

salario_jefe_area=int(input("Introduzca el salario del jefe de area: "))
print("Salario jefe de area: " + str(salario_jefe_area))

salario_admin=int(input("Introduzca el salario del admin: "))
print("Salario admin: ", str(salario_admin))

if salario_admin<salario_jefe_area<salario_director<salario_presidente:
    print("Correcto")
else:
    print("Algo falla")'''


'''print("Programa para validar becas 2020")

distancia_escuela = int(input("Ingrese en km la distancia de tu casa a la escuela: "))
print(distancia_escuela)

numero_hermanos = int(input("Ingrese el numero de hermanos: "))
print(numero_hermanos)

salario_familiar = int(input("Ingrese el salario familiar bruto al año: "))
print(salario_familiar)

if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:
    print("Tienes derecho a beca")
else:
    print("No tienes derecho a beca")'''
    
print("Asignaturas optativas 2020")

print("Informatica grafica - Pruebas de Software - Usabilidad")

opcion= input("Escribe la asignatura: ")

asignatura = opcion.lower()
if asignatura in ("informatica grafica", "pruebas de software", "usabilidad"):
    print("Asignatura elegida: " + asignatura)
else:
    print("Asignatura no contemplada")
