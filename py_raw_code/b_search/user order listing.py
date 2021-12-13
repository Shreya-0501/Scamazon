#from flask import Flask
import mysql.connector
from datetime import datetime

#app = Flask(__name__)

usertype = "buyer"
item = input("enter i_id")
buyer = input("enter buyerid")

######################################################


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysqlpassword",
    database="challa"
)

now = datetime.now()

sql_item_listing_statement = "SELECT*FROM orders WHERE ordered_by = %s ORDER BY o_date;"
sql_item_value = (buyer)

mycursor = mydb.cursor()
mycursor.execute(sql_item_listing_statement, sql_item_value)
records = mycursor.fetchall()

print("items by ", buyer, "\n")

for row in records:
    print(row[0], row[1])


#app.run(host = "127.0.0.1", port = 5000, debug = True)
