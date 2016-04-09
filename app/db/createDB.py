#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3
conn = sqlite3.connect('blogg.db')
print "Opened database successfully"
conn.execute(''' drop table nyheter''') #sletter den gamle.

#Oppretter tabellen nyheter
conn.execute('''create table nyheter (
  id integer primary key autoincrement,
  tittel text not null,
  nyhet text not null,
  forfatter text not null,
  date text not null);''')
print "Table created successfully"
conn.close()


#lagre data:

conn = sqlite3.connect('blogg.db')
print "Opened database successfully"
with conn:
    cur = conn.cursor()
    cur.execute("insert into nyheter values(1,'Sportsnytt','Landslaget vant','Ola Nordmann','200392')")
    cur.execute("insert into nyheter values(2,'Sportsnytt','Landslaget vant igjen turneringen','Ola Nordmann','200392')")
    cur.execute("insert into nyheter values(3,'Utenriksnytt','Vla bbla bla avlyst','Ola Nordmann','200392')")


print "Data is inserted successfully"
conn.close()


#lese data:
conn = sqlite3.connect('blogg.db')
print "Opened database successfully"
with conn:
    cur = conn.cursor()
    cur.execute("select * from nyheter")
    rows = cur.fetchall()
    for row in rows:
        print row

print "Data is selected successfully"
conn.close()

