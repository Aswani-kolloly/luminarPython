import mysql.connector
db=mysql.connector.connect(host='localhost',
           user='root',
           password='Password@123',
           auth_plugin='mysql_native_password',
           database='pythondecember')
cursor=db.cursor()

sql="create table movies( id int,name varchar(30),year varchar(20),rating int)"
cursor.execute(sql)
print("Table 'movies' created")
db.close()
