import pytest
from classes.page import Page
from classes.grid import Grid
from classes.form import Form
from classes.image import Image

def test_create_grid():
    grid = Grid()
    grid.addForm(1, 2, Form())
    grid.addForm(1, 2, Form())
    grid.addForm(1, 2, Form())
    page = Page()
    page.addGrid(grid, 1, 2)
    assert page.getGrids() == [{'id': 1, 'x': 1, 'y': 2, 'grid': grid}]