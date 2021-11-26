from flask import Flask, render_template, request
from getpass import getpass
import mysql.connector
from mysql.connector import connect, Error


class Mysqlhandler:

    def login(self, uname, pwd, num):
       
        ######################################################

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=getpass("Enter password: "),
            database = "challa"
        )

        enteredname = uname
        enteredpass = pwd

        if num == 1:
            usertype = "buyer"         #either_buyer_or_vender

        elif num == 2:
            usertype = "vendor"

        userid = -1
        userexists = 0
        passmatch = 0
        rowadd = -1

        mycursor = mydb.cursor(buffered=True)
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
            return 1

        elif(userexists == 0 or passmatch == 0):
            return 0

    
    
    def signup(self, uname, pwd, num):
        
        ################################################

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=getpass("Enter password: "),
            database = "challa"
        )

        enteredname = uname
        enteredpass = pwd

        if num == 1:
            usertype = "buyer"         #either_buyer_or_vender

        elif num == 2:
            usertype = "vendor"

        userid = -1
        userexists = 0
        passmatch = 0
        signupstat = 0

        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("SELECT * FROM " + usertype + "")
        mydb.commit()
        records = mycursor.fetchall()

        for i in range(0, mycursor.rowcount): #checks_if_username_is_taken
            if(enteredname == records[i][0]):
                userexists = 1
                break

        if(userexists != 1): #if_username_is_not_used

            mycursor = mydb.cursor(buffered=True)
            query = "INSERT INTO "+ usertype + "(username, pass)"
            mycursor.execute(query + "VALUES (%s, %s)", (enteredname, enteredpass))
            mydb.commit()

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
                return 1

        else:
            return 0

    
