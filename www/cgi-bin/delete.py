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

print '<title>Delete Account</title>'
	#http://papermashup.com/read-url-get-variables-withjavascript/
print '''
	<script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
	<script type="text/javascript">
		
		var profileLink = "/cgi-bin/profile.py?user=" + localStorage['username']
		var updateLink = "/cgi-bin/updateinfo.py?user=" + localStorage['username']
		var deleteLink = "/cgi-bin/goodbye.py?user=" + localStorage['username']
			
			$(document).ready(function() {
				function getUrlVars() {
					var vars = {};
					var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) {
						vars[key] = value;
					});
					return vars;
				};
				var first = getUrlVars()["user"];

				$("#logout").click(function() {
					localStorage.removeItem('username');
				});
	
				$("#profileLink").click(function() {
					$("#profileLink").attr("href", profileLink);
				});

				$("#definitelyDelete").click(function() {
					console.log("Are we here?");
					$("#definitelyDelete").attr("href", deleteLink);
					console.log("Deleted.")
				});

			})
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
	<img src="../FinalLogo.jpg" id="logo"/>
		<ul id = "nav">
			<li><a href="/">Home</a></li>
			<li><a id="profileLink" href="/profile.html">Profile</a></li>
			<li><a href="/cgi-bin/tracks.py">Find Tracks</a></li>
			<li><a id="logout" href="/">Logout</a></li>
		</ul>'''
print'''
		<div id="content">
We're sad to see you go. Are you sure you want to delete your account?
<p><a id="definitelyDelete" href="goodbye.py">Yes, delete my account.</a></p>
<p>No. Take me back!</p>
		</div>

'''
print'</body>'
print'</html>'

conn.close()