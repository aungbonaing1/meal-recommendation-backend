from utility.dynamodb import client

def create_areas_table():
    table_name = 'areas'

    dynamodb = client()
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'strArea',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'strArea',
                'AttributeType': 'S'
            }
        ],
        BillingMode='PAY_PER_REQUEST',
    )
    print(table_name + ' is created successfully!')