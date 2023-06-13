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