import findspark
findspark.init()

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

# Cambiad <FILL_IN> por vuestro nombre de usuario
sc = SparkContext("local[2]", "top_words_paulagili")
sc.setLogLevel("ERROR")

micro_batch_length = 5
ssc = StreamingContext(sc, micro_batch_length)
ssc.checkpoint("checkpoint")

initialStateRDD = sc.parallelize([])

# CUIDADO: Introducid el puerto que se os ha proporcionado.
puerto=21002
netCatStream = ssc.socketTextStream("localhost", puerto)

running_counts = netCatStream.flatMap(lambda line: line.split(" "))\
    .map(lambda word: (word, 1))\
    .reduceByKeyAndWindow(lambda w1,w2: w1+w2,5,5)

running_counts.pprint()

ssc.start()
ssc.awaitTermination()