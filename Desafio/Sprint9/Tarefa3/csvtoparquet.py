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

data_frame = spark.read.option("delimiter", "|").csv("s3://ex3sprint7bucket/upload/movies/2023/05/16/movies.csv/")

data_frame.write.parquet("s3://ex3sprint7bucket/Trusted/CSV/2023/06/12/")

job.commit()