import json
import requests
import boto3


def lambda_handler(event, context):
    def get_secret_value(secret_id):
        secrets_manager = boto3.client("secretsmanager")
        response = secrets_manager.get_secret_value(SecretId=secret_id)
        secret_value = json.loads(response["SecretString"])
        api_key = secret_value.get("MyAPIKey")
        return api_key

    secret_id = "MyAPIKey1"
    api_key = get_secret_value(secret_id)

    topic = "University"
    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}"

    # Set up DynamoDB client
    dynamodb = boto3.resource("dynamodb")
    table_name = "DATA_SOURCE_1"
    table = dynamodb.Table(table_name)

    try:
        # Send GET request to the News API
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Retrieve the JSON response
            data = response.json()

            # Iterate over each item in the response
            for item in data.get("articles", []):
                author = item.get("author")
                if author is None:
                    # Skip items without an "author" attribute
                    continue

                # Store the item in DynamoDB
                table.put_item(Item=item)

            return {
                "statusCode": 200,
                "body": "Data retrieved and stored in DynamoDB successfully",
            }
        else:
            # Handle the API response error
            return {
                "statusCode": response.status_code,
                "body": "Failed to retrieve data from the News API",
            }
    except Exception as e:
        # Handle any exceptions that occurred during the API request
        return {"statusCode": 500, "body": f"An error occurred: {str(e)}"}


## Getting API-KEY from secert manager
## Retreiving Data from API
## Storing in Dynamo DB
