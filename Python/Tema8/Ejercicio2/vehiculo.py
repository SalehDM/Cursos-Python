class Vehiculo:
    def __init__(self,color,ruedas,puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        
    def tipo(self):
        if self.puertas==0:
            print(f"El vehículo de color {self.color}, {self.ruedas} rudas y {self.puertas} puertas es una moto")
        else:
            print(f"El vehículo de color {self.color}, {self.ruedas} rudas y {self.puertas} puertas no es una moto") 
