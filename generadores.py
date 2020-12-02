'''def genera_pares(limite):
    
    num= 1
        
    while num<limite:
        
        yield num*2
        
        num=num+1
        
devuelve_pares = genera_pares(10)

print(next(devuelve_pares))

print("Aqui podría ir mas codigo")

print(next(devuelve_pares))

print("Aqui podría ir mas codigo")

print(next(devuelve_pares))'''

def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        #for subelemento in elemento:
            yield from elemento
        
ciudades_devueltas = devuelve_ciudades("Madrid", "Barcelona","Bogota", "Cali")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))
