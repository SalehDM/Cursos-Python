def main():
    f=open('C:/Users/PC/Desktop/Python/Python/Tema8/Ejercicio1/archivo.txt','wt')
    f.close()

    f=f=open('C:/Users/PC/Desktop/Python/Python/Tema8/Ejercicio1/archivo.txt','a')
    f.write('Estamos añadiendo texto')
    f.close()

if __name__=='__main__':
    main()