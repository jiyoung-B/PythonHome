import boto3

resource = boto3.resource("dynamodb",
                          region_name='ap-northeast-2',
                          aws_access_key_id='액세스키',
                          aws_secret_access_key='시크릿키')
client = boto3.client('dynamodb')
# print(resource)
# client.list_tables(); # 처음에는 테이블을 만든 적이 없으니 가져올 것이 없다.                        
# print(client.list_tables()) # dynamoDB 테이블 생성 후 다시 print 실행하면 json으로 반환.


table = client.describe_table(
    TableName = 'lab-movie'
)
print(table)

table = resource.Table('lab-movie')
item = {
    'Code' : '1978080',
    'Name' : 'Star Wars',
    'Genre' : 'SF',
    'Date' : '1978-04-12',
    'Director' : 'George Lucas',
    'Actor' : '마크 해밀, 캐리 피셔, 해리슨 포드, 알렉 기네'
}
table.put_item(Item=item)