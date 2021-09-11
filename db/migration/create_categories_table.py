from utility.dynamodb import client

def create_categories_table():
    table_name = 'categories'

    dynamodb = client()
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'strCategory',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'strCategory',
                'AttributeType': 'S'
            }
        ],
        BillingMode='PAY_PER_REQUEST',
    )
    print(table_name + ' is created successfully!')