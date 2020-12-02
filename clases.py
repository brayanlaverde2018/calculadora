class Coche():
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False
    
    def arrancar(self):
        """
        Este metodo hace arancar al coche
        """
        self.enmarcha = True

    def estado(self):
        if(self.enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta detenido"
        
miCoche=Coche()

print(miCoche.largoChasis)
print("El coche tiene: ",miCoche.ruedas,"ruedas")
miCoche.arrancar()

print(miCoche.estado())