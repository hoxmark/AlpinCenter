from flask.ext.login import LoginManager

from DatabaseManager import dbM
from app import app
from wtforms import Form, BooleanField, TextField, PasswordField, validators

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    print("def load_user(user_id):")
    return dbM.getMember(user_id)


login_manager.init_app(app)


class RegistrationForm(Form):
    name = TextField('Username', [validators.Length(min=4, max=25)])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
    validators.Required(), validators.EqualTo('confirm', message='Passwords must match')
])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.Required()])
