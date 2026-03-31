from awsglue.context import GlueContext
from pyspark.context import SparkContext
from awsglue.job import Job
from pyspark.sql.functions import col, lit
from pyspark.sql.types import DoubleType
from datetime import datetime

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

input_path = "s3://deepak-crypto-raw-data-2026-001/crypto-data/"

current_date = datetime.now()

year = str(current_date.year)
month = str(current_date.month).zfill(2)
day = str(current_date.day).zfill(2)

output_path = f"s3://deepak-crypto-processed-data-2026-001/processed-data/year={year}/month={month}/day={day}/"

df = spark.read.json(input_path)

if "bitcoin" in df.columns:
    transformed_df = df.select(
        col("bitcoin.usd").cast(DoubleType()).alias("bitcoin_price_usd")
    )
else:
    transformed_df = df

transformed_df = transformed_df \
    .withColumn("year", lit(year)) \
    .withColumn("month", lit(month)) \
    .withColumn("day", lit(day))

transformed_df.write.mode("overwrite").parquet(output_path)

job.commit()