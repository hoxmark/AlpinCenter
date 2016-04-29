from flask import render_template
from app.DatabaseManager import dbM
from app import app

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
