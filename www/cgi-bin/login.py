#!/usr/bin/env python

 
import cgi
form = cgi.FieldStorage()

def printNotLoggedInPage():
	print "Content-type: text/html"
	print ''# don't forget the extra newline!
	print '<html>'
	print '<body>'
	print '<p>You are NOT yet logged in.</p>'
	print '<form method="post" action="login.py">'
	print 'Enter your usernamename:'
	print '<input name="_user" type=text size="30"/>'
	print 'Password:'
	print '<input name="_pass" type=text size="30"/>'
	print '<input type="submit"/>'
	print '</form>'
	print '</body></html>'

def printLoggedInPage(user):
	print "Content-type: text/html"
	print ''# don't forget the extra newline!
	print '<html>'
	print '''<head>
	</head>'''
	print '<body>'
	print 'hello ' + user
	print '</body>'
	print '</html>'

import sqlite3
conn = sqlite3.connect('accounts.db')
c = conn.cursor()

loginUsername = form['_user'].value
loginPassword = form['_pass'].value

is_user = False
for r in c.execute('select * from people where username=?', [loginUsername]):
	is_user = True
	if (r[2]==loginPassword):
		printLoggedInPage(loginUsername)
	else:
		printNotLoggedInPage()
if(!is_user):
	printNotLoggedInPage()

#for r in c.execute('select username from people'):
#	if (r[1]==loginUsername):
#		check=r[1]
#
i#f (check==None):
#	printNotLoggedInPage()

conn.close()