from utility.dynamodb import client

def create_meals_table():
    table_name = 'meals'

    dynamodb = client()
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'idMeal',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'strMeal',
                'KeyType': 'RANGE',
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'idMeal',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'strMeal',
                'AttributeType': 'S'
            }
        ],
        BillingMode='PAY_PER_REQUEST',
    )
    print(table_name + ' is created successfully!')