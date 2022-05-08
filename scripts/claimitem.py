#!/usr/bin/env python

import cgitb
import queries
import cgi
import mysql.connector
import MySQLdb
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
itemId = form.getvalue('id')
user = form.getvalue('user')
date = form.getvalue('date')

try:
    claim = (user, itemId, date)

    cursor.execute(queries.SQL_INSERT_CLAIM, claim)
    mydb.commit()

    print('<p>success</p>')

except (MySQLdb.Error, MySQLdb.Warning) as e:
    print('{}</p>'.format(e))

