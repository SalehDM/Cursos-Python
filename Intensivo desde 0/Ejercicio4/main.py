import requests
import json
import os

def main():
    os.system('cls')
    city=input('Introduzca la ciudad de la que desea obtener la temperatura máxima y la temperatura mínima.\n')

    url=f'https://api.openweathermap.org/data/2.5/weather?q={city.capitalize()}&appid=bab80304409291a5a8bd6125b2a78e6a'
    data=requests.get(url).json()

    if data['cod']=='404':
        os.system('cls')
        print('Ciudad no encontrada.')
    else:
        os.system('cls')
        tempMax=data['main']['temp_max']-273.15
        tempMin=data['main']['temp_min']-273.15
        print(f'Ciudad: {city.capitalize()}\nTemperatura máxima: {round(tempMax,2)} °C\nTemperatura mínima: {round(tempMin,2)} °C')


if __name__=='__main__':
    main()