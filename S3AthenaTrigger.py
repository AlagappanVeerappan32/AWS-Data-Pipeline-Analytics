import boto3


def lambda_handler(event, context):
    print(event)

    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = event["Records"][0]["s3"]["object"]["key"]

    print(bucket)
    print(key)

    if key.startswith("s3-target-source/"):
        stepfunctions = boto3.client("stepfunctions")

        response = stepfunctions.list_executions(
            stateMachineArn="arn:aws:states:ca-central-1:569029980056:stateMachine:MyStateMachine",
            statusFilter="RUNNING",
        )
        if response["executions"]:
            print("Step Function is already running")
            return

        response = stepfunctions.start_execution(
            stateMachineArn="arn:aws:states:ca-central-1:569029980056:stateMachine:MyStateMachine"
        )
        print(response)

    return "Step Function execution triggered."
