import boto3
from utility.config import get_aws_profile

def session(profile = None):
    if profile == None:
        return boto3
    session = boto3.Session(profile_name=profile)
    return session

def aws_session():
    aws_profile = get_aws_profile()
    return session(aws_profile)

def client():
    session = aws_session()
    return session.client(service_name="dynamodb")

def scan(table_name, process, input_parameters = {}):
    dynamodb = client()
    paginator = dynamodb.get_paginator('scan')
    parameters = {}
    parameters['TableName'] = table_name
    parameters['PaginationConfig'] = {'PageSize': 100}
    parameters = {**parameters, **input_parameters}

    results = []
    for page in paginator.paginate(**parameters):
        for item in page['Items']:
            result = process(item)
            if result:
                results.append(result)
    return results

def batch_itr(items, process):
    for start in range(0, len(items), 25):
        process(items[start: start+25])

def write_batch(table_name, items):
    def write(records):
        dynamodb = client()
        response = dynamodb.batch_write_item(
            RequestItems={table_name: records}
        )
    batch_itr(items, write)