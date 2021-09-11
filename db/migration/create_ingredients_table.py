from utility.dynamodb import client

def create_ingredients_table():
    table_name = 'ingredients'

    dynamodb = client()
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'idIngredient',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'strIngredient',
                'KeyType': 'RANGE',
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'idIngredient',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'strIngredient',
                'AttributeType': 'S'
            }
        ],
        BillingMode='PAY_PER_REQUEST',
    )
    print(table_name + ' is created successfully!')