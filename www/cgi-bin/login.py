#!/usr/bin/env python

 
import cgi
form = cgi.FieldStorage()

import Cookie
import os

def printNotLoggedInPage():
	print "Content-type: text/html"
	print ''# don't forget the extra newline!
	print '<html>'
	print '''<head>
<script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>

		<script type="text/javascript">
			$(document).ready(function() {
  				console.log("Hello world!");
  				$("#content").load("../unsuccessfullogin.html");
			});
		</script>

	</head>
		'''
	print '<body>'
	print '''
		<div id="content">
		u wrong
		</div>
'''


	print '</body></html>'

#Calls jQuery function to load another HTMl file so that we don't have to make a huge document in here :)

def printLoggedInPage(user):
	print "Content-type: text/html"
	print ''# don't forget the extra newline
	print '<html>'
	print '''<head>
		<script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>

		<script type="text/javascript">
			$(document).ready(function() {
  				console.log("Hello world!");
  				$("#content").load("../youarein.html");
			});
		</script>
	</head>'''
	print '<body id="content">'
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
	if (r[0]==None):
		printNotLoggedInPage()
if(is_user==False):
	printNotLoggedInPage()
	
conn.close()