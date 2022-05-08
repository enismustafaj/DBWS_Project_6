#!/usr/bin/env python
import cgitb
import cgi
import mysql.connector
cgitb.enable()


print("Content-Type: text/html;charset=utf-8\n\n")

mydb = mysql.connector.connect(
    host="localhost",
    user="user",
    password="user",
    database='group6',
    auth_plugin='mysql_native_password'
)
cursor = mydb.cursor()

form = cgi.FieldStorage()

head = '''
    <html>
    <head>
        <link rel="stylesheet" href="search.css">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
'''

print(head)

date = form.getvalue('time')

if (date == '1week'):
    query = '''
    select  `Person_email`, `Lost_Item_ID`, `Last_Seen`, `Lost_Date`, `Category`, `Color`, `Size` from Item join (select `Person_email`, `Lost_Item_ID`, `Last_Seen`, `Lost_Date` from Report 
    join `Lost` on `Person_Has_ID` = `Lost_Item_ID`) as rep on rep.Lost_Item_ID = Item.ITEM_ID where `Category` = '{}' and ROUND(DATEDIFF(now(), `Lost_Date`)/7, 0) <= 1 ;
    '''.format(form.getvalue('category'))

elif (date == '2weeks'):
    query = '''
    select  `Person_email`, `Lost_Item_ID`, `Last_Seen`, `Lost_Date`, `Category`, `Color`, `Size` from Item join (select `Person_email`, `Lost_Item_ID`, `Last_Seen`, `Lost_Date` from Report 
    join `Lost` on `Person_Has_ID` = `Lost_Item_ID`) as rep on rep.Lost_Item_ID = Item.ITEM_ID where `Category` = '{}' and ROUND(DATEDIFF(now(), `Lost_Date`)/7, 0) <= 2 ;
    '''.format(form.getvalue('category'))

elif (date == '1month'):
    query = '''
    select  `Person_email`, `Lost_Item_ID`, `Last_Seen`, `Lost_Date`, `Category`, `Color`, `Size` from Item join (select `Person_email`, `Lost_Item_ID`, `Last_Seen`, `Lost_Date` from Report 
    join `Lost` on `Person_Has_ID` = `Lost_Item_ID`) as rep on rep.Lost_Item_ID = Item.ITEM_ID where `Category` = '{}' and TIMESTAMPDIFF(MONTH, now(), `Lost_Date`) <=1 ;
    '''.format(form.getvalue('category'))

else:
    query = '''
    select  `Person_email`, `Lost_Item_ID`, `Last_Seen`, `Lost_Date`, `Category`, `Color`, `Size` from Item join (select `Person_email`, `Lost_Item_ID`, `Last_Seen`, `Lost_Date` from Report 
    join `Lost` on `Person_Has_ID` = `Lost_Item_ID`) as rep on rep.Lost_Item_ID = Item.ITEM_ID where `Category` = '{}' and TIMESTAMPDIFF(MONTH, now(), `Lost_Date`) <=2 ;
    '''.format(form.getvalue('category'))

# query = '''
#     select  `Person_email`, `Lost_Item_ID`, `Last_Seen`, `Lost_Date`, `Category`, `Color`, `Size` from Item join (select `Person_email`, `Lost_Item_ID`, `Last_Seen`, `Lost_Date` from Report
#     join `Lost` on `Person_Has_ID` = `Lost_Item_ID`) as rep on rep.Lost_Item_ID = Item.ITEM_ID where `Category` = '{}' ;
#     '''.format(form.getvalue('category'))

cursor.execute(query)
data = cursor.fetchall()

for i in data:

    if (i[4] == 'Keys'):
        cursor.execute(
            'select * from `Keys` where Keys_Item_ITEM_ID = {}'.format(i[1]))
        keys = cursor.fetchall()

        div = '''
            <div class ='users'>
            <label class="inline">Email:</label>
            <p class="inline">{}</p>
            <p>
            </p>
            <label class="inline">Item:</label>
            <p class="inline">{}</p>
                <a class="detail" href ='./details.py?id= {}'>More details</a>
                 <hr style="width:100%;text-align:left;margin-left:0">
             </div>
            <br>
        '''.format(i[0], i[4], keys[0][3])
        print(div)
    if (i[4] == 'Earphones'):
        cursor.execute(
            'select * from Earphone where Earphones_Item_ITEM_ID = {}'.format(i[1]))
        keys = cursor.fetchall()
        div = '''
              <div class ='users'>
            <label class="inline">Email:</label>
            <p class="inline">{}</p>
            <p>
            </p>
            <label class="inline">Item:</label>
            <p class="inline">{}</p>
                <a class="detail" href ='./details.py?id= {}'>More details</a>
                 <hr style="width:100%;text-align:left;margin-left:0">
             </div>
             <br>
        '''.format(i[0], i[4], keys[0][1])
        print(div)
    if (i[4] == 'CampusCard'):
        cursor.execute(
            'select * from Campus_Card where CampusCard_Item_ITEM_ID = {}'.format(i[1]))
        keys = cursor.fetchall()
        div = '''
            <div class ='users'>
            <label class="inline">Email:</label>
            <p class="inline">{}</p>
            <p>
            </p>
            <label class="inline">Item:</label>
            <p class="inline">{}</p>
                <a class="detail" href ='./details.py?id= {}'>More details</a>
                 <hr style="width:100%;text-align:left;margin-left:0">
             </div>
            <br>
        '''.format(i[0], i[4], keys[0][2])
        print(div)

footer = '''
        </body>
    </html>
'''

print(footer)
