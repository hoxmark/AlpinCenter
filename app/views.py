from flask import render_template, request, jsonify, flash, url_for, redirect, session
import datetime
from DatabaseManager import dbM, Member, UtleiePakke, ReceiptUtleiepakker
from app import app
from login import RegistrationForm, LoginForm
from flask.ext.login import LoginManager, UserMixin, login_required, login_user, user_logged_in


# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pw = request.form['password']

        user = dbM.getMemberFromEmail(email)
        print("name: "+user.name)
        if (user.password == pw):
            print("Korrekt PW")

            if (login_user(user)):
                flash('Logged in successfully.')

            return redirect('minSide')

    else :
        print("GETter login")
        return render_template('login.html')


@app.route('/utleie')
def utleie():
    utleiePakkene = dbM.getUtleiePakkeneFromDb();
    return render_template('utleieHomePage.html', utleiePakkene=utleiePakkene, astor=2)


@app.route('/utleie/<pakkenummer>')
def utleieWithPakkenummer(pakkenummer):
    print(pakkenummer)

    utleiePakkene = dbM.getUtleiePakkeneFromDb();
    utleiePakke = dbM.getUtleiePakkeFromDb(pakkenummer);
    return render_template('utleie.html', utleiePakke=utleiePakke, utleiePakkene=utleiePakkene)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/minSide')
@login_required
def minSide():
    memberEmail = session["user_id"]
    member = dbM.getMemberFromEmail(memberEmail);
    listOfRecipts = dbM.getKvitteringHeiskort(member.id) + dbM.getReceiptUtleiepakker(member.id);
    listOfRecipts.sort(key=lambda r: r.startTime)

    return render_template('minSide.html', member=member, listOfRecipts=listOfRecipts)



@app.route('/updateMember', methods=['GET', 'POST'])
@login_required
def updateMember():
    memberEmail = session["user_id"]
    member = dbM.getMemberFromEmail(memberEmail);

    if request.method == 'POST':
        member.email = request.form['email']
        #TODO checkbok bool TO 1, checkbox false = 0
        member.name = request.form['name']
        dbM.updateMember(member)
        return render_template('minSide.html', member=member)
        #TODO send with spesific ID.


    return render_template('updateMember.html', member=member)





@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        member = Member(-3, form.name.data, form.email.data, form.password.data, 0)
        dbM.registerNewMember(member)
        return render_template('login.html', email=member.email)
    return render_template('newUser.html', form=form)

@app.route('/checkout/<type>/<number>/<multiply>', methods=['GET', 'POST'])
def checkout(type, number, multiply):
    times = 1
    print("m"+multiply)
    if (multiply=="3"):
        times = 25
        typeOfPrice = 'ukepris'
    if (multiply=="2"):
        typeOfPrice = 'dagspris'
        times = 5
    if (multiply=="1"):
        typeOfPrice = 'timepris'
        times = 1


    memberEmail = session["user_id"]
    member = dbM.getMemberFromEmail(memberEmail)

    if request.method == 'GET':
        if (type=='heisKort'):
            return '' #TODO make this sql

        if (type == 'utleiepakker'):
            utleiePakke = dbM.getUtleiePakkeFromDb(number)

            return render_template('checkout.html', type='utleiepakker', utleiePakke=utleiePakke, member=member, number=number, times=times, typeOfPrice=typeOfPrice )

        if (type == 'paidMember'):
            return render_template('checkout.html', paidMember=True)

    if request.method == 'POST':
        print(request.form['child'])
        amount = (request.form['amount']) #TODO need to make sure this is correct
        print("amount: "+amount)
        print(request.form['code'])
        print(request.form['price'])

        #def __init__(self, id, name, beskrivelse, ski, shoes, skiPoles, price, antLedige):

        utleiePakke = dbM.getUtleiePakkeFromDb(number)

        #def __init__(self, id, owner, startTime, type, typeMutiplier, utleiepakker):
        receiptUtleiepakke = ReceiptUtleiepakker(-2,
                                                member.id,
                                                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                                0, # TODO make this generic
                                                int(amount),
                                                utleiePakke)

        dbM.registerReceiptUtleiepakker(receiptUtleiepakke)



        return render_template('minSide.html', member=member)

@app.route('/validateCode')
def validateCode():
    code = request.args.get('a', 1, type=str)
    if code=="JegErGladIFamilienMin":
        return jsonify(result="Ok")
    else:
        return jsonify(result="Feil")
