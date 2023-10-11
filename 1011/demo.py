import boto3

dynamodb = boto3.resource('dynamodb',
                          region_name='ap-northeast-2',
                          aws_access_key_id='액세스키',
                          aws_secret_access_key='시크릿키')
client = boto3.client('dynamodb')
list_tables = client.list_tables() #dict
# print(list_tables.keys())
# print(len(list_tables['TableNames']))
response = client.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'Code',
            'AttributeType': 'S'
        },
         {
            'AttributeName': 'Name',
            'AttributeType': 'S'
        }
    ],
    TableName='Movies',
    KeySchema=[
        {
            'AttributeName': 'Code',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'Name',
            'KeyType': 'RANGE'
        }
    ],
    Tags=[
        {
            'Key': 'Name',
            'Value': 'Movies'
        },
    ],
    TableClass='STANDARD',
    DeletionProtectionEnabled=True,
    BillingMode='PROVISIONED',
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    },
)
