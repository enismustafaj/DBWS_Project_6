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

date = form.getvalue('time')

if (date == '1week'):
    query = '''
    select  `Person_email`, `Found_Item_ID`, `Found_Location`, `Found_Date`, `Image`, `Category`, `Color`, `Size` from Item join (select `Person_email`, `Found_Item_ID`, `Found_Location`, `Found_Date`, `Image` from Report join 
    `Found` on `Person_Has_ID` = `Found_Item_ID`) as rep on rep.Found_Item_ID = Item.ITEM_ID where `Category` = '{}' and ROUND(DATEDIFF(now(), `Found_Date`)/7, 0) <= 1 ; 
    '''.format(form.getvalue('category'))

elif (date == '2week'):
    query = '''
    select  `Person_email`, `Found_Item_ID`, `Found_Location`, `Found_Date`, `Image`, `Category`, `Color`, `Size` from Item join (select `Person_email`, `Found_Item_ID`, `Found_Location`, `Found_Date`, `Image` from Report join 
    `Found` on `Person_Has_ID` = `Found_Item_ID`) as rep on rep.Found_Item_ID = Item.ITEM_ID where `Category` = '{}' and ROUND(DATEDIFF(now(), `Found_Date`)/7, 0) <= 2 ; 
    '''.format(form.getvalue('category'))

elif (date == '1month'):
    query = '''
    select  `Person_email`, `Found_Item_ID`, `Found_Location`, `Found_Date`, `Image`, `Category`, `Color`, `Size` from Item join (select `Person_email`, `Found_Item_ID`, `Found_Location`, `Found_Date`, `Image` from Report join 
    `Found` on `Person_Has_ID` = `Found_Item_ID`) as rep on rep.Found_Item_ID = Item.ITEM_ID where `Category` = '{}' and TIMESTAMPDIFF(MONTH, now(), `Found_Date`) <=1 ; 
    '''.format(form.getvalue('category'))

else:
    query = '''
    select  `Person_email`, `Found_Item_ID`, `Found_Location`, `Found_Date`, `Image`, `Category`, `Color`, `Size` from Item join (select `Person_email`, `Found_Item_ID`, `Found_Location`, `Found_Date`, `Image` from Report join 
    `Found` on `Person_Has_ID` = `Found_Item_ID`) as rep on rep.Found_Item_ID = Item.ITEM_ID where `Category` = '{}' and TIMESTAMPDIFF(MONTH, now(), `Found_Date`) <=2 ; 
    '''.format(form.getvalue('category')) 



# query = '''
#     select  `Person_email`, `Found_Item_ID`, `Found_Location`, `Found_Date`, `Image`, `Category`, `Color`, `Size` from Item join (select `Person_email`, `Found_Item_ID`, `Found_Location`, `Found_Date`, `Image` from Report join 
#     `Found` on `Person_Has_ID` = `Found_Item_ID`) as rep on rep.Found_Item_ID = Item.ITEM_ID where `Category` = '{}' ; 
#     '''.format(form.getvalue('category'))

cursor.execute(query)
data = cursor.fetchall()

for i in data:

    if (i[5] == 'Keys'):
        cursor.execute('select * from `Keys` where Keys_Item_ITEM_ID = {}'.format(i[1]))
        keys = cursor.fetchall()

        div = '''
            <div  class= 'users'>
            <p class="inline">Email:</p>
            <p class="inline">{}</p><br>
            <p></p>
            <img class="inline" src ='{}' width = 200 height = 200>
            <p class="inline"><span id="imagename">Image</span></p>
            <p></p>
            <p class="inline">Category:</p>
            <p class="inline">{}</p>
                <a class="detail" href = './details.py?id = {}'>More details</a>
                 <hr style="width:100%;text-align:left;margin-left:0">
            </div>
            <br>
        '''.format(i[0], i[4], i[5], keys[0][3])
        print(div)
    if (i[5] == 'Earphones'):
        cursor.execute('select * from Earphone where Earphone_Item_ITEM_ID = {}'.format(i[1]))
        keys = cursor.fetchall()
        div = '''
            <div  class= 'users'>
            <p class="inline">Email:</p>
            <p class="inline">{}</p><br>
            <p></p>
            <img class="inline" src ='{}' width = 200 height = 200>
            <p class="inline"><span id="imagename">Image</span></p>
            <p></p>
            <p class="inline">Category:</p>
            <p class="inline">{}</p>
                <a class="detail" href = './details.py?id = {}'>More details</a>
                 <hr style="width:100%;text-align:left;margin-left:0">
            </div>
             <br>
        '''.format(i[0], i[4], i[5],keys[0][1])
        print(div)
    if (i[5] == 'CampusCard'):
        cursor.execute('select * from Campus_Card where CampusCard_Item_ITEM_ID = {}'.format(i[1]))
        keys = cursor.fetchall()
        div = '''
           <div  class= 'users'>
            <p class="inline">Email:</p>
            <p class="inline">{}</p><br>
            <p></p>
            <img class="inline" src ='{}' width = 200 height = 200>
            <p class="inline"><span id="imagename">Image</span></p>
            <p></p>
            <p class="inline">Category:</p>
            <p class="inline">{}</p>
                <a class="detail" href = './details.py?id = {}'>More details</a>
                 <hr style="width:100%;text-align:left;margin-left:0">
            </div>
            <br>
        '''.format(i[0], i[4], i[5], keys[0][2])
        print(div)

footer = '''
        </body>
    </html>
'''

print(footer)
