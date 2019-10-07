from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from service_application_package.config import Config
from flask_pymongo import PyMongo

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_class=Config):
    application = Flask(__name__)
    application.config.from_object(Config)
    mongo = PyMongo(application)
    db.init_app(application)
    bcrypt.init_app(application)
    login_manager.init_app(application)
    mail.init_app(application)

    from service_application_package.users.routes import users
    from service_application_package.main.routes import main
    from service_application_package.catalog.routes import catalog
    from service_application_package.item.routes import item
    from service_application_package.errors.handlers import errors
    application.register_blueprint(users)
    application.register_blueprint(main)
    application.register_blueprint(catalog)
    application.register_blueprint(item)
    application.register_blueprint(errors)
    @application.before_first_request
    def create_tables():
        from service_application_package import models
        db.create_all()
    return application
