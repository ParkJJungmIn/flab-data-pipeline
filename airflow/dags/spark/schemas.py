from pyspark.sql.types import StructType, StructField, LongType, StringType, IntegerType, DoubleType

def get_event_data_schema():
    return StructType([
        StructField("ts", LongType()),
        StructField("userId", StringType()),
        StructField("sessionId", IntegerType()),
        StructField("page", StringType()),
        StructField("auth", StringType()),
        StructField("method", StringType()),
        StructField("status", StringType()),
        StructField("level", StringType()),
        StructField("itemInSession", IntegerType()),
        StructField("location", StringType()),
        StructField("userAgent", StringType()),
        StructField("lastName", StringType()),
        StructField("firstName", StringType()),
        StructField("registration", LongType()),
        StructField("gender", StringType()),
        StructField("artist", StringType()),
        StructField("song", StringType()),
        StructField("length", DoubleType()),
    ])
