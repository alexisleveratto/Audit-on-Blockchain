from app import app, posta
from flask import render_template
from flask_mail import Message


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    posta.send(msg)


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email(
        subject="Recuperar Contraseña",
        sender=app.config["ADMINS"][0],
        #    recipients=[user.email],
        recipients=["chinoleveratto2@gmail.com"],
        text_body=render_template("email/reset_password.txt", user=user, token=token),
        html_body=render_template("email/reset_password.html", user=user, token=token),
    )
