# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)

Bootstrap(app)

#import router/views
import views

#gjor alt med navigatorbaren her
import nav

#gjor alt med databasen
import DatabaseManager


# run it
if __name__ == '__main__':
    app.run(debug=True)