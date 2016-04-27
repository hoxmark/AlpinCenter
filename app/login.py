from flask.ext.login import LoginManager
from wtforms import Form, BooleanField, TextField, PasswordField, validators

from flask import Flask, Response
from flask.ext.login import LoginManager, UserMixin, login_required


from DatabaseManager import dbM
from app import app

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    print(user_id)
    user = dbM.getMemberFromEmail(user_id)
    user.get_id()
    return user



"""@login_manager.request_loader
def load_user(user_id):
    print("start: @login_manager.request_loader")
    token = request.headers.get('Authorization')
    if token is None:
        token = request.args.get('token')
        print("requested Token")

    if token is not None:
        username,password = token.split(":") # naive token
        #user_entry = User.get(username)
        user = dbM.getMemberFromEmail(username)
        if (user is not None):
            if (user.password == password):
                print("@login_manager.request_loader: pw = pw")
                return user
    return None
"""





class RegistrationForm(Form):
    name = TextField('Username', [validators.Length(min=4, max=25)])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.Required(), validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.Required()])


class LoginForm(Form):
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.Required()
    ])


