"""
Enunciado del ejercicio:
    En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.
"""
import pickle
import vehiculo as v

def main():
    vespa=v.Vehiculo('rojo',2,0)
    vespa.tipo()

    f=open('C:/Users/PC/Desktop/Python/Python/Tema8/Ejercicio2/datos.bin','wb')
    pickle.dump(vespa,f)
    f.close()

    f=open('C:/Users/PC/Desktop/Python/Python/Tema8/Ejercicio2/datos.bin','rb')
    vehiculoGuardado=pickle.load(f)
    f.close()

    vehiculoGuardado.tipo()

if __name__=='__main__':
    main()
