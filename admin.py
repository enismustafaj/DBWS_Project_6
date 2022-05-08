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


print("Content-Type: text/html;charset=utf-8\n\n")
#print(data)
if (len(data) == 1):

    html = '''
    <html>
        <head>
            <link rel="stylesheet" href="./screens/admin.css">
            <meta name="viewport" content="width=device-width, initial-scale=1">
        </head>
        <body>
            <ul class="navbar">
                <img src="./images/logo.png" width='150' height="150">
                <li><a href="./screens/admin/claimitem.py" target="frame">Claim Item</a></li>
            <li><a href="./screens/admin/delitem.py" target="frame">Delete Item</a></li>
                <li><a href="./screens/admin/repfound.html" target="frame">Report Found Item</a></li>
                <li><a href="./screens/admin/replost.html" target="frame">Report Lost Item</a></li>
                <li><a href="./screens/admin/addmod.html" target="frame">Add Moderator</a></li>
                <li><a href="./screens/admin/adduser.html" target="frame"> Add User</a></li>

            </ul>

            <iframe src="" name = 'frame' frameborder = '0' width="100%" height="80%" scrolling='yes'>

            </iframe>

            <script>

            </script>
            
        </body>
    </html>
    '''
    print(html)
else:
    print('No access')