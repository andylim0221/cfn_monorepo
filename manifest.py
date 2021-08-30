import boto3
import yaml
import logging
import time
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

client = boto3.client("cloudformation", region_name="us-east-1")

CAPABILITIES = ["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"]

"""
1. collect config from each stack
2. create stack/update stack/delete stack
"""


def collect_stack_config(stack):
    response = {}

    parameters = []
    if "Parameters" in stack:
        for parameter in stack["Parameters"]:
            for key, value in parameter.items():
                parameters.append({"ParameterKey": key, "ParameterValue": str(value)})
    response["Parameters"] = parameters

    response["EnableTerminationProtection"] = (
        stack["EnableTerminationProtection"]
        if "EnableTerminationProtection" in stack
        else False
    )

    tags = []
    if "Tags" in stack and stack["Tags"]:
        for key in stack["Tags"]:
            tags.append({"Key": key, "Value": stack["Tags"][key]})
    response["Tags"] = tags

    return response["Tags"]


def handle_stack(stack):
    stack_config = collect_stack_config(stack)
    try:
        response = client.describe_stacks(StackName=stack["StackName"])
    except Exception as e:
        logging.warning(
            f'Stack {stack["StackName"]} does not exist or invalid stack name'
        )
        response = client.create_stack(
            StackName=stack["StackName"],
            TemplateBody=stack["TemplateFile"],
            Parameters=stack_config["Parameters"],
            Capabilities=stack["Capabilities"],
            Tags=stack_config["Tags"],
            EnableTerminationProtection=stack_config["EnableTerminationProtection"],
        )
    else:
        if response["StackStatus"] in [
            "CREATE_COMPLETE",
            "UPDATE_COMPLETE",
            "UPDATE_ROLLBACK_COMPLETE",
        ]:
            if "Delete" in stack and stack["Delete"]:
                client.delete_stack(StackName=stack["StackName"])
            else:
                response = client.update_stack(
                    StackName=stack["StackName"],
                    TemplateBody=stack["TemplateFile"],
                    Parameters=stack_config["Parameters"],
                    Capabilities=stack["Capabilities"],
                    Tags=stack_config["Tags"],
                    EnableTerminationProtection=stack_config[
                        "EnableTerminationProtection"
                    ],
                )


if __name__ == "__main__":
    with open("manifest.yaml") as f:
        stacks = yaml.safe_load(f)
        for stack in stacks["Stacks"]:
            print(stack)
            handle_stack(stack)
