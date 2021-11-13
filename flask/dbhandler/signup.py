from flask import Flask, render_template, request
from getpass import getpass
import mysql.connector
from mysql.connector import connect, Error
#app = Flask(__name__)

class Mysqlhandler2:

    def signup(self, uname, pwd):
        ################################################

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=getpass("Enter password: "),
            database = "challa"
        )

        enteredname = uname
        enteredpass = pwd

        usertype = "buyer"                       #either_buyer_or_vender

        userid = -1
        userexists = 0
        passmatch = 0
        signupstat = 0

        mycursor = mydb.cursor()
        query = "SELECT * FROM " + usertype + ""
        mycursor.execute(query)
        mydb.commit()
        records = mycursor.fetchall()

        for i in range(0, mycursor.rowcount): #checks_if_username_is_taken
            if(enteredname == records[i][0]):
                userexists = 1
                break

        if(userexists != 1): #if_username_is_available

            sql_signup_statement = "INSERT INTO buyer (username, pass) VALUES (%s, %s)"
            sql_value = (enteredname, enteredpass)

            mycursor = mydb.cursor()
            mycursor.execute(sql_signup_statement, sql_value)
            mydb.commit()
            records = mycursor.fetchall()

            signupstat = 1

            rowadd = -1

        #logging_in_after_signing_up

            mycursor.execute("SELECT * FROM " + usertype + "")
            mydb.commit()
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
                print("\nSigned up and auto-Logged in as:", enteredname)

        else:
            print("ERROR: USERNAME TAKEN")
