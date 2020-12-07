class Coche():
    
    def __init__(self):
        
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False
    
    def arrancar(self,arrancamos):
        self.__enmarcha = arrancamos
        
        if(self.__enmarcha):
            chequeo=self.__chequeointerno()
        if(self.__enmarcha and chequeo):
            return "El coche esta en marcha"
        elif(self.__enmarcha and chequeo==False):
            return "Hay algo mal en el chequeo, no se puede arrancar"
        else:
            return "El coche esta detenido"
    
    def estado(self):
        print("El coche tiene ",self.__ruedas,"ruedas. Un ancho de", self.__anchoChasis,"Y un largo de ",self.__largoChasis)
        
    def __chequeointerno(self):
        print("Realizando chequeo interno")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"
        
        if self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas":
            return True
        else:
            return False
miCoche=Coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("-----------------A continuación esta el segundo objeto-----------------------")

miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()