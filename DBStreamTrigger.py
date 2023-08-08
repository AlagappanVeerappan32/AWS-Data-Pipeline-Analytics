import json
import boto3


def lambda_handler(event, context):
    dynamodb = boto3.client("dynamodb")
    stepfunctions = boto3.client("stepfunctions")

    # Check if the Step Function is already running
    response = stepfunctions.list_executions(
        stateMachineArn="arn:aws:states:ca-central-1:569029980056:stateMachine:MyStateMachine-DB",
        statusFilter="RUNNING",
    )

    if response["executions"]:
        # Step Function is already running, do not trigger again
        print("Step Function is already running")
        return

    for record in event["Records"]:
        if record["eventName"] in ["INSERT", "MODIFY"]:
            response = stepfunctions.start_execution(
                stateMachineArn="arn:aws:states:ca-central-1:569029980056:stateMachine:MyStateMachine-DB",
                input="{}",  # Empty input
            )
            print(response)

    return "Successfully processed {} records.".format(len(event["Records"]))
