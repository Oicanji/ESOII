import pytest
from classes.guest import Guest

def test_session():
    guest = Guest()
    print(guest.getSession())
    assert guest.getSession() != ''
    assert len(str(guest.getSession())) > 31