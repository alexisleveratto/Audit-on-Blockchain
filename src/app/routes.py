from app import app, db, posta
from app.forms import (
    AuditIndexForm,
    ChangePasswordForm,
    EmailForm,
    LoginForm,
    PasswordForm,
    RegisterClientForm,
    RegistrationForm,
)
from app.models import User
from app.utilsfunctions import get_random_string
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from flask_mail import Message
from werkzeug.urls import url_parse


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
@login_required
def index():
    title = "Menu Principal"
    form = AuditIndexForm()
    if form.validate_on_submit():
        if form.RegistrarCliente.data:
            return redirect(url_for("new_client"))
    return render_template("index.html", title=title, form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Usuario o Contraseña Invalidos")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("index")
        return redirect(next_page)
    return render_template("login.html", title="Iniciar Sesion", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Registrado")
        return redirect(url_for("login"))
    return render_template("register.html", title="Registro", form=form)


@app.route("/forgot-password", methods=["GET", "POST"])
def forgot():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = EmailForm()
    if form.validate_on_submit():
        mail = form.email.data
        check_mail = User.query.filter_by(email=mail).first()
        if check_mail:
            hashCode = get_random_string()
            check_mail.hashCode = hashCode
            db.session.commit()
            msg = Message(
                "Confirm Password Change",
                sender="alexis.leveratto@github.com",
                recipients=[mail],
            )
            msg.body = (
                "Hello,\nWe've received a request to reset your password. If you want to reset your password, click the link below and enter your new password\n http://127.0.0.1:5000/"
                + check_mail.hashCode
            )
            posta.send(msg)
            flash("Revise su email")
            return redirect(url_for("forgot"))
    return render_template(
        "forgot_password.html", title="Recuperar Contraseña", form=form
    )


@app.route("/<string:hashCode>", methods=["GET", "POST"])
def hashcode(hashCode):
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    check_by_hashCode = User.query.filter_by(hashCode=hashCode).first()
    if check_by_hashCode:
        form = PasswordForm()
        if form.validate_on_submit():
            check_by_hashCode.set_password(form.password.data)
            check_by_hashCode.hashCode = None
            db.session.commit()
            flash("Contraseña Recuperada con Éxito")
            return redirect(url_for("login"))
        return render_template(
            "change_password.html", title="Cambiar Contraseña", form=form
        )
    return redirect(url_for("index"))


@app.route("/change-password", methods=["GET", "POST"])
@login_required
def change():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.check_password(form.old_password.data):
            user.set_password(form.password.data)
            db.session.commit()
            logout_user()
            return redirect(url_for("index"))
        else:
            flash("Repita correctamente su contraseña anterior")
    return render_template(
        "user_change_password.html", title="Cambiar Contraseña", form=form
    )


@app.route("/new-client", methods=["GET", "POST"])
def new_client():
    if not current_user.is_authenticated:
        return redirect(url_for("index"))
    form = RegisterClientForm()
    if form.validate_on_submit():
        if form.submit.data:
            pass
        elif form.cancel.data:
            return redirect(url_for("index"))
    return render_template("client_register.html", form=form)
