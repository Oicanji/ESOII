import pytest

from classes.guest import Guest
from classes.user import User
from classes.comic import Comic
from classes.page import Page
from classes.grid import Grid
from classes.form import Form
from classes.image import Image

def test_create_comic():
    guest = Guest()
    user = User(guest.getSession())
    comic = Comic('comic 1', user.getSession())
    assert comic.getPages() == []
    assert comic.getName() == 'comic 1'
