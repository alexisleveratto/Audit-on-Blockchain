from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    client_name = db.Column(db.String(64))
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    hashCode = db.Column(db.String(120))
    role = db.Column(db.String(50), unique=False)

    contract = db.relationship("Contract", backref="client", lazy="dynamic")

    def __repr__(self):
        return "<User {}>".format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

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
    name_account = db.Column(db.String(128), index=True)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
