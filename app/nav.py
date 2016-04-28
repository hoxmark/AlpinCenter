from flask import session
from flask_nav import Nav
from flask_nav.elements import Navbar, View
from app import app

nav = Nav()

@nav.navigation()
def mynavbar():

    try:
        if(session["user_id"]):
            return Navbar(
            'Ski Alpinanlegg',
            View('Home', 'index'),
            View('Utleie', 'utleie'),
            View('Om oss', 'about'),
            View('logout', 'logout'),
            View('Min Side', 'minSide')
    )
    except Exception, e:
        return Navbar(
        'Ski Alpinanlegg',
        View('Home', 'index'),
        View('Utleie', 'utleie'),
        View('Om oss', 'about'),
        View('Login', 'login'),
        View('Registrer ny bruker', 'register'),
    )


    return Navbar(
        'Ski Alpinanlegg',
        View('Home', 'index'),
        View('Utleie', 'utleie'),
        View('Om oss', 'about'),
        View('Login', 'login'),
        View('Registrer ny bruker', 'register'),
        View('Min Side', 'minSide')
    )

nav.init_app(app)