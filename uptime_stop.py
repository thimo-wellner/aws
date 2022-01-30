
import requests
from datetime import datetime
import getopt, sys
import urllib3
import boto3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

time = 10*60*60

client = boto3.client('sagemaker')
uptime = client.describe_notebook_instance(
  NotebookInstanceName=get_notebook_name()
  )['LastModifiedTime']
starting_time = datetime.strptime(uptime,"%Y-%m-%dT%H:%M:%S.%fz")
    if (datetime.now() - starting_time).total_seconds() > time:
      idle = True
      
if idle:
    print('Closing idle notebook')
    client = boto3.client('sagemaker')
    client.stop_notebook_instance(
        NotebookInstanceName=get_notebook_name()
    )
