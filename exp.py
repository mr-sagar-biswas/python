
import mysql.connector

mydb= mysql.connector.connect(host="localhost",user="sagar",passwd="Havingfun@7407")
mycursor= mydb.cursor()
mycursor.execute("show databases")
for i in mycursor:
    print(i)