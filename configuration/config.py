import os


class Config(object):
    TESTING = False
    FLASK_RUN_PORT = os.environ.get("FLASK_RUN_PORT")


class ProductionConfig(Config):
    SECRET_KEY = "secret_for_production_environment"


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    SECRET_KEY = "secret_for_test_environment"
