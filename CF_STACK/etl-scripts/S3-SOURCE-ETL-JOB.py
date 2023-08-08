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
AWSGlueDataCatalog_node1686955307138 = glueContext.create_dynamic_frame.from_catalog(
    database="s3-data-source-cf", table_name="data_source_s3_2_cf"
)

# Script generated for node Change Schema
ChangeSchema_node1686955324264 = ApplyMapping.apply(
    frame=AWSGlueDataCatalog_node1686955307138,
    mappings=[
        ("col0", "string", "col0", "string"),
        ("col1", "string", "col1", "string"),
        ("col3", "string", "col3", "string"),
        ("col5", "string", "col5", "string"),
    ],
)

# Script generated for node Amazon S3s
AmazonS3_node1686955612472 = glueContext.write_dynamic_frame.from_options(
    frame=ChangeSchema_node1686955324264,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://data-source-extract-cf/S3-data-source/",
        "partitionKeys": [],
    },
)

job.commit()
