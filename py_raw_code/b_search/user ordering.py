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

sql_item_listing_statement = "INSERT INTO orders (ordered_id, o_date, ordered_by)VALUE (%s, %s, %s);"
sql_item_value = (item, now, buyer)

mycursor = mydb.cursor()
mycursor.execute(sql_item_listing_statement, sql_item_value)
mydb.commit()


#app.run(host = "127.0.0.1", port = 5000, debug = True)
