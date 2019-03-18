from game_controller import GameController


def test_init():
    game_controller = GameController(400, 200, "Name", "black")
    assert game_controller.WIDTH == 400
    assert game_controller.HEIGHT == 200
    assert game_controller.PLAYER_NAME == "Name"
    assert game_controller.PLAYER_COLOR == "black"
    assert game_controller.FILE_NAME == "scores.txt"

    assert game_controller.is_black
    assert not game_controller.is_skip
    assert not game_controller.is_finished
    assert not game_controller.black_wins
    assert not game_controller.white_wins
    assert not game_controller.draw
    assert not game_controller.black_num
    assert not game_controller.white_num
    # assert not game_controller.is_record


def test__eq__():
    game_controller_1 = GameController(400, 200, "Name", "black")
    game_controller_2 = GameController(400, 200, "Name", "black")
    assert game_controller_1 == game_controller_2


def test_record_scores():
    with open("test_scores.txt", "w") as scores:
        scores.truncate()
    scores.close()

    game_controller = GameController(400, 200, "Name1", "black",
                                     "test_scores.txt")
    game_controller.black_wins = True
    game_controller.black_num = 10
    game_controller.white_num = 6
    game_controller.record_scores()

    with open("test_scores.txt", "r") as scores:
        records = scores.readlines()

    game_controller = GameController(400, 200, "Name2", "black",
                                     "test_scores.txt")
    game_controller.white_wins = True
    game_controller.black_num = 11
    game_controller.white_num = 5
    game_controller.record_scores()

    with open("test_scores.txt", "r") as scores:
        records = scores.readlines()

    game_controller = GameController(400, 200, "Name3", "black",
                                     "test_scores.txt")
    game_controller.draw = True
    game_controller.black_num = 9
    game_controller.white_num = 7
    game_controller.record_scores()

    with open("test_scores.txt", "r") as scores:
        records = scores.readlines()
    assert records[0] == "Name2 11\n"
    assert records[1] == "Name1 10\n"
    assert records[2] == "Name3 9\n"
