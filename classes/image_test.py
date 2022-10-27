import pytest

from classes.image import Image

@pytest.mark.parametrize("url", [ f"src/img/{x}.png" for x in range(1, 10) ])
def test_create_image(url):
    image = Image(url)
    assert image.get() == url