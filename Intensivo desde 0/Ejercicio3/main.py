"""
Ejercicio 3
Enunciado: Crea una función que calcule los números primos entre 1 y N, siendo N el parámetro que recibe la función.
Objetivo:
    Uso de bucles anidados
    El uso de colecciones
"""
import os

def primos_o_no (num):
    iterador=num

    while iterador>2:
        iterador-=1
        if num % iterador == 0:
            return False
            break
    return True

def main():
    os.system('cls')
    print('Calcular números primos')
    print('Introduzca un número entero mayor que 1')
    num=int(input())
    while num<1:
        print('Número incorrecto, introduzca un número entero mayor que 1')
        num=int(input())

    primos=list(filter(primos_o_no,list(range(num,1,-1))))

    print(f'Los números primos entre el {num} y el 1 son {", ".join(map(str, primos))}')

if __name__=='__main__':
    main()
