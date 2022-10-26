import pytest

from classes.form import Form
from classes.image import Image

def test_create_form():
    form = Form()
    form.addPoint(10, 10)
    form.addPoint(10, 20)
    form.addPoint(20, 20)
    form.addPoint(20, 10)
    assert form.isForm() == True

def test_not_formed_form():
    form = Form()
    form.addPoint(10, 10)
    form.addPoint(10, 20)
    assert form.isForm() == False

def test_create_form_with_image():
    form = Form()
    form.addPoint(10, 10)
    form.addPoint(10, 20)
    form.addPoint(20, 20)
    form.addPoint(20, 10)
    form.setImage(Image('src/img/1.png'))
    assert form.isForm() == True
