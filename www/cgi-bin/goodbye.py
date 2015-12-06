#!/usr/bin/env python

import cgitb
cgitb.enable()

import datetime

import cgi
form = cgi.FieldStorage()

import sqlite3
conn = sqlite3.connect('accounts.db')
c = conn.cursor()


currentUser = form["user"].value

# prints a minimal HTTP header
print 'Content-Type: text/html'
print
print '<html>'
print '	<head>'

print '<title>Account Deleted</title>'
	#http://papermashup.com/read-url-get-variables-withjavascript/
print '''
	<script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
	<script type="text/javascript">
		
	localStorage.removeItem('username');
	</script>
'''

print'''
		<style>
  			#content {
  				margin-top: 25px;
  				margin-left: 5%;
  				margin-right: 5%;
			}

			#logo{

				width:40%;
				height:40%;
				margin-top: -10px;
			}

			#nav{
				list-style-type: none;
				display: inline;
			}

			#nav li{
				display: inline;
				font-size: 1.3em;
				padding-left: 25px;
			}
			body {
				font-size: 1.1em;
				font-family: Verdana;
			}
  		</style>
	</head>
'''
#"I can't think and listen to jazz at the same time!!!" - Katherine Briant
'<body>'
print'''
	We'll miss you!

'''
print currentUser
print'</body>'
print'</html>'
c.execute('delete from people where username="%s"' %currentUser)
conn.commit()

conn.close()