"""
Enunciado del ejercicio:
    En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa. Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.
    En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, haréis una operación para calcular el tiempo que queda de trabajo.
"""
from datetime import datetime

def main():
    hora=datetime.now().hour
    minutos=datetime.now().minute
    if hora<19:
        print("Su jornada laboral aun no ha finalizado.")
        if 18-hora==0:
            print("Faltan ",60-minutos," minutos para finalizar.")
        else:
            print("Faltan ",18-hora," horas y ",60-minutos," minutos para finalizar.")
    else:
        print("Su jornada laboral ha finaliza, pase buena tarde.")










if __name__=='__main__':
    main()
