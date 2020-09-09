import pytest
import requests

from app.models import User

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
