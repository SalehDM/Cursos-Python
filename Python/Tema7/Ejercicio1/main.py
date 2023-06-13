import operaciones as oper

def main():
    print ("CALCULADORA")
    print("Introduzca dos números enteros e indique la operación que desea realizar.")
    num1=int(input("Intreoduzca el primer número: "))
    num2=int(input("Intreoduzca el segundo número: "))
    calculo=int(input("Introduzca el número de la operación que desea realizar:\n1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n"))
    match calculo:
        case 1:
            print("El resultado es: ",oper.sumar(num1,num2))
        case 2:
            print("El resultado es: ",oper.restar(num1,num2))
        case 3:
            print("El resultado es: ",oper.multiplicar(num1,num2))
        case 4:
            print("El resultado es: ",oper.dividir(num1,num2))

if __name__=='__main__':
    main()