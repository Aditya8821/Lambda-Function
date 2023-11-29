import boto3
import datetime

ec2 = boto3.client('ec2', region_name='us-east-1')

def lambda_handler(event, context):
    instance_id = 'i-0f9753a25fef8cdac'
    stop_instances(instance_id)

def stop_instances(instance_id):
    ec2.stop_instances(InstanceIds=[instance_id])
    print(f"Instance {instance_id} stopped at {datetime.datetime.now()}")
