import boto3 
import yaml 

client = boto3.client('cloudformation', region_name='us-east-1')

class CloudFormationStack:
    def __init__(self, json):
        self.stack_name = json["StackName"]
        self.template_file = json["TemplateFile"]
        self.parameters = json["Parameters"]

    def deploy(self):
        print(self.stack_name)

if __name__ == "__main__":
    with open('manifest.yaml') as f:
        stacks = yaml.safe_load(f)
        print(stacks)
        for stack in stacks["Stacks"]:
            cfn = CloudFormationStack(stack)
            cfn.deploy()