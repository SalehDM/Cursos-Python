"""
Enunciado del ejercicio:
    En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.
"""
from functools import reduce
def main():
    numeros=list(range(1,50))
    lnumeros=reduce(lambda a,b:a+b,filter(lambda x:x%2==1,numeros))
    print(lnumeros)
    
if __name__=='__main__':
    main()
