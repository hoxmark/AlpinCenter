# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View




# create the application object
app = Flask(__name__)
Bootstrap(app)

nav = Nav()

@nav.navigation()
def mynavbar():
    return Navbar(
        'mysite',
        View('Home', 'index'),
        View('Login', 'login'),
        View('Utleie', 'utleie'),
        View('Om oss', 'about')
    )



nav.init_app(app)

# use decorators to link the function to a url
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/utleie')
def utleie():
    return render_template('utleie.html')


@app.route('/about')
def about():
    return render_template('about.html')





if __name__ == '__main__':
    app.run(debug=True)