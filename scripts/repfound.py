#!/usr/bin/env python

import cgitb
import queries
import cgi
import mysql.connector
import MySQLdb
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
itemId = queries.random_item_id()

report = dict()

report['ITEM_ID'] = itemId
report['Status'] = 'found'
report['Username'] = form.getvalue('user')
try:

	x = dict()
	x['ITEM_ID'] = itemId
	x['Size'] = form.getvalue('size')
	x['Color'] = form.getvalue('color')
	x['Category'] = form.getvalue('categories')
	queries.website_input_item(cursor,x)
	queries.website_input_person_has_item(cursor,report)

	found = dict()
	found['ITEM_ID'] = itemId
	found['Date'] = form.getvalue('fdate')
	found['Location'] =  form.getvalue('flocation')
	found['Image'] = form.getvalue('image')
	queries.website_input_found(cursor, found)

	cat = form.getvalue('categories')

	if(cat == 'Keys'):
		data = (form.getvalue('roomnum'), form.getvalue('college'), form.getvalue('attach'), itemId)
		cursor.execute(queries.SQL_INSERT_KEYS, data)
	elif(cat == 'Earphones'):
		data = (form.getvalue('brand'), itemId,)
		cursor.execute(queries.SQL_INSERT_EARPHONE, data)
	elif(cat == 'CampusCard'):
		data = (form.getvalue('matnum'), form.getvalue('name'), itemId,)
		cursor.execute(queries.SQL_INSERT_CAMPUS_CARD, data)

#print(cursor)
	mydb.commit()
	print('<p>success</p>')
except (MySQLdb.Error, MySQLdb.Warning) as e:
	print('<p>{} </p>'.format(e))

