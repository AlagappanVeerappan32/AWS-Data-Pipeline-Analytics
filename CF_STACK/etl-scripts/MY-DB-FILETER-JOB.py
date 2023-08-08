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
AWSGlueDataCatalog_node1686945988032 = glueContext.create_dynamic_frame.from_catalog(
    database="dynamodb-data-source-table-cf", table_name="datasourcecf"
)

# Script generated for node Change Schema
ChangeSchema_node1686945999741 = ApplyMapping.apply(
    frame=AWSGlueDataCatalog_node1686945988032,
    mappings=[
        ("author", "string", "author", "string"),
        ("urltoimage", "string", "urltoimage", "string"),
        ("source.name", "string", "source.name", "string"),
        ("source.id", "string", "source.id", "string"),
        ("title", "string", "title", "string"),
        ("url", "string", "url", "string"),
    ],
)

# Script generated for node Amazon S3
AmazonS3_node1686946514073 = glueContext.write_dynamic_frame.from_options(
    frame=ChangeSchema_node1686945999741,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://data-source-extract-cf/DB-data-source/",
        "partitionKeys": [],
    },
)

job.commit()
