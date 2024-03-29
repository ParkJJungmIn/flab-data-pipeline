from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_unixtime
import sys
import os
from schemas import get_event_data_schema

def create_spark_session():
    return SparkSession.builder \
        .appName("DataProcessing") \
        .config("spark.hadoop.fs.s3a.endpoint", "https://s3.ap-northeast-2.amazonaws.com") \
        .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
        .config("spark.kryo.registrationRequired", "true") \
        .config('spark.hadoop.fs.s3a.impl', 'org.apache.hadoop.fs.s3a.S3AFileSystem') \
        .config('spark.hadoop.fs.s3a.aws.credentials.provider', 'org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider') \
        .getOrCreate()

def file_exists(spark, path):
    try:
        spark._jvm.org.apache.hadoop.fs.FileSystem.get(spark._jsc.hadoopConfiguration()) \
            .exists(spark._jvm.org.apache.hadoop.fs.Path(path))
        return True
    except Exception as e:
        print(f"Error checking file existence: {e}")
        return False

def main():
    spark = create_spark_session()
    schema = get_event_data_schema()
    data_path = f"s3a://pjm-project-datalake/bronze/event_data.json"
    output_path = f"s3a://pjm-project-datalake/silver/"

    # if not file_exists(spark, data_path):
    #     print(f"skipping processing.")
    #     spark.stop()
    #     return

    raw_data = spark.read.schema(schema).json(data_path)
    transformed_data = raw_data.withColumn("event_date", from_unixtime(col("ts") / 1000).cast("date"))
    transformed_data.write.partitionBy("event_date").mode("overwrite").parquet(output_path)
    spark.stop()

if __name__ == "__main__":
    main()
