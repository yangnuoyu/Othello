from tile import Tile


def test__init__():
    tile = Tile(50)
    assert tile.DIAMETER == 50
    assert tile.is_black


def test__eq__():
    tile_1 = Tile(50)
    tile_2 = Tile(50)
    assert tile_1 == tile_2


def test_flip():
    tile = Tile(50)
    tile.flip()
    assert not tile.is_black


def test_set_white():
    tile = Tile(50)
    tile.set_white()
    assert not tile.is_black


def test_set_black():
    tile = Tile(50)
    tile.is_black = False
    tile.set_black()
    assert tile.is_black
