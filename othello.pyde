from othello import Othello

BOARD_SIZE = 800
GAME_SIZE = 8
PLAYER_COLOR = "black"
counter = 60
simple_game = None


def setup():
    global simple_game
    size(BOARD_SIZE, BOARD_SIZE)
    colorMode(RGB)

    player_name = input('enter your name')
    if player_name:
        print('hi ' + player_name)
    elif player_name == '':
        player_name = "unknown"
        print('[empty string]')
    else:
        print(player_name)  # Canceled dialog will print None
    simple_game = Othello(BOARD_SIZE, GAME_SIZE, player_name, PLAYER_COLOR)


def draw():
    global counter
    background(0)
    simple_game.update_info()
    simple_game.display()
    if (PLAYER_COLOR == "black" and not simple_game.is_black) or\
       (PLAYER_COLOR == "white" and simple_game.is_black):
        counter -= 1
        if counter == 0:
            simple_game.game_AI()
            counter = 60


def mousePressed():
    if (PLAYER_COLOR == "black" and simple_game.is_black) or\
       (PLAYER_COLOR == "white" and not simple_game.is_black):
        i = int(mouseY // (BOARD_SIZE/GAME_SIZE))
        j = int(mouseX // (BOARD_SIZE/GAME_SIZE))
        simple_game.control(i, j)
        redraw()


def input(self, message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)
