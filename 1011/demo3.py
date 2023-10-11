# Index Scanning
import boto3, dynamodbinfo

# dynamodbinfo Movies와 이미 연결된 테이블
table = dynamodbinfo.dynamodb.Table('Movies') 

#1. Using get_item
result = table.get_item(
    Key={
        'Code' : '20050112',
        'Name' : 'Batman Begins'
    }
)

# print(type(result)) # dict
# print(result.keys())

print(result['Item'])
