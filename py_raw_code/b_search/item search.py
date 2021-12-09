#from flask import Flask
import mysql.connector
from datetime import datetime

#app = Flask(__name__)

usertype = "buyer"
search_query = input("enter search query: ")

######################################################


def convert(lst):
    return (lst[0].split())


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysqlpassword",
    database="challa"
)

mycursor = mydb.cursor()

split = convert(search_query)
sql_search = "SELECT*FROM items WHERE"

for x in range(len(split)):
    if(x == 0):
        sql_search = sql_search + " i_name LIKE %" + split[x] + "%"
    else:
        sql_search = sql_search + " OR i_name LIKE %" + split[x] + "%"

sql_search = sql_search + ";"


mycursor.execute(sql_search)
records = mycursor.fetchall()


print("search results for ", search_query, ":\n")
print(records)


#app.run(host = "127.0.0.1", port = 5000, debug = True)
