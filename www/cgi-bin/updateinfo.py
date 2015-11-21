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

for r in c.execute('select * from people where username=?', [currentUser]):
	name = r[0]
	username = r[1]
	location = r[3]
	birthday = r[4]
	bio = r[5]

if(location==None):
	location=""
if(birthday==None):
	birthday=""
if(bio==None):
	bio=""

# prints a minimal HTTP header
print 'Content-Type: text/html'
print

# print the HTTP body, which is the HTML file representing lecture1.html

print '<html>'
print '<head>'
print '''
	<script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
	
	<script type="text/javascript">
	
		var profileLink = "/cgi-bin/profile.py?user=" + localStorage['username']
			$(document).ready(function() {
			$("#logout").click(function() {
				localStorage.removeItem('username');
				console.log("You out dawg!");
			});

			$("#profileLink").click(function() {
				console.log("Hello?");
				$("#profileLink").attr("href", profileLink);
				console.log("Hello!");
			});
'''
#c.execute("update people set deptid=3 where empid=101;")
print'''
			$("#submit").click(function(){
				var newName = $('#grabName').val();
				var newLocation = $('#grabLocation').val();
				var newBirthday = $('#grabBirthday').val();
				var newBio = $('#grabBio').val();
'''
#c.execute("update people set name=? where username=?", ['newName', currentUser])

print '''
			})
		})
	
		</script>
'''
print'''<style>
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

			#bio_area{
				font-size: 1em;
				font-family: Times New Roman;
				resize: none;
			}
  		</style>
'''


print '<title>Update your Info</title>'
print '</head>'
print '<body>'
print'''<img src="../FinalLogo.jpg" id="logo"/>
		<ul id = "nav">
			<li><a href="/">Home</a></li>
			<li><a id ="profileLink" href="/">Profile</a></li>
			<li><a href="">Find Tracks</a></li>
			<li><a id="logout" href="/">Logout</a></li>
		</ul>'''

print '''
<div id="content">
<form method='post' id='main' action="updateinfo.py">
<table>
  <tr>
    <td>Name:</td>
'''

print '<td><input name="_name" type=text size="50" id="grabName" value='+name+'/></td>'
print''' 
  </tr>
  <tr>
  <td>Location:</td>
'''
print '<td><input name="_location" type=text size="50" id="grabLocation" value='+location+'/></td></tr>'

print'''
    <tr><td>Birthday:</td>
'''
print '<td><input name="_birthday" type=text size="50" id="grabBirthday" value='+birthday+'/></td>'
print ''' 
  </tr>
  <tr>
  	<td>Bio:</td>
'''
print '<td><textarea rows="4" cols="53" name="comment" id="grabBio" form="main">'+bio+'</textarea></td>'
print'''</tr>
  <tr>
  	<td>Picture:</td>
  	<td>Will put a change picture thing here...</td>
  </tr>
</table>
<input type='submit' id='submit'/>
</form>
</div>
'''


print '</body>'
print '</html>'

conn.close()