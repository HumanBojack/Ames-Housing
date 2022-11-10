import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv

db = SQLAlchemy()

def create_app():
    load_dotenv("app/.env", override=True)

    # Create the app object
    app = Flask(__name__)
    print("Creating the app object")

    # Set some configuration variable for the app
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

    # Connect the database to the application
    db.init_app(app)

    # Create the user login handler
    login_manager = LoginManager(app)
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # Register the auth routes
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # Register the main app routes
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Register the predictions routes
    from .predictions import predictions as predictions_blueprint
    app.register_blueprint(predictions_blueprint, url_prefix="/predictions")

    # generate methods for the user model
    from app.models import User
    @login_manager.user_loader
    def load_user(email):
        return User.query.get(email)
    
    # Create the database if it doesn't already exists
    from app import models
    db.create_all(app=app)
        
    return app

def create_db(app):
    from app import models
    db.drop_all(app=app)
    db.create_all(app=app)