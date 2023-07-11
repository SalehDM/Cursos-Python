"""
Ejercicio 2
Enunciado: Crea una agenda de teléfonos que se gestione por consola, que te permita:
    Añadir a cualquier persona, indicando nombre y después teléfono
    Buscar el teléfono de una persona
Objetivo:
    Aprender a manejar la entrada y la salida por consola.
    El uso de colecciones (array o diccionario)
Ampliación:
    Al buscar a una persona, que te muestre todas aquellas que comiencen por el texto que has introducido. Ejemplo:
        Introduce un nombre: Pep
            Resultados:
                Pepe 659331013
                Pepe Martín 633743551

"""
import agenda as a
import os

contactos=dict()

def main():
    
    opc=0
    while opc!=1 and opc!=2 and opc!=3 and opc!=4 and opc!=5:
        os.system('cls')
        print('Bienvenido a su agenda, ¿qué desea realizar?')
        print('1. Añadir contacto.\n2. Buscar contacto.\n3. Eliminar contacto.\n4. Ver todos los contactos.\n5. Salir')
        opc=int(input('Intruduzca el número de la acción a realizar: '))

        if opc!=1 and opc!=2 and opc!=3 and opc!=4 and opc!=5:
            print('Valor fuera de rango, introduzca 1, 2 ó 3')
            input()
    
    match opc:
        case 1:
            nombre,telefono=a.nuevo_contacto(contactos)
            contactos[nombre]=telefono
            main()

        case 2:
            nombre_encontrado=a.buscar_contacto(contactos)
            if not nombre_encontrado:
                print('Contacto no encontrado')
            input()
            main()
        case 3:
            a.eliminar_contacto(contactos)
            input()
            main()
        case 4:
            a.ver_contactos(contactos)
            input()
            main()
        case 5:
            a.salir()
 



    






if __name__=='__main__':
    main()
