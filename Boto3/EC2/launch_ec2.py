import boto3

client = boto3.client('ec2')
resp = client.run_instances(ImageId='ami-04a0ae173da5807d3',
                            InstanceType='t2.micro',
                            MinCount=1,
                            MaxCount=1)

#for instance in resp['Instances']:
#    print(instance['InstanceId'])

instance_id = resp['Instances'][0]['InstanceId']
print(instance_id)