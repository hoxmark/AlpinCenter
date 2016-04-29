from flask import render_template, request, jsonify, flash, url_for, redirect, session
import datetime
from app.DatabaseManager import dbM, Member, UtleiePakke, ReceiptUtleiepakker, KvitteringHeiskort
from app import app
from app.forms import RegistrationForm
from flask.ext.login import LoginManager, UserMixin, login_required, login_user, user_logged_in, logout_user

# Routes All routes is in this file.

import utleieAndHeiskort
import user

#Home/Index
@app.route('/')
def index():
    return render_template('index.html')

#About page.
@app.route('/about')
def about():
    months = dbM.getAllUtleiepakkerForAllYears();
    labels = ["Januar","Februar","Mars","April","Mai","Juni","Juli","August", "September", "Oktober", "November", "Desember"]
    return render_template('about.html', values=months, labels=labels)
