from app import app
from flask import Flask, render_template
from DatabaseManager import dbManager

#Routes
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/utleie')
def utleie():
    dbM = dbManager();
    utleiePakkene = dbM.getUtleiePakkeneFromDb();

    return render_template('utleieHomePage.html', utleiePakkene=utleiePakkene)

@app.route('/utleie/<pakkenummer>')
def utleieWithPakkenummer(pakkenummer):

    print(pakkenummer)
    dbM = dbManager();
    utleiePakkene = dbM.getUtleiePakkeneFromDb();

    utleiePakke = dbM.getUtleiePakkeFromDb(pakkenummer);
    return render_template('utleie.html', utleiePakke=utleiePakke, utleiePakkene=utleiePakkene)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/minSide')
def minSide():
    memberId=0

    dbM = dbManager();
    member = dbM.getMember(memberId);
    kvitteringHeiskort = dbM.getKvitteringHeiskort(memberId)
    receiptUtleiepakker = dbM.getReceiptUtleiepakker(memberId)
    print(receiptUtleiepakker)


    listOfRecipts = kvitteringHeiskort + receiptUtleiepakker;

    listOfRecipts.sort(key=lambda r: r.startTime)





    return render_template('minSide.html', member=member, listOfRecipts=listOfRecipts)


