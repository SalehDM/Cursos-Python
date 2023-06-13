def main():
    paises=input("Introduce una lista de paises separados por comas:\n")
    lpaises=set(paises.lower().title().split(","))
    print(sorted(list(lpaises)))

if __name__=='__main__':
    main()