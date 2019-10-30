from flask import Flask
from service_application_package.config import Config



def create_app(config_class=Config):
    application = Flask(__name__)
    application.config.from_object(Config)

    from service_application_package.main.routes import main
    from service_application_package.ga.routes import ga
    from service_application_package.errors.handlers import errors
    application.register_blueprint(main)
    application.register_blueprint(ga)
    application.register_blueprint(errors)
    return application
