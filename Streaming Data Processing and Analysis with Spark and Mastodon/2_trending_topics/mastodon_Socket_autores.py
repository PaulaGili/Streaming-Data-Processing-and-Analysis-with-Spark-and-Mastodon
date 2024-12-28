import requests
import json
import time
import random
import socket
from mastodon import Mastodon

puerto = 21002  # Cambiar por el número de puerto asignado
access_token = 'XR0MVrACxUf9MhF8uNmW0uzf4TbQRDPm44TEfviuPDw'  # Cambiar por el token de la aplicación Mastodon

print("Esperando la conexión de Spark...")
# Se abre la comunicación mediante un socket al que se conectará Spark
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', puerto))
s.listen(1)
conn, addr = s.accept()

print("Iniciando la conexión a Mastodon")
# Se inicia la conexión a Mastodon
url = 'https://mastodon.social'
api = Mastodon(access_token=access_token, api_base_url="https://mastodon.social")

tiempo = 0
contador = 0

while tiempo < 60 and contador < 100:  # Limitar a 100 peticiones o 60 segundos
    inicio = time.time()
    respuesta = api.timeline()
    fin = time.time()
    tiempo = fin - inicio

    for toot in respuesta:
        autor = toot['account']['acct']  # Obtén el autor del toot
        print(autor)
        conn.sendall((autor + "\n").encode('utf-8'))  # Envía el autor por el socket
        time.sleep(1)  # Espera para evitar saturar el receptor

    contador += 1
    time.sleep(10)  # Espera de cortesía para no sobrecargar el servidor

conn.close()
