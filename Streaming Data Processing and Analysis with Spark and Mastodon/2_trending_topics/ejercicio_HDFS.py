import findspark
findspark.init()

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

# Cambiad <FILL_IN> por vuestro nombre de usuario
sc = SparkContext("local[2]", "ejercicio_HDFS_paulagili")
sc.setLogLevel("ERROR")

# Crear un StreamingContext con un intervalo de batch de 20 segundos
ssc = StreamingContext(sc, 20)


# Configurar la fuente de datos: leer datos del socket
puerto = 21002
lines = ssc.socketTextStream("localhost", puerto)


# Procesar datos: contar el número de toots enviados por cada usuario
authors = lines.map(lambda author: (author.strip(), 1))
author_counts = authors.reduceByKey(lambda a, b: a + b)

# Guardar el resultado en HDFS
# Cambia 'hdfs://<your-hdfs-path>' por la ruta HDFS correcta
output_path = "hdfs://Cloudera01:8020/user/paulagili/captura_toots/"
author_counts.saveAsTextFiles(output_path)

# Iniciar el StreamingContext
ssc.start()
ssc.awaitTermination()

ssc.start()
ssc.awaitTermination()






