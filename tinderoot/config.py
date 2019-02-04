class Config(object):
    # Some default config
    MAIL_SERVER = 'smtp.localhost.test'
    MAIL_DEFAULT_SENDER = 'admin@demo.test'

class Development(Config):
    """
    Testing config
    """
    SECRET_KEY = "Some really random string"
    SQLALCHEMY_DATABASE_URI = 'sqlite://' # In-memory sqlite db
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Production(Config):
    """
    Production config
    """
    SECRET_KEY = ""
    _SQLALCHEMY_DATABASE_DATABASE = 'MAJER_API'
    _SQLALCHEMY_DATABASE_HOSTNAME = 'localhost'
    _SQLALCHEMY_DATABASE_PASSWORD = '19970202'
    _SQLALCHEMY_DATABASE_USERNAME = 'postgres'
    SQLALCHEMY_DATABASE_URI = 'postgres://{u}:{p}@{h}/{d}'.format(
        d=_SQLALCHEMY_DATABASE_DATABASE, h=_SQLALCHEMY_DATABASE_HOSTNAME,
        p=_SQLALCHEMY_DATABASE_PASSWORD, u=_SQLALCHEMY_DATABASE_USERNAME
    )
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app_config = {
    'development' : Development,
    'production': Production
}