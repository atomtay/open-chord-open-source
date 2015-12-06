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
			var x = true;
			$(document).ready(function() {
				if (localStorage['username'] !== undefined && x == true)
				{
					document.location = "../youarein.html"
					x = false;
				}
				$("#click").click(function() {
					localStorage['username'] = $("#trial").val()
				})
			})
			
		</script>

		<title>Open Chord Open Source</title>
  		<style>
  			html, body{
  				width: 99%;
  				margin: 0 auto;
  			}

  			table{
  				margin: 0 auto;
  			}

  			#content {
  				text-align: center;
  				background-color: white;
  				margin-top: 10px;
			}
			#logo{
				width:60%;
				height:60%;
				margin-top: -10px;
			}
			body {
				font-size: 1.1em;
				font-family: Verdana
			}

			#click{
				margin: 10px;
				font-size: 1.05em;
				font-family: Verdana
			}
  		</style>
</head>'''
print '<body>'
print '''
	<div id="content">
	</div>
'''
print '</body>'
print '</html>'


conn.close()
