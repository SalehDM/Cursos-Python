import pandas as pd

def main():
    read_file = pd.read_excel ("C:/Users/PC\Desktop/Python/Intensivo desde 0/Ejercicio5/ejemplo.xlsx")

    read_file.to_csv ("C:/Users/PC\Desktop/Python/Intensivo desde 0/Ejercicio5/ejemplo_to_csv.csv", index = None, header=True)

    df = pd.DataFrame(pd.read_csv("C:/Users/PC\Desktop/Python/Intensivo desde 0/Ejercicio5/ejemplo_to_csv.csv"))

    print(df)
    
if __name__=='__main__':
    main()
