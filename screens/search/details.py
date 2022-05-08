#!/usr/bin/env python

import cgitb
import cgi
import MySQLdb
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

head = '''
    <html>
    <head>
        <link rel="stylesheet" href="search.css">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
        <div>
'''

print(head)


param = cgi.FieldStorage()

for key in param.keys():
    id = param.getvalue(key)


cursor.execute("select * from Report where Person_Has_ID = '{}'".format(id))
data = cursor.fetchall()
email = data[0][1]
status = data[0][0]
printemail = '''
    <p class="inline">Email:</p>
        <pclass="inline">{}</p>
        <p></p>
    <p class="inline">Status:</p>
        <p class="inline">{}</p>
    
    '''.format(email, status)

cursor.execute("select * from Item where Item_ID = '{}'".format(id))
data = cursor.fetchall()
cat = data[0][1]

printItem = '''
    <p class="inline">Category:</p>
        <p class="inline">{}</p>
        <p></p>
    <p class="inline">Color:</p>
        <p class="inline">{}</p>
         <p></p>
    <p class="inline">Size:</p>
        <p class="inline">{}</p>
    <hr style="width:100%;text-align:left;margin-left:0">
    '''.format(data[0][1], data[0][2], data[0][3])

print(printItem)

if (status == 'lost'):
    cursor.execute("select * from Lost where Lost_Item_ID = '{}'".format(id))
    data = cursor.fetchall()
    printLost = '''
    <p class="inline">Lost Date:</p>
        <p class="inline">{}</p>
        <p></p>
    <p class="inline">Last Seen:</p>
        <p class="inline">{}</p>
    <hr style="width:100%;text-align:left;margin-left:0">
    '''.format(data[0][1], data[0][2])
    print(printLost)
else:
    cursor.execute("select * from Found where Found_Item_ID = '{}'".format(id))
    data = cursor.fetchall()
    printFound = '''
    <p class="inline">Found Date:</p>
        <p>{}</p>
        <p></p>
    <p class="inline">Found Location:</p>
        <p>{}</p>
        <p></p>
    <p class="inline"><span id="imagename">Image</span></p>
        <img src = '{}' width = '200' height = '200'><br>
        
    '''.format(data[0][2], data[0][1], data[0][3])
    print(printFound)
    
if (cat == 'Keys'):
    cursor.execute("select * from `Keys` where Keys_Item_ITEM_ID = '{}'".format(id))
    data = cursor.fetchall()
    printFound = '''
    <p class="inline">Room number:</p>
        <p>{}</p>
        <p></p>
    <p class="inline">College:</p>
        <p>{}</p>
        <p></p>
    <p class="inline">Attached Item:</p>
        <p>{}</p>
    <hr style="width:100%;text-align:left;margin-left:0">
        
    '''.format(data[0][0], data[0][1], data[0][1])
    print(printFound)

elif (cat == 'Earphones'):
    cursor.execute("select * from Earphone where Earphones_Item_ITEM_ID = '{}'".format(id))
    data = cursor.fetchall()
    printFound = '''
    <p class="inline">Brand:</p>
        <p>{}</p>
        <p></p>
    <hr style="width:100%;text-align:left;margin-left:0">
    '''.format(data[0][0])
    print(printFound)

else:
    cursor.execute("select * from Campus_Card where CampusCard_Item_ITEM_ID = '{}'".format(id))
    data = cursor.fetchall()
    printFound = '''
    <p class="inline">Matriculation Number:</p>
        <p>{}</p>
        <p></p>
    <p class="inline">Name:</p>
        <p>{}</p>     
        <p></p>
    <hr style="width:100%;text-align:left;margin-left:0">
    '''.format(data[0][0], data[0][1])
    print(printFound)
