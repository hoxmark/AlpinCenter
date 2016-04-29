# import the Flask class from the flask module
from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)

Bootstrap(app)

#gjor alt med databasen
import DatabaseManager

#import router/views
from app.views import views

#gjor alt med navigatorbaren her
import nav


#gjor alt med login
import login

#This is not a very secure key. This will need to be changed to something "random"
app.config["SECRET_KEY"] = "ITSASECRET"

if __name__ == '__main__':
    app.run(debug=True)