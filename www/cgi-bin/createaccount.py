#!/usr/bin/env python

import cgitb
cgitb.enable()

import cgi
form = cgi.FieldStorage()

name = form['_name'].value
username = form['_user'].value
pw = form['_pass'].value
confirmpw = form['_confirmpass'].value


import sqlite3

conn = sqlite3.connect('accounts.db')
c = conn.cursor()
if (pw==confirmpw):
	c.execute('insert into people values (?, ?, ?, ?, ?, ?)', (name, username, pw, None, None, None))
	
conn.commit()


# prints a minimal HTTP header
print 'Content-Type: text/html'
print

print '''<html>
	<head>
		<title>Open Chord Open Source</title>
	</head>'''
print'''	<body>
		<h1>Open Chord Open Source</h1>
'''
print "Hello, " + name + "."

conn.close()


print '''
	</body>
</html>'''
