from flask import render_template, request

from DatabaseManager import dbM, Member
from app import app
from login import RegistrationForm


# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')



@app.route('/utleie')
def utleie():
    utleiePakkene = dbM.getUtleiePakkeneFromDb();

    return render_template('utleieHomePage.html', utleiePakkene=utleiePakkene)


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
def minSide():
    memberId = 0
    member = dbM.getMember(memberId);
    listOfRecipts = dbM.getKvitteringHeiskort(memberId) + dbM.getReceiptUtleiepakker(memberId);
    listOfRecipts.sort(key=lambda r: r.startTime)

    return render_template('minSide.html', member=member, listOfRecipts=listOfRecipts)



@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        member = Member(form.name.data, form.email.data, form.password.data)
        dbM.registerNewMember(member)
        #flash('Thanks for registering')
        return render_template('login.html', email=member.email)
    return render_template('newUser.html', form=form)
