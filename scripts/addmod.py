#!/usr/bin/env python

import cgitb
import queries
import MySQLdb
import cgi
import mysql.connector
cgitb.enable()



print("Content-Type: text/html;charset=utf-8\n\n")

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="root",
database = 'group6',
auth_plugin='mysql_native_password'
)

cursor = mydb.cursor()

form = cgi.FieldStorage()

email = form.getvalue('email')
 
username = email.split('@')[0]

x = dict()
x['Username'] = username
try:
    queries.website_input_moderator(cursor,x)


#print(cursor)
    mydb.commit()
    print('<p>success</p>')

except (MySQLdb.Error, MySQLdb.Warning) as e:
	print('<p>{}</p>'.format(e))