# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)

Bootstrap(app)

#gjor alt med databasen
import DatabaseManager

#import router/views
import views

#gjor alt med navigatorbaren her
import nav


#gjor alt med login
import login

# run it

app.config["SECRET_KEY"] = "ITSASECRET"

if __name__ == '__main__':
    app.run(debug=True)