#!/usr/bin/env python

import cgitb
import queries
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

form = cgi.FieldStorage()

id = form.getvalue('id')
description = form.getvalue('description')
mod = form.getvalue('mod')
try:
	cursor.execute("select * from Item where ITEM_ID = {}".format(id))
	data = cursor.fetchall()

	category=data[0][1]

	cursor.execute("select * from Report where Person_Has_ID = {}".format(id))

	data = cursor.fetchall()
	status=data[0][0]

	if (status=='lost'):
		cursor.execute("delete from Lost where Lost_Item_ID = {}".format(id))

	else:
		cursor.execute("delete from Found where Found_Item_ID = {}".format(id))

	if (category == "Keys"):
		cursor.execute("delete from `Keys` where Keys_Item_ITEM_ID = {}".format(id))
	elif (category == "CampusCard"):
		cursor.execute("delete from Campus_Card where CampusCard_Item_ITEM_ID = {}".format(id))
	elif (category == "Earphones"):
		cursor.execute("delete from Earphone where Earphones_Item_ITEM_ID = {}".format(id))

	query = (mod, id, description)
	cursor.execute("INSERT into Moderator_Moderates_Lost_and_Found(Moderator_Person_email, Lost_and_Found_Specific_ITEM_ID, Reason) values(%s, %s, %s)", query)
	cursor.execute("delete from Report where Person_Has_ID = {}".format(id))
	cursor.execute('delete from Claim where Claim_Item_ID = {} '.format(id))
	cursor.execute("delete from Item where ITEM_ID = {}".format(id))
	mydb.commit()

	print("<p>success</p>")
except (MySQLdb.Error, MySQLdb.Warning) as e:
	print('<p>{}</p>'.format(e))

