#!/usr/bin/env python

import cgitb
cgitb.enable()

import cgi
form = cgi.FieldStorage()

username = form['_user'].value
pw = form['_pass'].value

import sqlite3

conn = sqlite3.connect('accounts.db')
c = conn.cursor()
conn.commit()

print 'Content-Type: text/html'
print
print '''
<html>
<head>
	<title>Open Chord Open Source</title>
</head>
<body>
	<h1>Open Chord Open Source</h1>
'''
for r in c.execute('select * from users where username=?;', [username]):
	#print 'hi'
	currentname=r[0]
	print "Hello, " + currentname + "."
conn.close()
print'''
</body>
</html>'''