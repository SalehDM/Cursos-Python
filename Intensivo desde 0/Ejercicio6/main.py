"""
Ejercicio 6
Enunciado: Crea una función que convierta un password (entre 6 y 12 caracteres) es una cadena de texto alfanumérica de 32 caracteres. La función SIEMPRE debe devolver el mismo resultado para la misma entrada.
Objetivo:
    Aprender a manejar los bucles y las cadena de texto.
    Mejorar la capacidad algorítmica.
"""
import os

def encode(word):
    CHARACTERS='ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz0123456789'
    aux=True
    encode_word=''
    for aux2 in range(6):
        for character in word:
            pos_character=CHARACTERS.find(character)
            
            if aux:
                encode_word+=CHARACTERS[pos_character-7-aux2]
                aux=False
            else:
                encode_word+=CHARACTERS[pos_character-17-aux2]
                aux=True
            if len(encode_word)==32:
                break
        if len(encode_word)==32:
                break

    return encode_word

def main():
    os.system('cls')
    password=input('Introduzca una contraseña alfanumérica que contenga entre 6 y 12 caracteres:\n')
    while len(password)<6 or len(password)>12 or not password.isalnum():
        os.system('cls')
        if len(password)<6:
            print('La contraseña es inferior a 6 caracteres.')
        elif len(password)>12:
            print('La contraseña es superior a 12 caracteres.')
        elif not password.isalnum():
            print('La contraseña contiene caracteres que no son alfanuméricos.')
    
        password=input('Introduzca una contraseña alfanumérica que contenga entre 6 y 12 caracteres:\n')    
    
    encode_password=encode(password)
    os.system('cls')
    print(f'Contraseña: {password}\nContraseña codificada: {encode_password}')
    print(f'Número de caracteres de contraseña codificada: {len(encode_password)}')

if __name__=='__main__':
    main()
