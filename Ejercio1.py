class Vehiculo:
    color = "Blanco"
    ruedas = 4
    puertas = 5

class Coche(Vehiculo):
    velocidad = "140 km/h"
    cilindrada = "1500 CC"

coche = Coche()
print ("Las características del coche son:")
print ("Color: ", coche.color)
print ("Ruedas: ", coche.ruedas)
print ("Puertas: ", coche.puertas)
print ("Velocidad: ", coche.velocidad)
print ("Cilindrada: ", coche.cilindrada)
print
