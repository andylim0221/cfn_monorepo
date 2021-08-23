import boto3 
import yaml 
import logging 
import time 

logger = logging.getLogger()
logger.setLevel(logging.INFO)

client = boto3.client('cloudformation', region_name='us-east-1')

CAPABILITIES = ['CAPABILITY_IAM','CAPABILITY_NAMED_IAM','CAPABILITY_AUTO_EXPAND']

class CloudFormationStack:
    def __init__(self, json):

        self.client = client 
        self.stack_name = json["StackName"]
        self.template_file = json["TemplateFile"]
        self.parameters = json["Parameters"]
        self.capabilties = json["Capabilities"]
        self.region = json["Region"]
        self.tags = json["Tags"] if json["Tags"] else None 

    def get_stack(self, stack_name):
        try: 
            response = self.client.decribe_stacks(StackName=stack_name)
        except Exception as e:
            logging.error(e)
            return None
        else:
            return response["Stacks"][0]

    def validate_template(self, **kwargs):
        try:
            self.client.validate_template(**kwargs)
        except Exception as e:
            logging.error(e)

    def run(self):
        self.validate_template(self.template_file)

if __name__ == "__main__":
    with open('manifest.yaml') as f:
        stacks = yaml.safe_load(f)
        # print(stacks)
        for stack in stacks["Stacks"]:
            cfn = CloudFormationStack(stack)
            cfn.run()