#from flask import Flask
import mysql.connector
from datetime import datetime

#app = Flask(__name__)

item_name = input("enter item name: ")
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

mycursor = mydb.cursor()
mycursor.execute(sql_item_listing_statement, sql_item_value)

sql_item_listing_statement = "INSERT INTO items (i_name, listedon, listedby)VALUE (%s, %s, %s);"
sql_item_value = (item_name, now, vendorid)

mydb.commit()

print("item ", item_name, "added by ", vendorid)

#app.run(host = "127.0.0.1", port = 5000, debug = True)
