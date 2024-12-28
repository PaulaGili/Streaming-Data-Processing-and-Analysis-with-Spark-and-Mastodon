import json
import re
from textblob import TextBlob
import findspark
findspark.init()

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

# Inicialización de SparkContext y StreamingContext
sc = SparkContext(appName="NombreStreaming", master="local[2]")
sc.setLogLevel("ERROR")

# Inicialización del StreamingContext (con 10 segundos de intervalo)
ssc = StreamingContext(sc, 15)

# Conectar al socket donde se reciben los toots de Mastodon
lines = ssc.socketTextStream("localhost", 21002)

# Función para procesar el sentimiento de un toot
def get_sentiment(toot):
    # Limpiar el texto (eliminamos URLs, menciones y hashtags)
    toot = re.sub(r'http\S+', '', toot)  # Eliminar URLs
    toot = re.sub(r'@[A-Za-z0-9_]+', '', toot)  # Eliminar menciones
    toot = re.sub(r'#[A-Za-z0-9_]+', '', toot)  # Eliminar hashtags

    # Análisis de polaridad con TextBlob
    blob = TextBlob(toot)
    polarity = blob.sentiment.polarity

    # Clasificar según la polaridad
    if polarity > 0:
        return 'positive'
    elif polarity < 0:
        return 'negative'
    else:
        return 'neutral'

# Convertir los toots en sus respectivos sentimientos
sentiments = lines.map(lambda toot: (get_sentiment(toot), 1))

# Aplicar la ventana de 90 segundos con un intervalo de 15 segundos
windowed_sentiments = sentiments.window(90, 15)

# Contar los sentimientos
sentiment_counts = windowed_sentiments.reduceByKey(lambda a, b: a + b)

# Función para mostrar los resultados
def print_results(rdd):
    if not rdd.isEmpty():
        result = rdd.collect()
        for sentiment, count in result:
            print("({}, {})".format(sentiment, count))


# Imprimir los resultados cada vez que se reciba una nueva ventana de datos
sentiment_counts.foreachRDD(print_results)

# Comenzar a procesar los datos
ssc.start()
ssc.awaitTermination()
