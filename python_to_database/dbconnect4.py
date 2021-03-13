import mysql.connector
db=mysql.connector.connect(host='localhost',
           user='root',
           password='Password@123',
           auth_plugin='mysql_native_password',
           database='pythondecember')
cursor=db.cursor()
sql="select *from movies"
cursor.execute(sql)
movie=cursor.fetchall()
for m in movie:
    print(m)
#generators
yield movie
movie=get_data()
print(movie.__next__())