import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1686775870407 = glueContext.create_dynamic_frame.from_catalog(
    database="csvrefined",
    table_name="joincsvjson6",
    transformation_ctx="AWSGlueDataCatalog_node1686775870407",
)

# Script generated for node Amazon S3
AmazonS3_node1686775925157 = glueContext.write_dynamic_frame.from_options(
    frame=AWSGlueDataCatalog_node1686775870407,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": "s3://ex3sprint7bucket/Refined/2023/06/14/",
        "partitionKeys": [],
    },
    transformation_ctx="AmazonS3_node1686775925157",
)

job.commit()
