#!/usr/bin/env python

import cgitb
import cgi
import sys
import os
import smtplib
import mysql.connector




mydb = mysql.connector.connect(
host="localhost",
user="root",
password="root",
database = 'group6',
auth_plugin='mysql_native_password'
)

cursor = mydb.cursor()


form = cgi.FieldStorage()

for i in form.keys():

    hash = form.getvalue(i)

query = ''' 
            select * from Moderator where Hash = '{}'
        '''.format(hash)

cursor.execute(query)
data = cursor.fetchall()



if (len(data) == 1):
    print("Content-Type: text/html;")
    print("Status: 302 Moved")
    print("Location: http://192.168.117.166/html/admin.py?user={}\r\n".format(hash))

else:
    print("Content-Type: text/html;charset=utf-8\n\n")
    print('you are not admin')
    print(hash)