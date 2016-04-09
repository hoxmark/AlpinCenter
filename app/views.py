from app import app
from flask import Flask, render_template
from DatabaseManager import dbManager

#Routes
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/utleie')
def utleie():
    return render_template('utleie.html')

@app.route('/utleie/<pakkenummer>')
def utleieWithPakkenummer(pakkenummer):
    print(pakkenummer)
    dbM = dbManager();
    dbM.getUtleiePakkeFromDb(pakkenummer);

    return render_template('utleie.html', pakkenummer=pakkenummer)


@app.route('/about')
def about():
    return render_template('about.html')


