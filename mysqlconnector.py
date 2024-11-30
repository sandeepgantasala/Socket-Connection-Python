import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="Bobby@123",database="sys")

print("Connection Successful")
mycursor1=mydb.cursor()
mycursor=mydb.cursor()

mycursor.execute("select * from sys_config")
for i in mycursor:
    print(i)

# mycursor1.execute("show databases")
# for i in mycursor1:
#     print(i)