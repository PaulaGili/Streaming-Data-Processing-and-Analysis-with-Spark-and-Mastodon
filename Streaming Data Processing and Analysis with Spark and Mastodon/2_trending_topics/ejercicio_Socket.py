import findspark
findspark.init()

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

# Cambiad <FILL_IN> por vuestro nombre de usuario
sc = SparkContext("local[2]", "ejercicio_Socket_paulagili")
sc.setLogLevel("ERROR")
ssc = StreamingContext(sc, 15)

puerto = 21002
stream = ssc.socketTextStream("localhost", puerto)

def clean_html(text):
    while True:
        start_tag = text.find("<")
        end_tag = text.find(">")

        # Si se encuentran etiquetas HTML
        if start_tag != -1 and end_tag != -1:
            text = text[:start_tag] + text[end_tag + 1:]
        else:
            break  
    
    return text.lower().split()
        

words = stream.flatMap(lambda line: clean_html(line))
word_counts = words.map(lambda word: (word,1))
word_counts = word_counts.reduceByKey(lambda a, b: a + b)

top_words = word_counts.transform(
    lambda rdd: rdd.sortBy(lambda x: x[1], ascending=False)
    .zipWithIndex()
    .filter(lambda x: x[1] < 10)
    .map(lambda x: x[0])
)

top_words.pprint()

ssc.start()
ssc.awaitTermination()

import requests
import json
import time
import random
import socket
from mastodon import Mastodon

puerto = 21002  # Cambiar <FILL_IN> por el número de puerto asignado
access_token = 'XR0MVrACxUf9MhF8uNmW0uzf4TbQRDPm44TEfviuPDw'  # Cambiar <FILL_IN> por el token de Mastodon

print("Esperando la conexión de Spark...")
# Abre la comunicación mediante un socket al que se conectará Spark
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind(('localhost', puerto))
s.listen(1)
conn, addr = s.accept() 

print("Iniciando la conexión a Mastodon")
# Inicia la conexión a Mastodon
url = 'https://mastodon.social'
api = Mastodon(access_token=access_token, api_base_url="https://mastodon.social")

tiempo = 0
contador = 0

while tiempo < 60 and contador < 100:  # Limita el tiempo y las peticiones
    inicio = time.time()
    respuesta = api.timeline()
    fin = time.time()
    tiempo = fin - inicio

    for toot in respuesta:
        autor = toot['account']['acct']  # Obtiene el autor del toot
        print(autor)
        conn.sendall((autor + "\n").encode('utf-8'))  # Envía el autor por el socket
        time.sleep(1)  # Espera para no enviar todos los toots de golpe
    
    contador += 1
    time.sleep(10)  # Espera de cortesía para no sobrecargar el servidor con peticiones

conn.close()

