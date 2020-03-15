import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USERNAME = "chinoleveratto2@gmail.com"
    MAIL_PASSWORD = "password_bitch"
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

    SECRET_KEY = os.environ.get("SECRET_KEY") or "secret_key"

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    UPLOAD_FOLDER = os.environ.get("UPLOAD_FOLDER") or "/app/audit_results/"
    MAX_CONTENT_LENGTH = os.environ.get("MAX_CONTENT_LENGTH") or 16 * 1024 * 1024
