import requests
import json
import time
import random
import socket
from mastodon import Mastodon

puerto=21002#se debe cambiar <FILL_IN> por el número de puerto que tenéis asignado
access_token='XR0MVrACxUf9MhF8uNmW0uzf4TbQRDPm44TEfviuPDw'#se debe cambiar <FILL_IN> por el token de la aplicación Mastodon 

print("Esperando la conexión de Spark...")
#se abre la comunicación mediante un socket al que se conectará Spark
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind(('localhost', puerto))
s.listen(1)
conn, addr = s.accept() 

print("Iniciando la conexión a Mastodon")
#se inicia la conexión a Mastodon
url= 'https://mastodon.social'
api = Mastodon(access_token=access_token, api_base_url="https://mastodon.social")

tiempo=0
contador=0

while (tiempo<60 and contador < 100):    #contador se utiliza para limitar a 100 las peticiones
    inicio = time.time()
    respuesta=api.timeline()# Aquí se modificaría la consulta a Mastodon
    fin = time.time()
    tiempo=fin-inicio

    for toot in respuesta:
        print(toot['content'])
        conn.sendall((toot['content']+"\n").encode('utf-8'))  # envia el contenido del toot por el socket
        time.sleep(1) # espera para no enviar todos los toots de golpe y que se puedan visualizar
    
    contador+=1
    time.sleep(10) # espera de cortesía para no sobrecargar el servidor con peticiones

conn.close()