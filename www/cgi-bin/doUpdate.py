#!/usr/bin/env python
import cgitb
cgitb.enable()

import cgi
form = cgi.FieldStorage()

import sqlite3
conn = sqlite3.connect('accounts.db')
c = conn.cursor()

currentUser = form["user"].value

c.execute("update people set name='" + form['name'].value + 
	"', location='" + form['location'].value + 
	"', instruments='" + form['birthday'].value + 
	"', bio='" + form['bio'].value +
	"'where username='" + currentUser +"'")

conn.commit()

print "Content-Type: text/html"
print ""