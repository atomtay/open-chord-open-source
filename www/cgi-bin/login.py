#!"C:\Python27\python.exe"
import cgitb
cgitb.enable()
 
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
	print 'boobs'
	print '	<head>'
	print "			<script src='http://code.jquery.com/jquery-1.11.3.min.js'></script>"
	print "			<script type='text/javascript'>"
	print '					function logOut() {'
	print "						localStorage.removeItem('username');"
	print "						document.location = '../index.html';"
	print '                 }'
	print "			</script>"
	print '			</head>'
	print '<body>'
	print 'hello ' + user
	print '<p>'
	print '		<button id="logOut" onclick="logOut()"> Log Out</button></p>'
	print '</body>'
	print '</html>'


#printNotLoggedInPage()

import sqlite3
conn = sqlite3.connect('accounts.db')
c = conn.cursor()

loginUsername = form['_user'].value

loginPassword = form['_pass'].value

if (loginPassword == "cookie"):
	printLoggedInPage(loginUsername)
else:
	#printNotLoggedInPage()
	is_user = False
	for r in c.execute('select * from people where username=?', [loginUsername]):
		is_user = True
		if (r[2]==loginPassword):
			import Cookie 
			import os

			c = Cookie.SimpleCookie()
			c['username'] = loginUsername

			printLoggedInPage(loginUsername)
		else:
			printNotLoggedInPage()
	if(is_user == False):
		printNotLoggedInPage()

conn.close()