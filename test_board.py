from board import Board


def test__init__():
    board = Board(400, 4)
    assert board.WIDTH == 400
    assert board.SIZE == 4
    assert board.GRID_WIDTH == 100
    assert len(board.grids) == 4
    assert len(board.grids[0]) == 4
    assert not board.grids[0][0]


def test__eq__():
    board_1 = Board(400, 4)
    board_2 = Board(400, 4)
    assert board_1 == board_2


def test_put_on():
    board = Board(400, 4)
    assert board.put_on(0, 0, [])
    assert board.grids[0][0] == []
    assert not board.grids[0][1]


def test_take_off():
    board = Board(400, 4)
    assert board.put_on(0, 0, [])
    assert board.grids[0][0] == []
    board.take_off(0, 0)
    assert not board.grids[0][0]


def test_up_grid():
    board = Board(400, 2)
    assert board.put_on(0, 0, 1)
    assert board.put_on(0, 1, 2)
    assert board.put_on(1, 0, 3)
    assert board.put_on(1, 1, 4)
    assert not board.up_grid(0, 0)
    assert board.up_grid(1, 0) == 1


def test_down_grid():
    board = Board(400, 2)
    assert board.put_on(0, 0, 1)
    assert board.put_on(0, 1, 2)
    assert board.put_on(1, 0, 3)
    assert board.put_on(1, 1, 4)
    assert not board.down_grid(1, 0)
    assert board.down_grid(0, 0) == 3


def test_left_grid():
    board = Board(400, 2)
    assert board.put_on(0, 0, 1)
    assert board.put_on(0, 1, 2)
    assert board.put_on(1, 0, 3)
    assert board.put_on(1, 1, 4)
    assert not board.left_grid(0, 0)
    assert board.left_grid(0, 1) == 1


def test_right_grid():
    board = Board(400, 2)
    assert board.put_on(0, 0, 1)
    assert board.put_on(0, 1, 2)
    assert board.put_on(1, 0, 3)
    assert board.put_on(1, 1, 4)
    assert not board.right_grid(1, 1)
    assert board.right_grid(1, 0) == 4


def test_up_left_grid():
    board = Board(400, 2)
    assert board.put_on(0, 0, 1)
    assert board.put_on(0, 1, 2)
    assert board.put_on(1, 0, 3)
    assert board.put_on(1, 1, 4)
    assert not board.up_left_grid(0, 0)
    assert not board.up_left_grid(0, 1)
    assert not board.up_left_grid(1, 0)
    assert board.up_left_grid(1, 1) == 1


def test_up_right_grid():
    board = Board(400, 2)
    assert board.put_on(0, 0, 1)
    assert board.put_on(0, 1, 2)
    assert board.put_on(1, 0, 3)
    assert board.put_on(1, 1, 4)
    assert not board.up_right_grid(0, 0)
    assert not board.up_right_grid(0, 1)
    assert not board.up_right_grid(1, 1)
    assert board.up_right_grid(1, 0) == 2


def test_down_left_grid():
    board = Board(400, 2)
    assert board.put_on(0, 0, 1)
    assert board.put_on(0, 1, 2)
    assert board.put_on(1, 0, 3)
    assert board.put_on(1, 1, 4)
    assert not board.down_left_grid(0, 0)
    assert not board.down_left_grid(1, 1)
    assert not board.down_left_grid(1, 0)
    assert board.down_left_grid(0, 1) == 3


def test_down_right_grid():
    board = Board(400, 2)
    assert board.put_on(0, 0, 1)
    assert board.put_on(0, 1, 2)
    assert board.put_on(1, 0, 3)
    assert board.put_on(1, 1, 4)
    assert not board.down_right_grid(1, 1)
    assert not board.down_right_grid(0, 1)
    assert not board.down_right_grid(1, 0)
    assert board.down_right_grid(0, 0) == 4
