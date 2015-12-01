#!/usr/bin/env python

import cgitb
cgitb.enable()

import datetime

import cgi
form = cgi.FieldStorage()

import sqlite3
conn = sqlite3.connect('accounts.db')
c = conn.cursor()

import os

try: # Windows needs stdio set for binary mode.
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    pass


currentUser = form["user"].value

for r in c.execute('select * from people where username=?', [currentUser]):
	name = r[0]
	username = r[1]
	location = r[3]
	birthday = r[4]
	bio = r[5]
title = name + "'s Profile"

if(location==None):
	location = "<i>This user hasn't input their location yet</i>"

# prints a minimal HTTP header
print 'Content-Type: text/html'
print
print '<html>'
print '	<head>'

print '<title>'
print title
print '</title>'
	#http://papermashup.com/read-url-get-variables-withjavascript/
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
'''			
print'''
			function getUrlVars() {
				var vars = {};
				var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) {
					vars[key] = value;
				});
				return vars;
			};
'''
print'''
			var first = getUrlVars()["user"];

			if(localStorage["username"]==first){
				console.log(first);
				$("#ifOwnAccount").html('<a id="update" href="">Update</a>');
				$("#update").click(function() {
					console.log("Hello?");
					$("#update").attr("href", updateLink);
					console.log("Hello!");
				});

'''

print'''			}

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
		<table cellpadding="10">
			<tr>
				<!--Picture, name, location, birthday, bio-->
				<td valign="top">
					<table border="1">
						<tr>'''

print '<td rowspan="3">' + 'Image image image' + '</td>'
							

print '<th>'+name+'</th>'
print '</tr>'
print '<tr>'
print '<td>'+location+'</td>'
print '</tr><tr>'
print'<td>'+birthday+'</td>'
print '</tr><tr>'
print '<td colspan="2">'+bio+'</td>'
print '</tr>'
print '</table>'
print'''
					</td>
					<!--Vertical line dividing two info sections-->
					<td><hr class="vertical"/></td>
					<!--User's music-->
					<td valign="top">
						<table border="1">
							<tr>
								<th>Solo Tracks</th>
							</tr>
							<tr>
								<td><a href="save_file.py">Add a new track</a>
								</td>
							</tr>
							<tr>
								<th>Remixes</th>
							</tr>
							<tr>
								<td>Add a new track
								</td>
							</tr>
						</table>
					</td>
				</tr>
			</table>
			<span id="ifOwnAccount">It me?</span>
		</div>

'''
print'</body>'
print'</html>'

conn.close()