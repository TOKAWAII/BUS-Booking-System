import MySQL.connector
mydb=mysql.connector.connect(host="localhost",user='root',password='@Mohitmishra1')
print (mydb.connection_id)
