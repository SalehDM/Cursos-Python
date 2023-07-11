"""
Ejercicio 1
Enunciado: Imprime todos los ficheros existentes en tu carpeta de Descargas.

Objetivo:
    Aprender a utilizar librerías sencillas (en este caso, os) y sus funciones.
    Aprender a utilizar los bucles y los condicionales.
El algoritmo del ejercicio es el siguiente:
    Obtén todos los ficheros y directorios de un directorio en concreto. Para ello necesitas una función existente en la librería os (Sistema Operativo) de Python.
    Recorre todos los resultados obtenidos por la función anterior. Lo puedes hacer, por ejemplo, con un bucle for.
    Imprime por pantalla solo aquellos resultados que sean ficheros (para ello también necesitas una función existente en os.
Ampliación:
    Lista los tamaños de los ficheros en formato humano.
    Recorre de manera recursiva todos los directorios desde tu carpeta personal y muestra los ficheros de cada directorio y su tamaño.
"""
import os

def main():
    descargas_dir='C:/Users/PC/Downloads/'
    print('*****************************Solo ficheros*****************************')
    with os.scandir(descargas_dir) as ficheros:
        for fichero in ficheros:
            if fichero.is_file():
                print(f'{fichero.name} -> {os.stat(fichero).st_size} bytes')

    print('*****************************Listar un directorio de forma recursiva.*****************************')        
    for ruta_directorio, carpetas, ficheros in os.walk(descargas_dir):
        print(ruta_directorio)
        with os.scandir(ruta_directorio) as archivos:
            for archivo in archivos:
                print(f'{archivo.name} -> {os.stat(archivo).st_size} bytes')
          
if __name__=='__main__':
    main()
