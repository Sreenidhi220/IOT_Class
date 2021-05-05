import pymysql

conn =pymysql.connect(database="db1",user="Sreenidhi",password="12345",host="localhost")
cur=conn.cursor()

#create database
cur.execute("CREATE TABLE users(id int primary, name varchar, age int, gender varchar, address varchar);")

#to store user data

name = "Sreenidhi"
age = 28
gender = "M"
address = "KERALA"

data={'name':name,'age':age,'gender':gender,'address':address}
print(data)

# Saving data to DB
cur.execute("INSERT INTO users (name,age,gender,address) VALUES (%(name)s,%(age)s,%(gender)s,%(address)s);",data)
conn.commit()
print("saved to db")

#reading data from DB
cur.execute("SELECT * FROM users;")
#get one row
data1=cur.fetchone()
#get all rows
data2=cur.fetchall()

print(data1)
print(data2)


