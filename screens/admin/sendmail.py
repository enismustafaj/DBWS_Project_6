#!/usr/bin/env python

import cgitb
import cgi
import sys
import os
import smtplib
import random
import mysql.connector
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date



mydb = mysql.connector.connect(
host="localhost",
user="root",
password="root",
database = 'group6',
auth_plugin='mysql_native_password'
)

cursor = mydb.cursor()


today = date.today()

d1 = today.strftime("%Y-%m-%d")

cgitb.enable()

hash = random.getrandbits(128)

print("Content-Type: text/html;charset=utf-8\n\n")


form = cgi.FieldStorage()

email = form.getvalue('email')

email = email + '@jacobs-university.de'
server = 'gmail'
user = 'foundlost904@gmail.com'
passwd = 'lost.found1'
to = email 
subject = 'hello'
body = 'hello'
total = 1 




smtp_server = 'smtp.gmail.com'
port = 587

message = MIMEMultipart("alternative")
message["Subject"] = "Welcome to Lost and Found"
message["From"] = 'foundlost904@gmail.com'
message["To"] = email
to = email

html = """\
<html>
  <body>
    <p>Hi,<br></p>
    Your link to log in is <a href='http://192.168.117.166/html/screens/admin/check.py?id={}'>http://192.168.117.166/html/screens/admin/check.py?id={}</a>
  </body>
</html>
""".format(hash, hash)

message.attach(MIMEText(html, 'html'))


cursor.execute("select * from Moderator where Person_email = '{}'".format(email))

data = cursor.fetchall()

if(len(data) == 1):
     try:
          server = smtplib.SMTP(smtp_server,port)
          server.ehlo()
          if smtp_server == "smtp.gmail.com":
               server.starttls()
          server.login(user,passwd)
          for i in range(1, total+1):
               subject = 'Admin Login'
               server.sendmail(user,to,message.as_string())
               sys.stdout.flush()
               server.quit()
     except KeyboardInterrupt:

          sys.exit()
     except smtplib.SMTPAuthenticationError:
          sys.exit()

     query = ''' 
               update Moderator set Hash = %s, Login_Date = %s where Person_email = %s
          '''

     cursor.execute(query,(hash, d1, email))
     mydb.commit()
     print(email)
     print('<html><body><p>An email was sent to your email address</p></body></html>')
else:
     print('You are not ad admin')
