import mysql.connector
db=mysql.connector.connect(host='localhost',
           user='root',
           password='Password@123',
           auth_plugin='mysql_native_password',
           database='pythondecember')
cursor=db.cursor()
try:
    sql="insert into movies values( 101,'over the moon','2016',3.5)"
    cursor.execute(sql)
    db.commit()
except Exception as e:
    print(e.args)
    db.rollback()
db.close()
