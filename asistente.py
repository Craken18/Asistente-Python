#Librerias necesarias
import speech_recognition as sr
import pyttsx3, signal, sys
from pwn import *
import tareas


#Inicializacion de las librerias
listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 160)

#Variables globales
name = 'alexa'
message = 'Hola mi amor, que deceas hoy'
p = log.progress('Asistente por Voz')
p.status('Iniciando APP')


#Inicio del programa
engine.say(message)
engine.runAndWait()

#Funcion de ejecucion
def talk(text):
    engine.say(text)
    engine.runAndWait()

#Funcion de escucha
def listen():
    try:
        with sr.Microphone() as source:
            p.status("Escuchando")
            voice = listener.listen(source, phrase_time_limit=30)
            rec = listener.recognize_google(voice, language='es-MX')
            rec = rec.lower()
            #Condicion para busqueda por voz
            if name in rec:
                p.status('Comando valido')
                rec = rec.replace(name, '')
                run(rec)
            else:
                p.failure('No se encontro resultado')
                listen()
    except:
        sys.exit()
    

#Funcion principal
def run(rec):
    #Condicion la accion a ejecutar
    if 'reproduce' in rec:
        p.status('Reproduciendo')
        music = rec.replace('reproduce', '')
        talk('Reproduciendo ' + music)
        tareas.call_YT(music)
    elif 'hora' in rec:
        p.status('Hora')
        hora = tareas.get_hora()
        talk('Son las ' + hora)
    elif 'abre' in rec:
        p.status("Abriendo")
        order = rec.replace('abre', '')
        tareas.open_apps(app=order)
        talk(f'Abriendo {order}')
    elif 'clima' in rec:
        p.status("Clima")
        res = tareas.get_clima()
        talk(f'El tiempo de hoy es: {res}')
    elif 'chiste' in rec:
        chiste = tareas.get_chiste()
        talk(chiste)
    elif 'cómo estás' in rec:
        estado = tareas.get_estado()
        talk(f'Estoy {estado}')
    elif 'hasta luego' in rec or 'adiós' in rec:
        p.success('Finalizando')
        talk("Adios...")
        sys.exit()
    else:
        talk('Lo siento, no te entendi')
    
    listen()

#Funcion para detener el programa
def def_handler(sig, frame):
    p.success('Finalizando')
    sys.exit()    

# Ctrl+C
signal.signal(signal.SIGINT, def_handler)

if __name__ == '__main__':
    listen()
