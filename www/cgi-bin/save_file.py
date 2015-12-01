#!/usr/bin/env python

#http://code.activestate.com/recipes/273844-minimal-http-upload-cgi/
import cgi
import cgitb; cgitb.enable()
import os, sys
try: # Windows needs stdio set for binary mode.
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    pass

UPLOAD_DIR = "/home/annabelle_taylor/Documents/College/Junior Year/Fall Semester/CSC 210/www/user-recordings"

HTML_TEMPLATE = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
	<title>File Upload</title>
	<script src='http://code.jquery.com/jquery-1.11.3.min.js'></script>
	<script src='../js/basicscript.js'></script>
	<link rel="stylesheet" type="text/css" href="../mystyle.css">
</head>


<body>
	<img src="../FinalLogo.jpg" id="logo"/>
		<ul id = "nav">
			<li><a href="/">Home</a></li>
			<li><a id="profileLink" href="/profile.html">Profile</a></li>
			<li><a href="/cgi-bin/tracks.py">Find Tracks</a></li>
			<li><a id="logout" href="/">Logout</a></li>
		</ul>
	<div id="content">
	<form action="%(SCRIPT_NAME)s" method="POST" enctype="multipart/form-data">
		File name: <input name="file_1" type="file"><br>
		<input name="submit" type="submit">
	</form>
	</div>
</body>

</html>"""

def print_html_form ():
    """This prints out the html form. Note that the action is set to
      the name of the script which makes this is a self-posting form.
      In other words, this cgi both displays a form and processes it.
    """
    print "content-type: text/html\n"
    print HTML_TEMPLATE % {'SCRIPT_NAME':os.environ['SCRIPT_NAME']}

def save_uploaded_file (form_field, upload_dir):
    """This saves a file uploaded by an HTML form.
       The form_field is the name of the file input field from the form.
       For example, the following form_field would be "file_1":
           <input name="file_1" type="file">
       The upload_dir is the directory where the file will be written.
       If no file was uploaded or if the field does not exist then
       this does nothing.
    """
    form = cgi.FieldStorage()
    if not form.has_key(form_field): return
    fileitem = form[form_field]
    if not fileitem.file: return
    fout = file (os.path.join(upload_dir, fileitem.filename), 'wb')
    while 1:
        chunk = fileitem.file.read(100000)
        if not chunk: break
        fout.write (chunk)
    fout.close()

save_uploaded_file ("file_1", UPLOAD_DIR)

print_html_form ()