import boto3

dynamodb = boto3.resource('dynamodb',
                          region_name='ap-northeast-2',
                          aws_access_key_id='액세스키',
                          aws_secret_access_key='시크릿키')
table = dynamodb.Table('Movies')
item = {
    'Code' : '1978080',
    'Name' : 'Star Wars',
    'Genre' : 'SF',
    'Date' : '1978-04-12',
    'Director' : 'George Lucas',
    'Actor' : '마크 해밀, 캐리 피셔, 해리슨 포드, 알렉 기네'
}
table.put_item(Item=item)

item = {
    'Code' : '20050112',
    'Name' : 'Batman Begins',
    'Time' : 134,
    'Genre' : '범죄, 액션, 퍈타지',
    'Date' : '2005--06-24',
    'Director' : '크리스토퍼 놀란',
    'Actor' : '리암 니슨, 크리스찬 베일, 마이클 케인'
}
table.put_item(Item=item)

