import boto3

region = 'us-east-1'
instances = ['i-0d7b0fd3871ef1261']

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: %s', str(instances))