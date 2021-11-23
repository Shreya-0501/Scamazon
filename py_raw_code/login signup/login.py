#from flask import Flask
import mysql.connector

#app = Flask(__name__)

enteredname = input("enter username: ")
enteredpass = input("enter password: ")
usertype = "buyer" #either_buyer_or_vender

######################################################

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysqlpassword",
    database = "challa"
)


userid = -1
userexists = 0
passmatch = 0
rowadd = -1

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM " + usertype + "")
records = mycursor.fetchall()

for i in range(0, mycursor.rowcount):
    if(enteredname == records[i][0]):
        userexists = 1
        rowadd = i
        break

if(userexists):
    if(enteredpass == records[rowadd][1]):
        passmatch = 1
        userid = records[i][2]

if(userexists == 1 and passmatch == 1):
    print("\nLogged in as:", enteredname)

elif(userexists == 0 or passmatch == 0):
    print("\nINVALID CREDENTIALS")

#app.run(host = "127.0.0.1", port = 5000, debug = True)