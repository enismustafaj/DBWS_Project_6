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

cursor.execute("select * from Person")
data = cursor.fetchall()

res = []

for i in data:
    res.append(i[0])


html = '''
<html>
    <head>
        <link rel="stylesheet" href="search.css">
        <script src="http://ajax.aspnetcdn.com/ajax/jQuery/jquery-1.5.min.js" type="text/javascript"></script>
<script src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.9/jquery-ui.min.js" type="text/javascript"></script>
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>

    <body>
'''
print(html)
print('<script>')
print('var items = [];')

for i in res:
    print("items.push(\"{}\");".format(i))

print('console.log(items);')
print('</script>')


jquery = '''
    <script>
      $( function() {

    $( "#auto" ).autocomplete({
      source: items
    });
  } );

  </script>
'''
print(jquery)

body = '''

        <h1 id ="head"> Find Your Friends</h1>
        <div id = 'formlost'>
            <form style="text-align: center;margin-top: 10%;" action="./resuser.py" method="GET">
                <input type="text" class = 'comp' name = 'email' id = 'auto'>
                <input class="button" type="submit" value="Search">
            </form>
        </div>



    </body>
</html>
'''
print(body)