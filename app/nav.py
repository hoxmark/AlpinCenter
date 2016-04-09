from flask_nav import Nav
from flask_nav.elements import Navbar, View
from app import app

nav = Nav()

@nav.navigation()
def mynavbar():
    return Navbar(
        'Ski Alpinanlegg',
        View('Home', 'index'),
        View('Utleie', 'utleie'),
        View('Login', 'login'),
        View('Om oss', 'about')
    )

nav.init_app(app)