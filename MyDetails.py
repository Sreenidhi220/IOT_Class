import pymysql

conn =pymysql.connect(database="db1",user="Sreenidhi",password="12345",host="localhost")
cur=conn.cursor()

#create database
cur.execute("CREATE TABLE Person ( PersonID int,name varchar(255),age int, gender varchar(255),address varchar(255) );")
#to store user data

name = "Sreenidhi"
age = 28
gender = "M"
address = "KERALA"

data={'name':name,'age':age,'gender':gender,'address':address}
print(data)

# Saving data to DB
cur.execute("INSERT INTO Person (name,age,gender,address) VALUES (%(name)s,%(age)s,%(gender)s,%(address)s);",data)
conn.commit()
print("saved to db")

#reading data from DB
cur.execute("SELECT * FROM Person;")
#get one row
data1=cur.fetchone()
#get all rows
data2=cur.fetchall()

print(data1)
print(data2)


