from othello import Othello
from board import Board
from tile import Tile
from game_controller import GameController
from record import Record


def test__init__():
    othello = Othello(400, 4, "Name", "black")

    board = Board(400, 4)
    gc = GameController(400, 400, "Name", "black")
    tiles = [Tile(100) for _ in range(16)]

    tile = tiles.pop()
    tile.set_white()
    board.grids[1][1] = tile

    tile = tiles.pop()
    tile.set_black()
    board.grids[1][2] = tile

    tile = tiles.pop()
    tile.set_black()
    board.grids[2][1] = tile

    tile = tiles.pop()
    tile.set_white()
    board.grids[2][2] = tile

    assert othello.board == board
    assert othello.gc == gc
    assert othello.tiles == tiles
    assert othello.valid_grids == set({})
    assert othello.is_black
    assert not othello.is_control


def test_update_info():
    othello = Othello(400, 4, "Name", "black")
    othello.gc.is_black = False
    othello.is_control = True
    othello.update_info()
    assert othello.gc.is_black
    assert not othello.is_control


def test_game_AI():
    othello = Othello(400, 4, "Name", "white")
    othello.update_info()
    othello.game_AI()
    assert any([isinstance(othello.board.grids[0][1], Tile),
                isinstance(othello.board.grids[1][0], Tile),
                isinstance(othello.board.grids[3][2], Tile),
                isinstance(othello.board.grids[2][3], Tile)])
    for i, j in [(0, 1), (1, 0), (3, 2), (2, 3)]:
        if isinstance(othello.board.grids[i][j], Tile):
            assert othello.board.grids[i][j].is_black


def test_control():
    othello = Othello(400, 4, "Name", "black")

    # test if I can make an illegal move
    othello.update_info()
    othello.control(0, 0)
    assert not othello.board.grids[0][0]
    assert othello.is_black
    assert not othello.is_control

    # test if I can make a legal move
    othello.update_info()
    othello.control(0, 1)
    assert not othello.is_black
    assert othello.is_control

    assert isinstance(othello.board.grids[0][1], Tile)
    assert othello.board.grids[0][1].is_black

    assert isinstance(othello.board.grids[1][1], Tile)
    assert othello.board.grids[1][1].is_black


def test_update_legal_move():
    othello = Othello(400, 4, "Name", "black")
    othello.update_legal_move()

    # worked in "d"
    assert isinstance(othello.board.grids[0][1], Record)
    assert not othello.board.grids[0][1].record["u"]
    assert othello.board.grids[0][1].record["d"] == 1
    assert not othello.board.grids[0][1].record["l"]
    assert not othello.board.grids[0][1].record["r"]
    assert not othello.board.grids[0][1].record["ul"]
    assert not othello.board.grids[0][1].record["ur"]
    assert not othello.board.grids[0][1].record["dl"]
    assert not othello.board.grids[0][1].record["dr"]

    # worked in "r"
    assert isinstance(othello.board.grids[1][0], Record)
    assert othello.board.grids[1][0].record["r"] == 1

    # worked in "u"
    assert isinstance(othello.board.grids[3][2], Record)
    assert othello.board.grids[3][2].record["u"] == 1

    # worked in "l"
    assert isinstance(othello.board.grids[2][3], Record)
    assert othello.board.grids[2][3].record["l"] == 1

    assert not isinstance(othello.board.grids[0][0], Record)

    # worked in "ul"
    othello.board.grids[1][1].flip()
    othello.update_legal_move()
    assert isinstance(othello.board.grids[3][3], Record)
    assert othello.board.grids[3][3].record["ul"] == 1
    othello.board.grids[1][1].flip()

    # worked in "ur"
    othello.board.grids[2][1].flip()
    othello.update_legal_move()
    assert isinstance(othello.board.grids[3][0], Record)
    assert othello.board.grids[3][0].record["ur"] == 1
    othello.board.grids[2][1].flip()

    # worked in "dr"
    othello.board.grids[2][2].flip()
    othello.update_legal_move()
    assert isinstance(othello.board.grids[0][0], Record)
    assert othello.board.grids[0][0].record["dr"] == 1
    othello.board.grids[2][2].flip()

    # worked in "dl"
    othello.board.grids[1][2].flip()
    othello.update_legal_move()
    assert isinstance(othello.board.grids[0][3], Record)
    assert othello.board.grids[0][3].record["dl"] == 1
    othello.board.grids[1][2].flip()


def test_put_tile_on():
    othello = Othello(400, 4, "Name", "black")
    tile = Tile(100)

    othello.put_tile_on(0, 0)
    assert othello.board.grids[0][0] == tile

    othello.is_black = False
    othello.put_tile_on(0, 0)
    tile.flip()
    assert othello.board.grids[0][0] == tile


def test_flip():
    othello = Othello(400, 4, "Name", "black")

    othello.flip(0, 0, "dr", 1)
    assert othello.board.grids[1][1].is_black
    othello.flip(0, 0, "dr", 1)

    othello.flip(0, 3, "dl", 1)
    assert not othello.board.grids[1][2].is_black
    othello.flip(0, 3, "dl", 1)

    othello.flip(3, 0, "ur", 1)
    assert not othello.board.grids[2][1].is_black
    othello.flip(3, 0, "ur", 1)

    othello.flip(3, 3, "ul", 1)
    assert othello.board.grids[2][2].is_black
    othello.flip(3, 3, "ul", 1)

    othello.flip(1, 0, "r", 1)
    assert othello.board.grids[1][1].is_black
    othello.flip(1, 0, "r", 1)

    othello.flip(1, 3, "l", 1)
    assert not othello.board.grids[1][2].is_black
    othello.flip(1, 3, "l", 1)

    othello.flip(0, 1, "d", 1)
    assert othello.board.grids[1][1].is_black
    othello.flip(0, 1, "d", 1)

    othello.flip(3, 1, "u", 1)
    assert not othello.board.grids[2][1].is_black
    othello.flip(3, 1, "u", 1)


def test_skip_or_finish():
    # test when game is not finished
    othello = Othello(400, 4, "Name", "black")
    othello.update_legal_move()
    othello.skip_or_finish()
    assert not othello.gc.is_finished

    # test when skipping this turn
    othello.board.take_off(1, 1)
    othello.board.take_off(1, 2)
    othello.board.take_off(2, 1)
    othello.board.take_off(2, 2)
    for i in range(4):
        othello.is_black = False
        othello.put_tile_on(0, i)
        if i > 0:
            othello.is_black = True
            othello.put_tile_on(1, i)
    othello.update_legal_move()
    othello.skip_or_finish()
    assert othello.gc.is_skip
    assert not othello.is_black

    othello.control(2, 0)
    othello.update_legal_move()
    othello.skip_or_finish()
    assert not othello.gc.is_skip

    # test whether no empty grids will finish the game
    othello = Othello(400, 2, "Name", "black")
    othello.skip_or_finish()
    assert othello.gc.is_finished

    # test whether no legal moves will finish the game
    othello.board.take_off(0, 0)
    othello.skip_or_finish()
    assert othello.gc.is_finished

    # test whether all tiles are in one color will finish the game
    othello.board.take_off(1, 1)
    othello.skip_or_finish()
    assert othello.gc.is_finished


def test_judge_game():
    othello = Othello(400, 4, "Name", "black")

    # assert the draw
    othello.judge_game()
    assert not othello.gc.black_wins
    assert not othello.gc.white_wins
    assert othello.gc.draw
    assert othello.gc.white_num == 2
    assert othello.gc.black_num == 2

    # assert black wins
    othello.put_tile_on(0, 0)
    othello.judge_game()
    assert othello.gc.black_wins
    assert not othello.gc.white_wins
    assert not othello.gc.draw
    assert othello.gc.white_num == 2
    assert othello.gc.black_num == 3

    # assert white wins
    othello = Othello(400, 4, "Name", "black")
    othello.is_black = False
    othello.put_tile_on(0, 0)
    othello.judge_game()
    assert not othello.gc.black_wins
    assert othello.gc.white_wins
    assert not othello.gc.draw
    assert othello.gc.white_num == 3
    assert othello.gc.black_num == 2


# def test_skip_if_need():
#     board = Board(400, 4)
#     game_controller = GameController(400, 400, "Name", "black")
#     othello = Othello(board, game_controller)
#     othello.board.take_off(1, 1)
#     othello.board.take_off(1, 2)
#     othello.board.take_off(2, 1)
#     othello.board.take_off(2, 2)
#     for i in range(4):
#         othello.put_on(0, i, "white")
#         if i > 0:
#             othello.put_on(1, i, "black")
#     othello.update_legal_move()
#     othello.skip_if_need()
#     assert othello.gc.is_skip
#     assert not othello.is_black
#     othello.update_legal_move()
#     othello.control(2, 0)
#     othello.update_legal_move()
#     othello.skip_if_need()
#     assert not othello.gc.is_skip
