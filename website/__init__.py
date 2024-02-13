from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config['SECRET_KEY'] = '12345'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{path.join(app.root_path, DB_NAME)}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import Users, Storage

    with app.app_context():
        db.create_all()

    from flask_login import LoginManager

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    login_manager.session_protection = 'strong'  # Security measure
    login_manager.cookie_samesite = True

    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(int(id))

    return app

from os import path

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)