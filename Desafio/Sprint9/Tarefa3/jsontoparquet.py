import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

df_movies = spark.read.option("multiline", "true").json("s3://ex3sprint7bucket/Raw/TMDB/JSON/2023/06/02/*.json")

df_movies.write.parquet("s3://ex3sprint7bucket/Trusted/JSON/2023/06/12")

job.commit()