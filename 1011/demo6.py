import boto3, dynamodbinfo

table = dynamodbinfo.dynamodb.Table('Movies')
table.delete() # 삭제 방지 옵션으로 바로 안지워짐.