#!"C:\Python27\python.exe"

# the above line is for Windows. For Mac OS, use the path to your Python,
# which is usually:
#!/usr/bin/env python


# Lecture 4 - CSC210 Fall 2015
# Philip Guo

# To create a database named people.db, run:
#
# python lecture4-create-database.py

#Run this when you need to update the database!
import sqlite3

# create a database file named 'people.db' if it doesn't exist yet.
# if this file already exists, then the program will quit.
conn = sqlite3.connect('accounts.db')
c = conn.cursor()

#c.execute('create table people(name varchar(100), username varchar(100) primary key, password varchar(100), location varchar(100), instruments varchar(100), bio varchar(500));')
#c.execute("insert into people values('Philip','pgbovineman', 'passcat', 'Rochester', '','');")
for r in c.execute('select * from people;'):
	print r

loginUsername = "pgbovineman"
r = c.execute('select * from people where username=?', [loginUsername])
for n in r:
	print r[n]

checkPassword = c.execute('select password from people where username=?', [loginUsername])

conn.commit()
conn.close()