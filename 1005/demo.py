import pymysql

# 1. Connect
conn, cursor = None, None
try :
    conn = pymysql.connect(host='3.35.175.13', port=3306,
                       user='root', password='pythonmysql')
    print(conn)
    
# 2. cursor
    cursor = conn.cursor()
# 3. SQL Statement
    sql = "SELECT NOW()"
    cursor.execute(sql)
    
# 4. fetch
    result = cursor.fetchone()
    print(result)
except Exception as err:
    print(err)

# 5. close
finally :
    cursor.close()
    conn.close()