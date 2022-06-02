import datetime, os, requests, json, random
from deep_translator import GoogleTranslator
import subprocess as sub
import webbrowser as web

import pywhatkit

def get_hora():
    return datetime.datetime.now().strftime('%I:%M %p')

def call_YT(music):
    pywhatkit.playonyt(music)

def open_apps(app):
    apps = ['whatsapp', 'spotify']
    pathW = 'C:/Users/Yonatan Ortiz/AppData/Local/WhatsApp'

    if apps[0] in app:            
        os.chdir(pathW)
        sub.call('start WhatsApp.exe',  shell=True)
    else:
        web.open(apps[1])

def get_clima():
    api_key = '53e210f796c02047bf883cae8dcf769d'
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "Mexico"

    traductor = GoogleTranslator(source='auto', target='es')
    
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
    
    response = requests.get(complete_url) 
    
    x = response.json()     

    if x['cod'] == 200:
        y = x["main"] 

        current_temperature = y["temp"] - 273.15
        temperatura = "{0:.2f}".format(current_temperature)
        current_pressure = y["pressure"] 
        current_humidiy = y["humidity"] 
        
        z = x["weather"] 
        weather_description = z[0]["description"]
        res = traductor.translate(weather_description)
        res = res.replace('nubes', '')

        respuesta = f"Temperatura: {temperatura} grados centigrados. Precion atmosferica: {current_pressure} pascales. Humedad: {current_humidiy}%. Cielo: {res}" 
    
    else: 
        respuesta = 'No encontre la ciudad'
    
    return respuesta

def get_chiste():
    base_uri = 'https://v2.jokeapi.dev/joke/Any?lang=es&amount=10'

    response = requests.get(base_uri)

    x = response.json()
    chistes = x['jokes']
    index = random.randint(0, len(chistes) - 1)
    chiste = chistes[index]

    if chiste['type'] == 'single':
        respuesta = chiste['joke']
    else:
        preg = chiste['setup']
        res = chiste['delivery']
        respuesta = f'{preg} {res}'

    return respuesta

def get_estado():
    estados = ["muy feliz porque estoy contigo", "muy triste, ¿Me abrazas?", "enojada, tengo hambre", "aburrida, bamonos a beber", "muy cachonda, ¿Vamos a besarnos?"]
    index = random.randint(0, len(estados) - 1)

    return estados[index]