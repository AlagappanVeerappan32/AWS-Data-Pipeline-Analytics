import json
import boto3


def lambda_handler(event, context):
    dynamodb = boto3.client("dynamodb")
    stepfunctions = boto3.client("stepfunctions")
    
    SF_ARN = "arn:aws:states:us-east-1:637592602151:stateMachine:CF-DB-SOURCE-STATE-MACHINE"

    # Check if the Step Function is already running
    response = stepfunctions.list_executions(
        stateMachineArn=SF_ARN,
        statusFilter="RUNNING",
    )

    if response["executions"]:
        # Step Function is already running, do not trigger again
        print("Step Function is already running")
        return

    for record in event["Records"]:
        if record["eventName"] in ["INSERT", "MODIFY"]:
            response = stepfunctions.start_execution(
                stateMachineArn=SF_ARN,
                input="{}",  # Empty input
            )
            print(response)

    return "Successfully processed {} records.".format(len(event["Records"]))
