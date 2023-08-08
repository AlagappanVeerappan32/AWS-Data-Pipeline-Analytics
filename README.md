# AWS-Data-Pipeline-Analytics
Data Pipeline, Processing, and BI Visualization on AWS: Collect, process, and analyze data from Amazon S3 and an external API using AWS Glue, Athena, and QuickSight. Gain insights through intuitive dashboards.

# Data Pipeline and Analytics with BI Visualization

Welcome to the Data Pipeline and Analytics with BI Visualization project repository! This project aims to create a robust and efficient data pipeline that collects, processes, and analyzes data from Amazon S3 and an external API using AWS services. The insights obtained are then visualized using Amazon QuickSight, enabling data-driven decision-making.

## Application Details

### Project Goal
The main objective of this project is to establish a comprehensive data pipeline that:
- Collects data from Amazon S3 and an external API (NEWS API).
- Processes and transforms the collected data using AWS Glue.
- Enables querying and analysis of the data using AWS Athena.
- Visualizes the insights through intuitive dashboards using Amazon QuickSight.
- Operates in a serverless manner, reducing operational overhead.

### Project Overview
1. **Data Sources:**
   - **Amazon S3:** Cloud-based storage for unstructured/semi-structured data.
   - **API (NEWS API):** Fetches real-time updates based on keywords.

2. **Data Collection:**
   - Regularly fetches data from S3 and the API to ensure up-to-date information.
   - Data is stored in both Amazon S3 and DynamoDB.

3. **Data Processing and Filtering:**
   - **AWS Glue:** Fully managed ETL service for data preparation and transformation.
   - Efficiently processes and transforms data from S3 and the API into a structured format.

4. **Data Querying and Analysis:**
   - **AWS Athena:** Interactive query service for running standard SQL queries on S3-stored data.
   - Perform data analysis based on specific conditions and filters.

5. **BI Visualization:**
   - **Amazon QuickSight:** BI service for creating interactive visualizations and dashboards.
   - Present analysis results through user-friendly and insightful visualizations.

## Getting Started
### Prerequisites
- Familiarity with AWS services like S3, Glue, Athena, and QuickSight.
- AWS CLI configured with the necessary permissions.

### Installation
1. Clone this repository
2. Configure your AWS credentials: Follow [AWS CLI Configuration](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html).
3. Set up your data pipeline by creating Glue jobs, Athena queries, and QuickSight visualizations.

### Usage
- Regularly fetch data from Amazon S3 and the API to keep the information up to date.
- Run Glue jobs to process and transform the data.
- Query data using AWS Athena to perform various analysis tasks.
- Create intuitive dashboards and visualizations using Amazon QuickSight.

<img width="1172" alt="Screenshot 2023-08-08 at 7 14 22 PM" src="https://github.com/AlagappanVeerappan32/AWS-Data-Pipeline-Analytics/assets/133504573/a3009c08-292b-4050-b303-f77f50e7b890">


## Notes
- Ensure to properly configure AWS services to avoid potential issues during data processing.
- For assistance, refer to AWS documentation and tutorials related to Glue, Athena, and QuickSight.


