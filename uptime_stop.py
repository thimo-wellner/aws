
import requests
from datetime import datetime
import getopt, sys
import urllib3
import boto3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

hours = 10
time = hours*60*60
idle = False

def get_notebook_name():
    log_path = '/opt/ml/metadata/resource-metadata.json'
    with open(log_path, 'r') as logs:
        _logs = json.load(logs)
    return _logs['ResourceName']

client = boto3.client('sagemaker')
uptime = client.describe_notebook_instance(
    NotebookInstanceName=get_notebook_name()
    )['LastModifiedTime']
starting_time = datetime.strptime(uptime.strftime("%Y-%m-%dT%H:%M:%S.%fz"),"%Y-%m-%dT%H:%M:%S.%fz")
if (datetime.now() - starting_time).total_seconds() > time:
    idle = True
      
if idle:
    print(f'Closing notebook after {hours} hours of uptime!')
    client = boto3.client('sagemaker')
    client.stop_notebook_instance(
        NotebookInstanceName=get_notebook_name())
else:
    print("Not yet time to close")
