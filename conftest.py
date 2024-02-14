import os

from pyspark.sql import SparkSession
from pathlib import Path

ROOT_DIR = Path(__file__).parent
TEST_FILE_PATH = str(Path(__file__).parent) + '/' + 'tests'

print('gkl')
print(ROOT_DIR)
print(TEST_FILE_PATH)
def setUp():
    spark = SparkSession.builder.appName('test_pipeline').getOrCreate()
    return spark

def tearDown(spark):
    spark.stop()
