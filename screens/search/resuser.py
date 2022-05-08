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



head = '''
    <html>
    <head>
        <link rel="stylesheet" href="search.css">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
'''

print(head)

form = cgi.FieldStorage()

query = '''
    select * from Item join (select * from Report where `Person_email` = '{}') as per on per.Person_Has_ID = ITEM_ID;
    '''.format(form.getvalue('email'))

cursor.execute(query)
data = cursor.fetchall()

for i in data:
    div = '''
            <div class ='users'>
                <lable>Email:</label>
                <p>{}</p>
                <lable>Category:</label>
                <p>{}</p>
                <label>Status:</label>
                <p>{}</p>

                <a style= 'float:right' href = './details.py?id = {}'>More details</a>
                
               

            </div>
            <br>
        '''.format(i[5], i[1], i[4],i[0])

    print(div)

 
    # if (i[4] == 'lost'):
    #     cursor.execute('select * from `Keys` where Keys_Item_ITEM_ID = {}'.format(i[1]))
    #     keys = cursor.fetchall()

    #     div = '''
    #         <div>
    #             <lable>Email:</label>
    #             <p>{}</p>
    #             <lable>Category:</label>
    #             <p>{}</p>
               

    #         </div>
    #     '''.format(i[0], i[4])
    #     print(div)
    # if (i[4] == 'Earphones'):
    #     cursor.execute('select * from Earphone where Earphones_Item_ITEM_ID = {}'.format(i[1]))
    #     keys = cursor.fetchall()
    #     div = '''
    #         <div>
    #             <lable>Email:</label>
    #             <p>{}</p>
    #             <lable>Category:</label>
    #             <p>{}</p>

    #          </div>
    #     '''.format(i[0], i[4])
    #     print(div)
    # if (i[4] == 'CampusCard'):
    #     cursor.execute('select * from Campus_Card where CampusCard_Item_ITEM_ID = {}'.format(i[1]))
    #     keys = cursor.fetchall()
    #     div = '''
    #         <div>
    #             <lable>Email:</label>
    #             <p>{}</p>
    #             <lable>Category:</label>
    #             <p>{}</p>
                

    #         </div>
    #     '''.format(i[0], i[4])
    #     print(div)

footer = '''
        </body>
    </html>
'''

print(footer)
