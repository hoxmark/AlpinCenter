import sqlite3
from flask import  g
from app import app

DATABASE = 'alpin.db'
app.config.from_object(__name__)

def connect_db():
    """Kobler til databasen."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

# lager databasen
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# pner forbindelsen til databasen
def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

# lukker forbindelsen til databasen
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()



class dbManager:
    def __init__(self):
        init_db()


    def getUtleiePakkeFromDb(self, pakkenummer):
        print("getting pakkenummer from DB")
        db = get_db()
        cur = db.execute('select * from utleiepakker WHERE '+pakkenummer)
        entries = cur.fetchone()
        print(entries)
        print ('Innlegget ble sendt og lagret i databasen')




class UtleiePakke:
    id = -1
    name = 'canine'         # class variable shared by all instances
    beskrivelse = 'canine'         # class variable shared by all instances
    ski = 'canine'         # class variable shared by all instances
    shoes = 'canine'         # class variable shared by all instances
    skiPoles = 'canine'         # class variable shared by all instances
    price = 10

    def __init__(self, id, name, beskrivelse, ski, shoes, skiPoles, price):
        self.name = name
        self.id = id
        self.beskrivelse = beskrivelse
        self.ski
        self.shoes = shoes
        self.skiPoles = skiPoles
        self.price = price

