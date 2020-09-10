import pytest
import requests

from app import db
from app.models import User

from app.classes.cliente import Cliente
from app.classes import BlockchainManager

############## Commiting to the SQLite DB ##############
# Testeamos solamente la conexión a la base de datos de SQLite.
def add_user(username, email, password):
    try:
        user = User(username=username, email=email)
        user.set_password(password)
        user.set_role("Client")
        user.set_client_name(client_name=username)
        db.session.add(user)
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False


def delete_user(username):
    try:
        user = User.query.filter_by(username=username).first()
        db.session.delete(user)
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False


##########################################################

# Prueba de Registro de Cliente: Validar datos obligatorios del cliente.
# a.Permitir registrar cliente con los datos completos: si el auditor ingresa todos los datos obligatorios,
# se debe permitir pasar a la siguiente etapa de registro.


def test_register_client_ok():
    test_client_username = "test_Client"
    test_client_password = "test_password"
    test_client_email = "test_email@email.com"

    assert add_user(
        username=test_client_username,
        email=test_client_email,
        password=test_client_password,
    )
    assert delete_user(test_client_username)


# b.Rechazar registro de cliente con los datos incompletos: si el auditor cuando no completa todos los campos requeridos,
# no debe continuar con el proceso de registro.
def test_register_client_fail():
    test_client_username = "Client"
    test_client_password = "client"
    test_client_email = "client@email.com"

    assert not (
        add_user(
            username=test_client_username,
            email=test_client_email,
            password=test_client_password,
        )
    )


# Prueba de Inicio de Sesión: Validar datos obligatorios.
# a. Permitir iniciar sesión cuando presenta los datos completos: cuando el usuario
# completa tanto el campo usuario como contraseña, el sistema le debe permitir pasar al apartado de validación de datos.
def test_login_client_ok():
    test_client_username = "Client"
    test_client_password = "client"

    test_client = User.query.filter_by(username=test_client_username).first()

    assert test_client.check_password(test_client_password)


def test_login_audit_ok():
    test_audit_username = "Audit"
    test_audit_password = "audit"

    test_audit = User.query.filter_by(username=test_audit_username).first()
    assert test_audit.check_password(test_audit_password)


# b. Rechazar el inicio de sesión cuando los datos sean incompletos: cuando el usuario no completa todos los campos, no
# se debe permitir validar dichos datos posteriormente.

def test_login_client_fail_username():
    test_client_username = "Not Client"

    test_client = User.query.filter_by(username=test_client_username).first()
    assert not (test_client)


def test_login_client_fail_password():
    test_client_username = "Client"
    test_client_password = "Fake-Password"

    add_user(
        username=test_client_username, email="test@email.com", password="real_password"
    )
    test_client = User.query.filter_by(username=test_client_username).first()

    assert not (test_client.check_password(test_client_password))


def test_login_audit_fail_username():
    test_audit_username = "Not-Audit"

    test_audit = User.query.filter_by(username=test_audit_username).first()
    assert not (test_audit)


def test_login_audit_fail_password():
    test_audit_username = "Audit"
    test_audit_password = "not-password"

    test_audit = User.query.filter_by(username=test_audit_username).first()
    assert not (test_audit.check_password(test_audit_password))