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
    database='group6',
    auth_plugin='mysql_native_password'
)
cursor = mydb.cursor()

form = cgi.FieldStorage()

count = 0
def showLostData(data):
    global count
    for i in data:
        cursor.execute("select * from Item where ITEM_ID = {}".format(i[0]))
        id = cursor.fetchall()
        div = '''
                <div class ='item'>
                <label class="inline">Category:</label>
                <p class="inline">{}</p><br>
                <label class="inline">Lost Date:</label>
                <p class="inline">{}</p>
                <p>
                </p>
                <label class="inline">Last Seen:</label>
                <p class="inline">{}</p>
                <a class="detail" href ='./details.py?id= {}'>More details</a>
                    <hr style="width:100%;text-align:left;margin-left:0">
                </div>
                <br>
            '''.format(id[0][1],i[1], i[2],i[0])
        print(div)
        count+=1
def showFoundData(data):
    global count
    for i in data:
        cursor.execute("select * from Item where ITEM_ID = {}".format(i[0]))
        id = cursor.fetchall()
        div = '''
                <div class ='item'>
                <label class="inline">Category:</label>
                <p class="inline">{}</p><br>
                <label class="inline">Found Date:</label>
                <p class="inline">{}</p>
                <p>
                </p>
                <label class="inline">Found Location:</label>
                <p class="inline">{}</p>
                <a class="detail" href ='./details.py?id= {}'>More details</a>
                    <hr style="width:100%;text-align:left;margin-left:0">
                </div>
                <br>
            '''.format(id[0][1],i[2], i[1],i[0])
        print(div)
        count+=1

head = '''
    <html>
    <head>
        <link rel="stylesheet" href="search.css">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
'''

print(head)
place = form.getvalue('place')

cursor.execute("select * from Lost where Last_Seen = '{}'".format(place))
data = cursor.fetchall()
showLostData(data)

cursor.execute("select * from Found where Found_Location = '{}'".format(place))
data = cursor.fetchall()

showFoundData(data)

if (count == 0):
    print("<h3>No Result</h3>")