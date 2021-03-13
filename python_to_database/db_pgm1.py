import mysql.connector

#step2: est connection
db=mysql.connector.connect(host='localhost',user='root',password='Password@123',auth_plugin='mysql_native_password')

#step3: create cursor obj
cursor=db.cursor()

sql="select version()"
cursor.execute(sql)
data=cursor.fetchone()
print(data)
db.close()
