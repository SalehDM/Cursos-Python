"""
Ejercicio 5
Enunciado: Convierte un Excel a CSV
Objetivo:
    Aprender a trabajar con ficheros
    Usar la librería pandas de Python
"""
import pandas as pd

def main():
    read_file = pd.read_excel ("C:/Users/PC\Desktop/Python/Intensivo desde 0/Ejercicio5/ejemplo.xlsx")

    read_file.to_csv ("C:/Users/PC\Desktop/Python/Intensivo desde 0/Ejercicio5/ejemplo_to_csv.csv", index = None, header=True)

    df = pd.DataFrame(pd.read_csv("C:/Users/PC\Desktop/Python/Intensivo desde 0/Ejercicio5/ejemplo_to_csv.csv"))

    print(df)
    
if __name__=='__main__':
    main()
