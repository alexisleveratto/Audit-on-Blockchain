from config import Config
from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail, Message
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = "login"
migrate = Migrate(app, db)
posta = Mail(app)

from app import routes, models
