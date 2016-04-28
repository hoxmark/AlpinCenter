DROP TABLE if exists members;
DROP TABLE if exists utleiepakker;
DROP TABLE if exists heisKort;
DROP TABLE if exists kvitteringHeiskort;
DROP TABLE if exists receiptUtleiepakker;

CREATE TABLE members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    paidMember INTEGER
);


CREATE TABLE kvitteringHeiskort (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  owner id,
  startTime TEXT,
  heikort INTEGER,
  FOREIGN KEY(owner) REFERENCES members(id),
  FOREIGN KEY(heikort) REFERENCES heisKort(id)

);

CREATE TABLE receiptUtleiepakker (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  owner id,
  startTime TEXT,
  type INTEGER,
  typeMultiplier INTEGER,
  utleiePakke INTEGER,
  FOREIGN KEY(owner) REFERENCES members(id),
  FOREIGN KEY(utleiePakke) REFERENCES utleiepakker(id)
);

CREATE TABLE heisKort(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  categori TEXT NOT NULL,
  price INTEGER
);

CREATE TABLE utleiepakker (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT ,
  beskrivelse TEXT ,
  ski TEXT ,
  shoes TEXT ,
  skiPoles TEXT ,
  price INTEGER,
  antLedige INTEGER
);



INSERT INTO members (id, name, email, password, paidMember) VALUES(0, 'Bjorn Hoxmark', 'hoxmark@me.com', 'pbkdf2:sha1:1000$RdQZfJr7$8f5eee349005d01c67c47b68997f8267317dbd52', 1 );
INSERT INTO members (id, name, email, password, paidMember) VALUES(1, 'Kari Normann','Kari@norman.no', '123', 0);
INSERT INTO members (id, name, email, password, paidMember) VALUES(2, 'McGlagen Normann','McGlagen@norman.no', '123', 1);
INSERT INTO members (id, name, email, password, paidMember) VALUES(3, 'test','test@test.no', 'test', 1);

INSERT INTO utleiepakker (id, name, beskrivelse, ski, shoes, skiPoles, price, antLedige) VALUES(1, 'Langrenn Pakka','Fantastisk bra sett for å stå på langrenn, dette er det settet vi anbefaler til alle som skal stå langrenn', 'Ski', 'Sko', 'staver', 79, 10);
INSERT INTO utleiepakker (id, name, beskrivelse, ski, shoes, skiPoles, price, antLedige) VALUES(2, 'Alpin Pakka','Fantastisk bra sett for å stå på alpin, dette er det settet vi anbefaler til alle som skal stå alpin', 'Ski', 'Sko', 'staver', 99, 10);
INSERT INTO utleiepakker (id, name, beskrivelse, ski, shoes, skiPoles, price, antLedige) VALUES(3, 'Telemark Pakka','Fantastisk bra sett for å stå på telemark, dette er det settet vi anbefaler til alle som skal stå telemark', 'Ski', 'Sko', 'staver', 109, 5);
INSERT INTO utleiepakker (id, name, beskrivelse, ski, shoes, skiPoles, price, antLedige) VALUES(4, 'Twintip Pakka','Fantastisk bra sett for å stå på twintip, dette er det settet vi anbefaler til alle som skal stå twintip', 'Ski', 'Sko', 'staver', 100, 19);
INSERT INTO utleiepakker (id, name, beskrivelse, ski, shoes, skiPoles, price, antLedige) VALUES(5, 'Super Pakka','Fantastisk bra sett for å stå på ski, dette er det settet vi anbefaler til alle som skal stå ski', 'Ski', 'Sko', 'staver', 199, 3);

INSERT INTO heisKort (id, categori, price) VALUES(0,'dagkort', 200);
INSERT INTO heisKort (id, categori, price) VALUES(1,'ukekort', 1000);
INSERT INTO heisKort (id, categori, price) VALUES(2,'sesongkort', 5000);

INSERT INTO kvitteringHeiskort (owner, startTime, heikort) VALUES (0, '2016-04-19 19:17:22', 0);
INSERT INTO kvitteringHeiskort (owner, startTime, heikort) VALUES (0, '2011-11-03 18:21:26', 1);
INSERT INTO kvitteringHeiskort (owner, startTime, heikort) VALUES (0, '2011-11-03 18:21:26', 2);
INSERT INTO kvitteringHeiskort (owner, startTime, heikort) VALUES (1, '2011-11-03 18:21:26', 1);
INSERT INTO kvitteringHeiskort (owner, startTime, heikort) VALUES (2, '2011-11-03 18:21:26', 2);

INSERT INTO receiptUtleiepakker(owner, startTime, type, typeMultiplier, utleiePakke) VALUES (0,'2016-04-18 19:17:22', 1, 3, 1);
INSERT INTO receiptUtleiepakker(owner, startTime, type, typeMultiplier, utleiePakke) VALUES (1,'2011-11-03 18:21:26', 1, 3, 2);
INSERT INTO receiptUtleiepakker(owner, startTime, type, typeMultiplier, utleiePakke) VALUES (2,'2011-11-03 18:21:26', 2, 1, 3);




