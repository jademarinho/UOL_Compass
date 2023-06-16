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
AWSGlueDataCatalog_node1686919205366 = glueContext.create_dynamic_frame.from_catalog(
    database="csvrefined",
    table_name="filme",
    transformation_ctx="AWSGlueDataCatalog_node1686919205366",
)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1686919235365 = glueContext.create_dynamic_frame.from_catalog(
    database="csvrefined",
    table_name="avaliacao",
    transformation_ctx="AWSGlueDataCatalog_node1686919235365",
)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1686919334907 = glueContext.create_dynamic_frame.from_catalog(
    database="csvrefined",
    table_name="contagemvotos",
    transformation_ctx="AWSGlueDataCatalog_node1686919334907",
)

# Script generated for node Amazon S3
AmazonS3_node1686919246406 = glueContext.write_dynamic_frame.from_options(
    frame=AWSGlueDataCatalog_node1686919205366,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": "s3://ex3sprint7bucket/Refined/2023/06/16/Filme/",
        "partitionKeys": [],
    },
    transformation_ctx="AmazonS3_node1686919246406",
)

# Script generated for node Amazon S3
AmazonS3_node1686919308812 = glueContext.write_dynamic_frame.from_options(
    frame=AWSGlueDataCatalog_node1686919235365,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": "s3://ex3sprint7bucket/Refined/2023/06/16/Avaliacao/",
        "partitionKeys": [],
    },
    transformation_ctx="AmazonS3_node1686919308812",
)

# Script generated for node Amazon S3
AmazonS3_node1686919344209 = glueContext.write_dynamic_frame.from_options(
    frame=AWSGlueDataCatalog_node1686919334907,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": "s3://ex3sprint7bucket/Refined/2023/06/16/ContagemVotos/",
        "partitionKeys": [],
    },
    transformation_ctx="AmazonS3_node1686919344209",
)

job.commit()
