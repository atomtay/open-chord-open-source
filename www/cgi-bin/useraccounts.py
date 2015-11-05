#!"C:\Python27\python.exe"

# the above line is for Windows. For Mac OS, use the path to your Python,
# which is usually:
#!/usr/bin/env python


# Lecture 4 - CSC210 Fall 2015
# Philip Guo

# To create a database named people.db, run:
#
# python lecture4-create-database.py


import sqlite3

# create a database file named 'people.db' if it doesn't exist yet.
# if this file already exists, then the program will quit.
conn = sqlite3.connect('accounts.db')
c = conn.cursor()

# create a new 'users' table with three columns: name, age, image
c.execute('create table users(name varchar(100), username varchar(100) primary key, password varchar(100))')

# commit ('save') the transaction and close the connection
conn.commit()
conn.close()