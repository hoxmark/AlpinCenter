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
        View('Om oss', 'about'),
        View('Login', 'login'),
        View('Min Side', 'minSide')
    )

nav.init_app(app)