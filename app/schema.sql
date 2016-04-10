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

INSERT INTO utleiepakker (id, name, beskrivelse, ski, shoes, skiPoles, price) VALUES(1, 'Langrenn Pakka','Fantastisk bra sett for å stå på langrenn, dette er det settet vi anbefaler til alle som skal stå langrenn', 'Ski', 'Sko', 'staver', 79);
INSERT INTO utleiepakker (id, name, beskrivelse, ski, shoes, skiPoles, price) VALUES(2, 'Alpin Pakka','Fantastisk bra sett for å stå på alpin, dette er det settet vi anbefaler til alle som skal stå alpin', 'Ski', 'Sko', 'staver', 99);
INSERT INTO utleiepakker (id, name, beskrivelse, ski, shoes, skiPoles, price) VALUES(3, 'Telemark Pakka','Fantastisk bra sett for å stå på telemark, dette er det settet vi anbefaler til alle som skal stå telemark', 'Ski', 'Sko', 'staver', 109);
INSERT INTO utleiepakker (id, name, beskrivelse, ski, shoes, skiPoles, price) VALUES(4, 'Snowboard Pakka','Fantastisk bra sett for å stå på twintip, dette er det settet vi anbefaler til alle som skal stå twintip', 'Ski', 'Sko', 'staver', 100);
INSERT INTO utleiepakker (id, name, beskrivelse, ski, shoes, skiPoles, price) VALUES(5, 'Super Pakka','Fantastisk bra sett for å stå på ski, dette er det settet vi anbefaler til alle som skal stå ski', 'Ski', 'Sko', 'staver', 199);
