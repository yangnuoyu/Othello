import re


class GameController:
    """Maintains the state of the game."""
    def __init__(self, WIDTH, HEIGHT, PLAYER_NAME, PLAYER_COLOR,
                 file_name="scores.txt"):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.PLAYER_NAME = PLAYER_NAME
        assert PLAYER_COLOR in ["black", "white"], "Wrong color!"
        self.PLAYER_COLOR = PLAYER_COLOR
        self.FILE_NAME = file_name

        self.is_black = True
        self.is_skip = False
        self.is_finished = False
        self.black_wins = False
        self.white_wins = False
        self.draw = False
        self.black_num = None
        self.white_num = None

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def display(self):
        """Carries out necessary actions when game is in processing"""
        if self.is_black:
            fill(255, 0, 0)
            textSize(20)
            text("Turn: Black", 50, 50)
        else:
            fill(255, 0, 0)
            textSize(20)
            text("Turn: White", 50, 50)
        if self.is_finished:
            if self.black_wins:
                fill(0, 255, 0)
                textSize(50)
                text("BLACK WINS!!!", self.WIDTH/2 - 140, self.HEIGHT/2)
                text("Black: "+str(self.black_num),
                     self.WIDTH/2 - 100, self.HEIGHT/2 + 50)
                text("White: "+str(self.white_num),
                     self.WIDTH/2 - 100, self.HEIGHT/2 + 100)
            elif self.white_wins:
                fill(0, 255, 0)
                textSize(50)
                text("WHITE WINS!!!", self.WIDTH/2 - 140, self.HEIGHT/2)
                text("Black: "+str(self.black_num),
                     self.WIDTH/2 - 100, self.HEIGHT/2 + 50)
                text("White: "+str(self.white_num),
                     self.WIDTH/2 - 100, self.HEIGHT/2 + 100)
            elif self.draw:
                fill(0, 255, 0)
                textSize(50)
                text("DRAW", self.WIDTH/2 - 100, self.HEIGHT/2)
                text("Black: "+str(self.black_num),
                     self.WIDTH/2 - 100, self.HEIGHT/2 + 50)
                text("White: "+str(self.white_num),
                     self.WIDTH/2 - 100, self.HEIGHT/2 + 100)
        elif self.is_skip:
            fill(0, 255, 0)
            textSize(20)
            text("Switch player since there is no valid step.",
                 self.WIDTH/4, self.HEIGHT/4)

    def record_scores(self):
        """record player's score if player wins"""
        # if ((self.PLAYER_COLOR == "black" and self.black_wins) or
        #    (self.PLAYER_COLOR == "white" and self.white_wins)):
        with open(self.FILE_NAME, "r+") as scores:
            record = scores.read()
            if not record:
                if self.PLAYER_COLOR == "black":
                    scores.write(self.PLAYER_NAME + " " +
                                 str(self.black_num) + "\n")
                else:
                    scores.write(self.PLAYER_NAME + " " +
                                 str(self.white_num) + "\n")
            else:
                max_score = int(re.findall(r"^.* (\d*)\n", record)[0])
                if self.PLAYER_COLOR == "black":
                    if self.black_num >= max_score:
                        scores.seek(0)
                        scores.write(self.PLAYER_NAME + " " +
                                     str(self.black_num) + "\n" + record)
                    else:
                        scores.write(self.PLAYER_NAME + " " +
                                     str(self.black_num) + "\n")
                else:
                    if self.white_num >= max_score:
                        scores.seek(0)
                        scores.write(self.PLAYER_NAME + " " +
                                     str(self.white_num) + "\n" + record)
                    else:
                        scores.write(self.PLAYER_NAME + " " +
                                     str(self.white_num) + "\n")
            scores.close()
