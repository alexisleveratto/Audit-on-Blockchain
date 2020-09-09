from config import Config
from flask import Flask, request
from flask_babel import Babel
# from flask_babel import lazy_gettext as _l
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail, Message
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = "login"
login.login_message = _l("Por favor inicie sesión para acceder a esta página")
migrate = Migrate(app, db)
posta = Mail(app)


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config["LANGUAGES"])


from app import routes, models
