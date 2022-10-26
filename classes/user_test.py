import pytest

from classes.user import User

def test_create_user():
    user = User('session')
    user.setName('name')
    user.saltPassword('senha123')
    assert user.getName() == 'name'
    assert user.auth('senha123') == True
    assert user.getSession() == 'session'
    assert user.isAdm() == False

