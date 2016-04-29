from flask import render_template, request, redirect, session, escape
from app.DatabaseManager import dbM, Member
from app import app
from app.forms import RegistrationForm
from flask.ext.login import login_required, login_user, logout_user

#####################
#USER VIEWS/Auth    #
#####################

@app.route('/minSide')
@login_required
def minSide():
    memberEmail = session["user_id"]
    member = dbM.getMemberFromEmail(memberEmail);
    listOfRecipts = dbM.getKvitteringHeiskort(member.id) + dbM.getReceiptUtleiepakker(member.id);
    listOfRecipts.sort(key=lambda r: r.startTime)
    return render_template('minSide.html', member=member, listOfRecipts=listOfRecipts)

#update Member page
@app.route('/updateMember', methods=['GET', 'POST'])
@login_required
def updateMember():
    memberEmail = session["user_id"]
    member = dbM.getMemberFromEmail(memberEmail);
    print("her")
    if request.method == 'POST':
        member.name = request.form['name']
        if(request.form['paidMember']=='yes'):
            member.paidMember = 1;
            print(member.paidMember)
        else:
            member.paidMember = 0;

        if (request.form['password'] != ""):
            member.set_password(request.form['password'])

        dbM.updateMember(member)
        return redirect('minSide')

    return render_template('updateMember.html', member=member)


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            email = request.form['email']
            pw = request.form['password']

            user = dbM.getMemberFromEmail(email)
            if user is None:
                return render_template('login.html', error="Something went wrong, please try again with a correct username and passsword")

            if (user.check_password(pw)):
                login_user(user)
                return redirect('minSide')
            else:
                return render_template('login.html', error="Something went wrong, please try again with a correct username and passsword")
        except:
            return render_template('login.html', error="Something went wrong, please try again with a correct username and passsword")

    else :
        return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        member = Member(-3, form.name.data, form.email.data.lower(), form.password.data, 0)
        member.set_password(form.password.data)
        if(dbM.registerNewMember(member)):
            return redirect('login')
    return render_template('registerNewUser.html', form=form)
