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

cursor.execute("select * from Lost")
data = cursor.fetchall()

res = []

for i in data:
    if (not i[1] in res):
        res.append(i[2])

cursor.execute("select * from Found")
data = cursor.fetchall()
for i in data:
    if (not i[1] in res):
        res.append(i[1])
head = '''
<html>
    <head>

        <link rel="stylesheet" href="../search/search.css">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>

  
<script src="http://ajax.aspnetcdn.com/ajax/jQuery/jquery-1.5.min.js" type="text/javascript"></script>
<script src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.9/jquery-ui.min.js" type="text/javascript"></script>
<script>
var items = [];
'''
print(head)
for i in res:
    print("items.push(\"{}\")".format(i))
body = '''
  $( function() {
 
    $( "#tags" ).autocomplete({
      source: items
    });
  } );
  </script>
    <body>
        <h1 id ="head"> Search By Place</h1>
        <div id = 'formlost' class="ui-widget">
            <form style="text-align: center;margin-top: 10%;" action="./resplace.py" method="GET">
              <label for="tags" style="font-family: Chilanka; font-size:100; color:gray">Place: </label>
              <input id='tags' class='comp'style="font-family: Chilanka; font-size:50; color:gray" name = 'place'>
              <input class="button" type="submit" value="Search" id='tags'>
            </form>
        </div>



    </body>
</html>
'''
print(body)