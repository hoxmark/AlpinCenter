DROP TABLE if exists members;
DROP TABLE if exists utleiepakker;

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

INSERT INTO utleiepakker (id, name, beskrivelse, ski, shoes, skiPoles, price) VALUES(1, 'Bjørn Dæli Pakka','for det meste for de som går langrenn', 'Ski', 'Sko', 'staver', 100)
