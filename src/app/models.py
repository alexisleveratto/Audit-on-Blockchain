from app import db, login, app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from time import time
import jwt


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    client_name = db.Column(db.String(64))
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    hashCode = db.Column(db.String(120))
    role = db.Column(db.String(50), unique=False)

    contract = db.relationship("Contract", backref="client", lazy="dynamic")
    balance = db.relationship("Balance", backref="user", lazy="dynamic")

    def __repr__(self):
        return "<User {}>".format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {"reset_password": self.id, "exp": time() + expires_in},
            app.config["SECRET_KEY"],
            algorithm="HS256",
        ).decode("utf-8")

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])[
                "reset_password"
            ]
        except:
            return
        return User.query.get(id)

    def set_role(self, role):
        self.role = role

    def set_client_name(self, client_name):
        self.client_name = client_name


class Country(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String(64), index=True, unique=True)
    city = db.relationship("City", backref="country", lazy="dynamic")

    def __repr__(self):
        return "<Country {}>".format(self.country_name)


class City(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    zip_code = db.Column(db.Integer, index=True, unique=True)
    city_name = db.Column(db.String(64), index=True)
    country_id = db.Column(db.Integer, db.ForeignKey("country.id"))
    office = db.relationship("Office", backref="city", lazy="dynamic")

    def __repr__(self):
        return "<City {}>".format(self.city_name)


class Office(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(128), index=True, unique=True)
    city_id = db.Column(db.Integer, db.ForeignKey("city.id"))

    def __repr__(self):
        return "<Office {}>".format(self.address)


class Contract(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fee = db.Column(db.Float, index=True)
    init_date = db.Column(db.String(128))
    end_date = db.Column(db.String(128))
    client_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return "<Contract {}>".format(self.init_date)


class Account(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_account = db.Column(db.String(128), index=True, unique=True)
    balance = db.relationship("Balance", backref="account", lazy="dynamic")

    def __repr__(self):
        return "<Account {}>".format(self.name_account)


class Balance(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Float, index=True)
    client_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    account_id = db.Column(db.Integer, db.ForeignKey("account.id"))

    def __repr__(self):
        return "<Balance {}>".format(self.client_id)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
