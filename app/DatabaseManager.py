import datetime
import math
import sqlite3

from flask import g

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


# Apner forbindelsen til databasen
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
        cur = db.execute('select * from utleiepakker WHERE id = ' + pakkenummer)
        entries = cur.fetchone()
        utleiePakke = UtleiePakke(entries[0], entries[1], entries[2], entries[3], entries[4], entries[5], entries[6],
                                  entries[7])
        print ('hentet ut: ' + utleiePakke.name)
        return utleiePakke

    def getUtleiePakkeneFromDb(self):
        utleiePakkene = []
        db = get_db()
        cur = db.execute('SELECT * FROM utleiepakker')
        entries = cur.fetchall()
        for row in entries:
            utleiePakkene.append(UtleiePakke(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        print ('Innlegget ble sendt og lagret i databasen')
        print("get utleiepakkene")
        return utleiePakkene

    def getMember(self, id):
        db = get_db()
        cur = db.execute('select * from members WHERE id =' + str(id))
        entries = cur.fetchone()
        member = Member(entries[0], entries[1], entries[2], entries[3], entries[4])
        return member

    # (id, name, email, password)
    def getMemberFromEmail(self, email):
        db = get_db()
        cur = db.execute("select * from members WHERE email = '" + email + "'");
        entries = cur.fetchone()
        member = Member(entries[0], entries[1], entries[2], entries[3], entries[4])
        return member

    def getKvitteringHeiskort(self, id):
        kvitteringHeiskort = []
        db = get_db()
        cur = db.execute('select * from kvitteringHeiskort WHERE owner=' + str(id))
        entries = cur.fetchall()
        for row in entries:
            kvitteringHeiskort.append(KvitteringHeiskort(row[0], row[1], row[2], row[3]))
        return kvitteringHeiskort

    def getReceiptUtleiepakker(self, id):
        receiptUtleiepakker = []
        db = get_db()
        cur = db.execute('select * from receiptUtleiepakker WHERE owner=' + str(id))
        entries = cur.fetchall()
        for row in entries:
            receiptUtleiepakker.append(ReceiptUtleiepakker(row[0], row[1], row[2], row[3], row[4], row[5]))
        return receiptUtleiepakker

    def getReceiptUtleiepakkerOfKind(self, id):
        receiptUtleiepakker = []
        db = get_db()
        cur = db.execute('select * from receiptUtleiepakker WHERE type=' + str(id))
        entries = cur.fetchall()
        for row in entries:
            receiptUtleiepakker.append(ReceiptUtleiepakker(row[0], row[1], row[2], row[3], row[4], row[5]))
        return receiptUtleiepakker


    def registerNewMember(self, member):
        db = get_db();
        try:
            db.execute('INSERT INTO members (name, email, password) VALUES(?, ?, ?)',
                       [member.name, member.email, member.password])
            db.commit()
            return True
        except:
            db.rollback()
            return False

    def registerReceiptUtleiepakker(self, receiptUtleiepakker):
        db = get_db();
        try:
            db.execute(
                    'INSERT INTO receiptUtleiepakker(owner, startTime, type, typeMultiplier, utleiePakke) VALUES (?,?,?,?,?)',
                    [receiptUtleiepakker.owner, receiptUtleiepakker.startTime, receiptUtleiepakker.type,
                     receiptUtleiepakker.typeMutiplier, receiptUtleiepakker.utleiepakkerNumber])
            db.commit()
            return True
        except:
            db.rollback()
            return False

    def registerKvitteringHeiskort(self, kvitteringHeiskort):
        db = get_db();
        try:
            db.execute('INSERT INTO kvitteringHeiskort (owner, startTime, heikort) VALUES (?, ?, ?)',
                       [kvitteringHeiskort.owner, kvitteringHeiskort.startTime, kvitteringHeiskort.heiskort])
            db.commit()
            return True
        except:
            db.rollback()
            return False

    def updateMember(self, newMember):
        db = get_db();
        # TODO feil med try catch?

        #test = "Hallo %s", member.email
        mem = newMember
        mem.name = "BARE TULL"

        sql = 'UPDATE members SET name = "%s", email = "%s", password = "%s", paidMember = %s WHERE id=%s' % (
        mem.name, mem.email, mem.password, str(mem.paidMember), str(mem.id));

        try:
            db.execute(sql)
            db.commit()
            print("OKAY, db updated with sqp: " + sql)
            return True
        except:
            db.rollback()
            print("FAILED, db did not update" + sql)

            return False

    #TODO Doublecheck if this works
    def calculateAmountOfUtleiepakker(self, utleiepakkeid):
        receiptUtleiepakke = self.getReceiptUtleiepakkerOfKind(utleiepakkeid)
        print(len(receiptUtleiepakke))
        amountInUse = 0;
        for rec in receiptUtleiepakke:
            print(rec.outdated)
            if (rec.outdated):
                print("true")
            else:
                amountInUse += 1;

        return amountInUse


    def getAllUtleiepakkerForAllYears(self):
        months = [0]*12
        for x in range(0,5):
            for i in self.getReceiptUtleiepakkerOfKind(x):
                startTimeObj = datetime.datetime.strptime(i.startTime, '%Y-%m-%d %H:%M:%S')
                months[startTimeObj.month] += 1
        return months


class UtleiePakke:
    id = -1
    name = ''
    beskrivelse = 'canine'
    ski = 'canine'
    shoes = 'canine'
    skiPoles = 'canine'
    price = 10
    childPrice = 5;
    antLedige = 0;

    def __init__(self, id, name, beskrivelse, ski, shoes, skiPoles, price, antLedige):
        self.name = name
        self.id = id
        self.beskrivelse = beskrivelse
        self.ski
        self.shoes = shoes
        self.skiPoles = skiPoles
        self.price = math.ceil(price)
        self.antLedige = antLedige
        self.childPrice = math.ceil(price / 2);


# member = Member(entries[0], entries[1], entries[2], entries[3])
class Member:
    id = ''
    name = ''
    email = ''
    password = ''
    paidMember = 0;

    def __init__(self, id, name, email, password, paidMember):
        self.name = name
        self.id = id
        self.email = email
        self.password = password
        self.paidMember = paidMember

    # Changes
    """def __init__(self, name, email, password):
        self.name = name
        self.id = -2
        self.email = email
        self.password = password"""

    def get_id(self):
        print(chr(id))
        return chr(id)

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

class Heiskort:
    id = -1
    categori = 'canine'  # class variable shared by all instances
    price = 10  # class variable shared by all instances

    def __init__(self, id, categori, price):
        self.categori = categori
        self.id = id
        self.price = price


class KvitteringHeiskort:
    id = -1
    owner = ''
    startTime = 'time'
    endTime = 'time'
    heiskort = object;
    outdated = True;

    # datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    def __init__(self, id, owner, startTime, heiskort):
        self.id = "L" + str(id)  # Adding an L to the receiptID so it will be unique
        self.owner = owner
        self.startTime = startTime
        self.heiskort = heiskort

        # now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        startTimeObj = datetime.datetime.strptime(startTime, '%Y-%m-%d %H:%M:%S')

        if (heiskort == 0):
            self.endTime = startTimeObj + datetime.timedelta(days=1)
            if (self.endTime > datetime.datetime.now()):
                self.outdated = False;

        if (heiskort == 1):
            self.endTime = startTimeObj + datetime.timedelta(days=7)
            if (self.endTime > datetime.datetime.now()):
                self.outdated = False;

        if (heiskort == 2):
            self.endTime = startTimeObj + datetime.timedelta(days=60)
            if (self.endTime > datetime.datetime.now()):
                self.outdated = False;


class ReceiptUtleiepakker:
    id = -1
    owner = ''
    startTime = 'time'
    utleiepakker = '';
    type = -1;
    typeMutiplier = -1;
    outdated = True;
    utleiepakkerNumber = 0

    def __init__(self, id, owner, startTime, type, typeMutiplier, utleiepakker):
        self.utleiepakkerNumber = utleiepakker
        self.id = "R" + str(id)  # Adding an R to the receiptID so it will be unique
        self.owner = owner
        self.startTime = startTime
        self.utleiepakker = self.nameOfUtleiepakke(utleiepakker);
        print("VERDIEN TIL SELF UTLEIE ER NA : "+self.utleiepakker)
        self.type = type;
        self.typeMutiplier = typeMutiplier

        startTimeObj = datetime.datetime.strptime(startTime, '%Y-%m-%d %H:%M:%S')

        # type 0 = hourly
        if (type == 0):
            self.endTime = startTimeObj + datetime.timedelta(hours=typeMutiplier)
            if (self.endTime > datetime.datetime.now()):
                self.outdated = False;

        # type 1 = daily
        if (type == 1):
            self.endTime = startTimeObj + datetime.timedelta(days=typeMutiplier)
            if (self.endTime > datetime.datetime.now()):
                self.outdated = False;

        # type2 = weekly
        if (type == 2):
            self.endTime = startTimeObj + datetime.timedelta(days=(7 * typeMutiplier))
            if (self.endTime > datetime.datetime.now()):
                self.outdated = False;

    def nameOfUtleiepakke(self, nummer):
        if nummer == 1:
            return 'Langrenn Pakka'
        elif nummer == 2:
            return 'Alpin Pakka'
        elif nummer == 3:
            return 'Telemark Pakka'
        elif nummer == 4:
            return 'Twintip Pakka'
        elif nummer == 5:
            return 'Super Pakka'
        else:
            return 'ulistet'


dbM = dbManager();
