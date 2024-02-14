from pyspark.sql import SparkSession

def setUp():
    spark = SparkSession.builder.appName('test_pipeline').getOrCreate()
    return spark

def tearDown(spark):
    spark.stop()
