from pyspark.sql import SparkSession
from pyspark.sql.functions import from_unixtime, col, dayofweek, hour, avg, countDistinct, first

def create_spark_session():
    return SparkSession.builder \
        .appName("GoldLayerDataProcessing") \
        .config("spark.hadoop.fs.s3a.endpoint", "https://s3.ap-northeast-2.amazonaws.com") \
        .config('spark.hadoop.fs.s3a.impl', 'org.apache.hadoop.fs.s3a.S3AFileSystem') \
        .config('spark.hadoop.fs.s3a.aws.credentials.provider', 'org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider') \
        .getOrCreate()

def process_data_for_gold_layer(spark):
    silver_data_path = "s3a://pjm-project-datalake/silver/"
    gold_data_path = "s3a://pjm-project-datalake/gold/"

    df = spark.read.parquet(silver_data_path)

    df = df.withColumn("event_date", from_unixtime(col("ts") / 1000).cast("date")) \
           .withColumn("date_id", from_unixtime(col("ts") / 1000).cast("date")) \
           .withColumn("event_hour", hour(from_unixtime(col("ts") / 1000))) \
           .withColumn("event_dayofweek", dayofweek(from_unixtime(col("ts") / 1000)))

    engagement_df = df.groupBy("userId", "event_date", "date_id") \
        .agg(
            countDistinct("sessionId").alias("daily_sessions"),
            avg("itemInSession").alias("avg_items_per_session"),
            first("event_hour").alias("first_event_hour"),
            first("event_dayofweek").alias("event_dayofweek")
        )

    engagement_df.write.partitionBy("date_id").mode("overwrite").parquet(gold_data_path)

def main():
    spark = create_spark_session()
    process_data_for_gold_layer(spark)
    spark.stop()

if __name__ == "__main__":
    main()
