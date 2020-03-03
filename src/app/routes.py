from app import app
from app.forms import LoginForm
from flask import flash, redirect, render_template, url_for


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "aleveratto001"}
    title = "Menu Principal"
    posts = [
        {"author": {"username": "John"}, "body": "Beautiful day in Portland!"},
        {"author": {"username": "Susan"}, "body": "The Avengers movie was so cool!"},
    ]
    # return render_template('index.html', title=title, user=user)
    return render_template("index.html", title=title, user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            "Login requested for user {}, remember_me={}".format(
                form.username.data, form.remember_me.data
            )
        )
        return redirect(url_for("index"))
    return render_template("login.html", title="Iniciar Sesion", form=form)
