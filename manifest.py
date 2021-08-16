import boto3 
import yaml 
import logging 

logger = logging.getLogger()
logger.setLevel(logging.INFO)

client = boto3.client('cloudformation', region_name='us-east-1')

class CloudFormationStack:
    def __init__(self, json):
        self.client = client 
        self.stack_name = json["StackName"]
        self.template_file = json["TemplateFile"]
        self.parameters = json["Parameters"]
        self.capabilties = json["Capabilities"]
        self.region = json["Region"]
        self.tags = json["Tags"] if json["Tags"] else []

    def get_tags(self):
        self.tags.extend([{
            'DEPLOY_THROUGH': 'AZURE_DEVOPS'
        }])

    def deploy(self):
        try:
            response = client.describe_stacks(StackName=self.stack_name)
        except Exception as e:
            logging.info(f'${self.stack_name} does not exist')
            logging.warn(e)

            response = client.create_stack(
                            StackName=self.stack_name,
                            TemplateBody=self.template_file,
                            Parameters=self.parameters,
                            Capabilities=self.capabilties,
                            Tags=self.tags
                        )
            logging.info(response["StackId"])
        except Exception as e:
            logging.error(e)
        

if __name__ == "__main__":
    with open('manifest.yaml') as f:
        stacks = yaml.safe_load(f)
        print(stacks)
        for stack in stacks["Stacks"]:
            cfn = CloudFormationStack(stack)
            cfn.deploy()