from flask import render_template, request, jsonify, flash, url_for, redirect, session
import datetime
from app.DatabaseManager import dbM, Member, UtleiePakke, ReceiptUtleiepakker, KvitteringHeiskort
from app import app
from app.forms import RegistrationForm
from flask.ext.login import LoginManager, UserMixin, login_required, login_user, user_logged_in, logout_user

# Routes All routes is in this file.

#page to order heiskort
@app.route('/heiskort')
def heiskort():
    allCards = []
    for i in range(0,3):
        allCards.append(dbM.getHeiskortDB(i))
    return render_template('heisKort.html', allCards=allCards)

#Overviewpage to order utleie utstyr
@app.route('/utleie')
def utleie():
    utleiePakkene = dbM.getUtleiePakkeneFromDb();
    left1 =  dbM.calculateAmountOfUtleiepakker(1);
    return render_template('utleieHomePage.html', utleiePakkene=utleiePakkene, astor=2)


#spesific page to utleie utstyr
@app.route('/utleie/<pakkenummer>')
def utleieWithPakkenummer(pakkenummer):
    utleiePakkene = dbM.getUtleiePakkeneFromDb();
    utleiePakke = dbM.getUtleiePakkeFromDb(pakkenummer);

    #calculating how many is left
    howManyLeft =0;
    allReceipts = dbM.getAllReceiptFromASpesificUtleiepakker(pakkenummer)
    amountRentedOutAtTheMoment = 0;
    for i in allReceipts:
        print(i.outdated)
        if (not i.outdated):
            amountRentedOutAtTheMoment += 1
    howManyLeft = (utleiePakke.antLedige - amountRentedOutAtTheMoment);

    return render_template('utleie.html', utleiePakke=utleiePakke, utleiePakkene=utleiePakkene, howManyLeft=howManyLeft)


#Checkout for utleiepakker
@app.route('/checkout/<type>/<number>/<multiply>', methods=['GET', 'POST'])
def checkout(type, number, multiply):
    try:
        memberEmail = session["user_id"]
        member = dbM.getMemberFromEmail(memberEmail)

    except:
        return redirect('login')


    times = 1
    if (multiply=="3"):
        times = 25
        typeOfPrice = 'ukepris'
    if (multiply=="2"):
        typeOfPrice = 'dagspris'
        times = 5
    if (multiply=="1"):
        typeOfPrice = 'timepris'
        times = 1



    if request.method == 'GET':
        if (type == 'utleiepakker'):
            utleiePakke = dbM.getUtleiePakkeFromDb(number)
            return render_template('checkout.html', type='utleiepakker', utleiePakke=utleiePakke, member=member, number=number, times=times, typeOfPrice=typeOfPrice, multiply=multiply)

        if (type == 'paidMember'):
            return render_template('checkout.html', paidMember=True)

    if request.method == 'POST':
        print(request.form['child'])
        amount = (request.form['amount']) #TODO need to make sure this is correct
        print("amount: "+amount)
        print(request.form['code'])
        print(request.form['price'])

        receiptUtleiepakke = ReceiptUtleiepakker(-2,
                                                member.id,
                                                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                                int(multiply)-1, # TODO make this generic
                                                int(amount),
                                                number)

        dbM.registerReceiptUtleiepakker(receiptUtleiepakke)
        return redirect('minSide')

#Checkout for heiskort
@app.route('/checkout/<type>/<number>', methods=['GET','POST'])
def checkoutHeiskort(type, number):
    try:
        memberEmail = session["user_id"]
    except:
        return redirect('login')


    typeOfCard = "dager"
    if number=="1":
        typeOfCard="uker"
    if number=="2":
        typeOfCard="sesonger"

    card = dbM.getHeiskortDB(number)
    if request.method == 'GET':
        return render_template('checkout.html', card=card, type='heiskort', number=number, typeOfCard=typeOfCard)

    if request.method == 'POST':
        memberEmail = session["user_id"]
        amount= request.form['amount'];

        member = dbM.getMemberFromEmail(memberEmail)

        # def __init__(self, id, owner, startTime, heiskort):
        kvitteringHeiskort = KvitteringHeiskort(0,
                                                member.id,
                                                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                                card.id,
                                                int(amount))

        dbM.registerKvitteringHeiskort(kvitteringHeiskort)

        return redirect("minSide")




#Her kunne vi ogsaa lagt til etternavn, saa han hadde sjekket opp mot baade etternavnet til broren eller soesteren. Men det faar bli i 2.0
@app.route('/validateCode')
def validateCode():
    code = request.args.get('a', 1, type=str)
    if code=="JegErGladIFamilienMin":
        return jsonify(result="Ok")
    else:
        return jsonify(result="Feil")

