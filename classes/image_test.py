import pytest

from classes.image import Image

@pytest.mark.parametrize("url", [ f"src/img/{x}.png" for x in range(1, 100) ])
def test_create_image(url):
    image = Image(url)
    assert image.get() == url