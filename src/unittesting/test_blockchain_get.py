import pytest
import requests

from app import db
from app.models import User


def add_user(username, email, password):
    try: 
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return True
    except:
        return False

def delete_user(username):
    try:
        user = User.query.filter_by(username=username).first()
        db.session.delete(user)
        db.session.commit()
        return True
    except:
        return False


def test_login_client_fail_username():
    test_client_username = "Not Client"

    test_client = User.query.filter_by(username=test_client_username).first()
    assert not(test_client)

def test_login_client_fail_password():
    test_client_username = "Client"
    test_client_password = "Fake-Password"
    
    add_user(username=test_client_username, email="test@email.com", password="real_password")
    test_client = User.query.filter_by(username=test_client_username).first()
    
    assert not(test_client.check_password(test_client_password))
    assert delete_user(test_client_username)


def test_login_audit_ok():
    test_audit_username = 'Audit'
    test_audit_password = 'audit'
    
    test_audit = User.query.filter_by(username=test_audit_username).first()
    assert test_audit.check_password(test_audit_password)

def test_login_audit_fail_username():
    test_audit_username = 'Not-Audit'

    test_audit = User.query.filter_by(username=test_audit_username).first()
    assert not(test_audit)

def test_login_audit_fail_password():
    test_audit_username = 'Audit'
    test_audit_password = 'not-password'

    test_audit = User.query.filter_by(username=test_audit_username).first()
    assert not(test_audit.check_password(test_audit_password))
