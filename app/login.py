from flask.ext.login import LoginManager

from DatabaseManager import dbM
from app import app

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    user = dbM.getMemberFromEmail(user_id)
    return user

