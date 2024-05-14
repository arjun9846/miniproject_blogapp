import mysql.connector
mycon=mysql.connector.connect(host="localhost",user="root",password="root")
mycur=mycon.cursor()
mycur.execute("CREATE DATABASE blog")