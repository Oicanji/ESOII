import pytest

from classes.grid import Grid
from classes.form import Form
from classes.image import Image

def test_create_grid():
    grid = Grid()
    assert grid.getForms() == []

def test_add_form_to_grid():
    grid = Grid()
    form = Form()
    form.addPoint(10, 10)
    form.addPoint(10, 20)
    form.addPoint(20, 20)
    form.addPoint(20, 10)
    form.setImage(Image('src/img/1.png'))
    grid.addForm(form)
    assert grid.getForms() == [form]

def test_add_form_to_grid_with_border():
    grid = Grid()
    form = Form()
    form.addPoint(10, 10)
    form.addPoint(10, 20)
    form.addPoint(20, 20)
    form.addPoint(20, 10)
    form.setImage(Image('src/img/1.png'))
    form.setBorder(1, 'solid', 'black')
    grid.addForm(form)
    assert grid.getForms() == [form]