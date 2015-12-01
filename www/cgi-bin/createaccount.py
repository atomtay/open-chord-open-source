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

print "Content-type: text/html"
print ''# don't forget the extra newline
print '<html id="page">'
print '''<head>
	<script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
		<script type="text/javascript">
		$(document).ready(function() {
 				console.log("Hello world!");
 				$("#page").load("../youarein.html");
		});
	</script>
</head>'''
print '<body>'
print '''
	<div id="content">
	</div>
'''
print '</body>'
print '</html>'


conn.close()
