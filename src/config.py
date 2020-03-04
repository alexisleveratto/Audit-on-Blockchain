import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_USERNAME = 'beratbozkurt1999@gmail.com'
    MAIL_PASSWORD = '[password]'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

    SECRET_KEY = os.environ.get("SECRET_KEY") or "secret_key"

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
