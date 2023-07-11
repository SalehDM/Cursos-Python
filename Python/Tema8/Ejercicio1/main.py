"""
Enunciado del ejercicio:
    En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.
"""
def main():
    f=open('C:/Users/PC/Desktop/Python/Python/Tema8/Ejercicio1/archivo.txt','wt')
    f.close()

    f=f=open('C:/Users/PC/Desktop/Python/Python/Tema8/Ejercicio1/archivo.txt','a')
    f.write('Estamos añadiendo texto')
    f.close()

if __name__=='__main__':
    main()
