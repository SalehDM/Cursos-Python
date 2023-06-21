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
