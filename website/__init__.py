from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'

    from .views import views
    app.register_blueprint(views, url_prefix = '/')
    from .auth import auth
    app.register_blueprint(auth, url_prefix = '/')
    from .projectviews import project_views
    app.register_blueprint(project_views, url_prefix = '/projects')
    
    return app
