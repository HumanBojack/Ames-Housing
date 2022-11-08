import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv(".env", override=True)
db = SQLAlchemy()
print("hellllo")

def create_app():
    # Create the app object
    app = Flask(__name__)
    print("creating the app object")

    # Set some configuration variable for the app
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

    # Connect the database to the application
    db.init_app(app)
    # login_manager = LoginManager(app)

    # Register the auth routes
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # Register the main app routes
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app