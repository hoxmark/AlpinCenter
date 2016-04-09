#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3
conn = sqlite3.connect('alpin.db')
print "Opened database successfully"
#conn.execute(''' DROP TABLE members''')  # sletter den gamle.

# Oppretter tabellen members

conn.executescript('''
DROP TABLE members;
DROP TABLE utleiepakker;

CREATE TABLE members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstName TEXT NOT NULL,
    lastName TEXT NOT NULL);

  CREATE TABLE utleiepakker (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT ,
    beskrivelse TEXT ,
    ski TEXT ,
    shoes TEXT ,
    skiPoles TEXT ,
    price INTEGER);
    ''');



print "Table created successfully"
conn.close()

# lagre data:

conn = sqlite3.connect('alpin.db')
print "Opened database successfully"
with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO members (firstName, lastName) VALUES('Bjonn','Hox')")
    cur.execute("INSERT INTO members (firstName, lastName) VALUES('Jorg','wim')")
    cur.execute("INSERT INTO members (firstName, lastName) VALUES('Borg','Lie')")


    cur.execute("INSERT INTO utleiepakker (id, name, beskrivelse, ski, shoes, skiPoles, price) VALUES(1, 'Bjørn Dæli Pakka','for det meste for de som går langrenn', 'Ski', 'Sko', 'staver', 100)");


print "Data is inserted successfully"
conn.close()

# lese data:
conn = sqlite3.connect('alpin.db')
print "Opened database successfully"
with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM members")
    rows = cur.fetchall()
    for row in rows:
        print row


    cur.execute("SELECT * FROM utleiepakker")
    rows = cur.fetchall()
    for row in rows:
        print row

print "Data is selected successfully"
conn.close()
