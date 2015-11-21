#!/usr/bin/env python

import cgitb
cgitb.enable()

import datetime

import cgi
form = cgi.FieldStorage()

import sqlite3
conn = sqlite3.connect('accounts.db')
c = conn.cursor()

# prints a minimal HTTP header
print 'Content-Type: text/html'
print
print '<html>'
print '	<head>'

print '<title>'
print 'Tracks'
print '</title>'
print '''
<script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
		<script type="text/javascript">
		var profileLink = "/cgi-bin/profile.py?user=" + localStorage['username']
		var updateLink = "/cgi-bin/updateinfo.py?user=" + localStorage['username']
			$(document).ready(function() {
			$("#logout").click(function() {
				localStorage.removeItem('username');
				console.log("You out dawg!");
			});

			$("#update").click(function() {
				console.log("Hello?");
				$("#update").attr("href", updateLink);
				console.log("Hello!");
			});

			$("#profileLink").click(function() {
				console.log("Hello?");
				$("#profileLink").attr("href", profileLink);
				console.log("Hello!");
			});
		})
		</script>
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

		 /* nifty vertical line hack thanks to http://jsfiddle.net/8v1cpb0u/ */
			hr.vertical{
   				width: 0px;
   				height: 100px; /* or height in PX */
			} 
  		</style>
	</head>
'''
#"I can't think and listen to jazz at the same time!!!" - Katherine Briant
print
'<body>'
print'''
	<img src="../FinalLogo.jpg" id="logo"/>
		<ul id = "nav">
			<li><a href="/">Home</a></li>
			<li><a id="profileLink" href="/profile.html">Profile</a></li>
			<li><a href="/cgi-bin/tracks.py">Find Tracks</a></li>
			<li><a id="logout" href="/">Logout</a></li>
		</ul>'''
print'''
		<div id="content">
'''
for r in c.execute('select username from people'):
	usersUsername = r[0]
	url="/cgi-bin/profile.py?user="+usersUsername
	print '<a href="'+url+'">'+r[0]+'</a><br/>'
print'''
		</div>

'''
print'</body>'
print'</html>'

conn.close()