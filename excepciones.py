'''def divide():
    try:
        op1 = (float(input("Introduce el primer numero: ")))
    
        op2 = (float(input("Introduce el primer numero: ")))
    
        print("La división es: "+ str(op1/op2))
    except ValueError:
        
        print("Valores erroneos:")
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    
    print("Calculo finalizado.")
divide()'''

def evalua_edad(edad):
    if edad<0:
        raise TypeError("Su edad no puede ser negativa")
    
    if edad<20:
        return "Eres muy joven"
    elif edad<40:
        return "Eres joven"
    elif edad<65:
        return "Eres maduro"
    elif edad<100:
        return "Cuidate"
    
print(evalua_edad(-15))