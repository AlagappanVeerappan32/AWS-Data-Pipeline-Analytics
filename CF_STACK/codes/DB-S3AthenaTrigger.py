import boto3


def lambda_handler(event, context):
    print(event)

    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = event["Records"][0]["s3"]["object"]["key"]

    print(bucket)
    print(key)
    
    SF_ARN = "arn:aws:states:us-east-1:637592602151:stateMachine:CF-Athena-DB-RESULT-STATE-MACHINE"

    if key.startswith("DB-data-source/"):
        stepfunctions = boto3.client("stepfunctions")
        
        response = stepfunctions.list_executions(
            stateMachineArn= SF_ARN,
            statusFilter="RUNNING",
        )
        if response["executions"]:
            print("Step Function is already running")
            return

        response = stepfunctions.start_execution(
            stateMachineArn= SF_ARN
        )
        print(response)

    return "Step Function execution triggered."
