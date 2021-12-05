#from flask import Flask
import mysql.connector
from datetime import datetime

#app = Flask(__name__)

usertype = "vendor"
vendorid = input("enter vendor id: ")

######################################################

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysqlpassword",
    database = "challa"
)

now = datetime.now()

sql_item_listing_statement = "SELECT*FROM items WHERE listedby = %s ORDER BY listedon;"
sql_item_value = (vendorid)


mycursor = mydb.cursor()
mycursor.execute(sql_item_listing_statement, sql_item_value)
records = mycursor.fetchall()

print("items by ", vendorid, "\n")

for row in records:
    print(row[0], row[1])


#app.run(host = "127.0.0.1", port = 5000, debug = True)
