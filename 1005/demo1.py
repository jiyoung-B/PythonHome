import pymysql

host = 'ec2-3-35-175-13.ap-northeast-2.compute.amazonaws.com'
port = 3306
user = 'root'
password = 'pythonmysql'
database = 'mycompany'
conn = pymysql.connect(port=port, user=user,
                       host=host, password=password, database=database)

cursor = conn.cursor()
sql = " SELECT EMPNO, ENAME, JOB, SAL, DEPTNO FROM EMP WHERE DEPTNO = 20"
cursor.execute(sql)
results = cursor.fetchall()
for emp in results :
    print(type(emp))
    print(emp[1], emp[3], sep=',\t')

cursor.close()
conn.close()