import os

def nuevo_contacto(contactos):
    os.system('cls')
    print('Introduzca los datos del nuevo contacto.')
    nombre=input('Nombre: ')
    if nombre in contactos:
        print('El nombre ya existe.')
        input()
        return nuevo_contacto(contactos)
    else:
        telefono=int(input('Número de teléfono: '))
    return (nombre,telefono)

def buscar_contacto(contactos):
    os.system('cls')
    nombre_a_buscar=input('Introduzca el nombre del contacto a buscar: ')
    var_auxiliar=False
    for (nombre) in contactos.keys():
        if nombre_a_buscar.lower() in nombre.lower():
            print(f'Nombre: {nombre}\nNúmero de telefono: {contactos[nombre]}')
            var_auxiliar=True
    return var_auxiliar

def eliminar_contacto(contactos):
    os.system('cls')
    contacto_a_eliminar=input('Introduzca el nombre del contacto a eliminar: ')
    contacto_eliminado=str(contactos.pop(contacto_a_eliminar,'Tiene que introducir el nombre como está en el reistro de contactos'))
    
    if 'Tiene' in contacto_eliminado:
        print('El contacto no se ha eliminaddo')
        print(contacto_eliminado)
    else:
        print(f'Numero de teléfono: {contacto_eliminado}')
        print('Contacto eliminado')

def ver_contactos(contactos):
    os.system('cls')
    print('Contactos')
    for (nombre) in contactos.keys():
        print(f'Nombre: {nombre}\nNúmero de telefono: {contactos[nombre]}\n')

def salir():
    os.system('cls')
    quit()