#!/usr/bin/env python

import cgitb
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



head = '''<html>
    <head>
        <link rel="stylesheet" href="../admin.css">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
        <div style="text-align: center;margin-top: 10%;">
            <form action="../../scripts/delitem.py" method="POST">
                <label class="label">Item Id:</label><br>
                <div style="display: inline">
                    <select name='id'>


                    '''
print(head)
cursor.execute("select * from Item")
items = cursor.fetchall()
for i in items:
    print("<option value = '{}'>{}</option>".format(i[0],i[0]))

body = '''
            </select>
    </div><br><br>

        <label class = 'label'>Moderator</label><br>
        <div>
        <select name ='mod'>
        '''
print(body)
cursor.execute('select * from Moderator')
people = cursor.fetchall()

for j in people:
    print('<option value = {}>{}</option>'.format(j[0],j[0]))

footer = '''
        </select>
        </div><br>
                <label class="label">Description:</label><br>
                <div style="display: inline">
                    <div ><textarea name='description' style="width: 25%; height: 15%;">

                    </textarea></div>
                </div>
                <input class="button" type="submit" value="Delete">
            </form>
        </div>
    </body>
</html>
'''
print(footer)
