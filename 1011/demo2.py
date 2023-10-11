# Full Scanning

import boto3

dynamodb = boto3.resource('dynamodb',
                          region_name='ap-northeast-2',
                          aws_access_key_id='액세스키',
                          aws_secret_access_key='시크릿키')
table = dynamodb.Table('Movies')

results = table.scan()
# print(type(results)) # dict
# print(results)
# print(results.keys()) # 'Items', 'Count', 'ScannedCount', 'ResponseMetadata'
# print(results['Count'], results['ScannedCount'])

# items = results['Items']
for i in range(results['Count']) :
#     # print(items[i])
    print(results['Items'][i])