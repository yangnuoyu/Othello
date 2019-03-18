from board import Board
from tile import Tile
from game_controller import GameController
from record import Record


class Othello:
    def __init__(self, board_width, game_size, player_name, player_color):
        '''
        Initializing the game with class Board, and class GameController
        '''
        self.board = Board(board_width, game_size)
        self.tiles = [Tile(board_width / game_size)
                      for _ in range(game_size ** 2)]
        self.gc = GameController(board_width, board_width,
                                 player_name, player_color)

        tile = self.tiles.pop()
        tile.set_white()
        self.board.grids[game_size//2 - 1][game_size//2 - 1] = tile

        tile = self.tiles.pop()
        tile.set_black()
        self.board.grids[game_size // 2][game_size//2 - 1] = tile

        tile = self.tiles.pop()
        tile.set_black()
        self.board.grids[game_size//2 - 1][game_size // 2] = tile

        tile = self.tiles.pop()
        tile.set_white()
        self.board.grids[game_size // 2][game_size // 2] = tile

        self.valid_grids = set({})
        self.is_black = True
        # self.game_start()
        # self.skip_times = 0
        self.is_control = False
        # self.game_finished = False

    # def game_start(self):
    #     '''put 4 tiles in the middle of the board'''

    def update_info(self):
        if self.gc.is_finished:
            return
        self.update_legal_move()
        self.skip_or_finish()
        if self.gc.is_finished:
            self.judge_game()
            self.gc.record_scores()
        self.gc.is_black = self.is_black
        self.is_control = False

    def display(self):
        '''show game on the screen'''
        self.board.display()
        for i in range(self.board.SIZE):
            for j in range(self.board.SIZE):
                if isinstance(self.board.grids[i][j], Tile):
                    self.board.grids[i][j].display(
                        (j+0.5) * self.board.GRID_WIDTH,
                        (i+0.5) * self.board.GRID_WIDTH)
        self.gc.display()

    def game_AI(self):
        '''AI of the game with greedy strategy'''
        if self.gc.is_finished:
            return
        if (self.gc.PLAYER_COLOR == "black" and not self.is_black or
           self.gc.PLAYER_COLOR == "white" and self.is_black):
            flip = {(i, j): sum(self.board.grids[i][j].record.values())
                    for i, j in self.valid_grids}
            best = {n for n in flip if flip[n] == max(flip.values())}
            if len(best) != 0:
                m, n = best.pop()
                self.control(m, n)

    def control(self, i, j):
        '''make a legal move and flip the tiles'''
        if isinstance(self.board.grids[i][j], Record):
            rec = self.board.grids[i][j]
            self.put_tile_on(i, j)
            for d in rec.record:
                self.flip(i, j, d, rec.record[d])
            self.is_black = not self.is_black
            self.is_control = True

    def update_legal_move(self):
        '''find out all legal moves'''
        valid_grids = set({})
        for i in range(self.board.SIZE):
            for j in range(self.board.SIZE):
                if isinstance(self.board.grids[i][j], Record):
                    self.board.take_off(i, j)
                if not isinstance(self.board.grids[i][j], Tile):
                    # up
                    if (isinstance(self.board.up_grid(i, j), Tile) and
                       self.board.up_grid(i, j).is_black
                       is not self.is_black):
                        k = i - 1
                        l = j
                        count = 0
                        while isinstance(self.board.up_grid(k, l), Tile):
                            count += 1
                            if (self.board.up_grid(k, l).is_black
                               is self.is_black):
                                self.board.put_on(i, j, Record())
                                self.board.grids[i][j].update("u", count)
                                valid_grids.add((i, j))
                                break
                            k -= 1

                    # down
                    if (isinstance(self.board.down_grid(i, j), Tile) and
                       self.board.down_grid(i, j).is_black
                       is not self.is_black):
                        k = i + 1
                        l = j
                        count = 0
                        while isinstance(self.board.down_grid(k, l), Tile):
                            count += 1
                            if (self.board.down_grid(k, l).is_black
                               is self.is_black):
                                if not isinstance(self.board.grids[i][j],
                                                  Record):
                                    self.board.put_on(i, j, Record())
                                self.board.grids[i][j].update("d", count)
                                valid_grids.add((i, j))
                                break
                            k += 1

                    # left
                    if (isinstance(self.board.left_grid(i, j), Tile) and
                       self.board.left_grid(i, j).is_black
                       is not self.is_black):
                        k = i
                        l = j - 1
                        count = 0
                        while isinstance(self.board.left_grid(k, l), Tile):
                            count += 1
                            if (self.board.left_grid(k, l).is_black
                               is self.is_black):
                                if not isinstance(self.board.grids[i][j],
                                                  Record):
                                    self.board.put_on(i, j, Record())
                                self.board.grids[i][j].update("l", count)
                                valid_grids.add((i, j))
                                break
                            l -= 1

                    # right
                    if (isinstance(self.board.right_grid(i, j), Tile) and
                       self.board.right_grid(i, j).is_black
                       is not self.is_black):
                        k = i
                        l = j + 1
                        count = 0
                        while isinstance(self.board.right_grid(k, l), Tile):
                            count += 1
                            if (self.board.right_grid(k, l).is_black
                               is self.is_black):
                                if not isinstance(self.board.grids[i][j],
                                                  Record):
                                    self.board.put_on(i, j, Record())
                                self.board.grids[i][j].update("r", count)
                                valid_grids.add((i, j))
                                break
                            l += 1

                    # up-left
                    if (isinstance(self.board.up_left_grid(i, j), Tile) and
                       self.board.up_left_grid(i, j).is_black
                       is not self.is_black):
                        k = i - 1
                        l = j - 1
                        count = 0
                        while isinstance(self.board.up_left_grid(k, l), Tile):
                            count += 1
                            if (self.board.up_left_grid(k, l).is_black
                               is self.is_black):
                                if not isinstance(self.board.grids[i][j],
                                                  Record):
                                    self.board.put_on(i, j, Record())
                                self.board.grids[i][j].update("ul", count)
                                valid_grids.add((i, j))
                                break
                            k -= 1
                            l -= 1

                    # up-right
                    if (isinstance(self.board.up_right_grid(i, j), Tile) and
                       self.board.up_right_grid(i, j).is_black
                       is not self.is_black):
                        k = i - 1
                        l = j + 1
                        count = 0
                        while isinstance(self.board.up_right_grid(k, l), Tile):
                            count += 1
                            if (self.board.up_right_grid(k, l).is_black
                               is self.is_black):
                                if not isinstance(self.board.grids[i][j],
                                                  Record):
                                    self.board.put_on(i, j, Record())
                                self.board.grids[i][j].update("ur", count)
                                valid_grids.add((i, j))
                                break
                            k -= 1
                            l += 1

                    # down-left
                    if (isinstance(self.board.down_left_grid(i, j), Tile) and
                       self.board.down_left_grid(i, j).is_black
                       is not self.is_black):
                        k = i + 1
                        l = j - 1
                        count = 0
                        while isinstance(self.board.down_left_grid(k, l),
                                         Tile):
                            count += 1
                            if (self.board.down_left_grid(k, l).is_black
                               is self.is_black):
                                if not isinstance(self.board.grids[i][j],
                                                  Record):
                                    self.board.put_on(i, j, Record())
                                self.board.grids[i][j].update("dl", count)
                                valid_grids.add((i, j))
                                break
                            k += 1
                            l -= 1

                    # down-right
                    if (isinstance(self.board.down_right_grid(i, j),
                                   Tile) and
                       self.board.down_right_grid(i, j).is_black
                       is not self.is_black):
                        k = i + 1
                        l = j + 1
                        count = 0
                        while isinstance(self.board.down_right_grid(k, l),
                                         Tile):
                            count += 1
                            if (self.board.down_right_grid(k, l).is_black
                               is self.is_black):
                                if not isinstance(self.board.grids[i][j],
                                                  Record):
                                    self.board.put_on(i, j, Record())
                                self.board.grids[i][j].update("dr", count)
                                valid_grids.add((i, j))
                                break
                            k += 1
                            l += 1
        self.valid_grids = valid_grids

    def put_tile_on(self, i, j):
        '''put tile on the board'''
        tile = self.tiles.pop()
        if self.is_black:
            tile.set_black()
        else:
            tile.set_white()
        self.board.take_off(i, j)
        self.board.put_on(i, j, tile)

    def flip(self, i, j, dir, steps):
        '''flip the tiles after making a move'''
        assert dir in ['u', 'd', 'l', 'r', 'ul', 'ur', 'dl', 'dr']
        if dir == "u":
            for step in range(1, steps + 1):
                self.board.grids[i - step][j].flip()
        elif dir == "d":
            for step in range(1, steps + 1):
                self.board.grids[i + step][j].flip()
        elif dir == "l":
            for step in range(1, steps + 1):
                self.board.grids[i][j - step].flip()
        elif dir == "r":
            for step in range(1, steps + 1):
                self.board.grids[i][j + step].flip()
        elif dir == "ul":
            for step in range(1, steps + 1):
                self.board.grids[i - step][j - step].flip()
        elif dir == "ur":
            for step in range(1, steps + 1):
                self.board.grids[i - step][j + step].flip()
        elif dir == "dl":
            for step in range(1, steps + 1):
                self.board.grids[i + step][j - step].flip()
        elif dir == "dr":
            for step in range(1, steps + 1):
                self.board.grids[i + step][j + step].flip()

    # def skip_if_need(self):
    #     '''skip this turn if there is no legal move'''
    #     if not self.game_finished:
    #         if len(self.valid_grids) == 0:
    #             self.gc.is_skip = True
    #             self.skip_times += 1
    #             self.is_black = not self.is_black
    #         else:
    #             self.skip_times = 0
    #             if self.is_control is True:
    #                 self.gc.is_skip = False

    def skip_or_finish(self):
        '''make sure the game is finished'''
        if self.tiles == []:
            self.gc.is_finished = True
            return
        if len(self.valid_grids) == 0:
            self.is_black = not self.is_black
            self.update_legal_move()
            if len(self.valid_grids) == 0:
                self.gc.is_finished
            else:
                self.gc.is_skip = True
        elif self.is_control:
            self.gc.is_skip = False
        # elif self.skip_times == 2:
        #     return True
        # elif (all(n.is_black for n in sum(self.board.grids, [])
        #           if isinstance(n, Tile)) or
        #       all(not n.is_black for n in sum(self.board.grids, [])
        #           if isinstance(n, Tile))):
        #     return True
        # return False

    def judge_game(self):
        '''judge the game'''
        tiles = [t for t in sum(self.board.grids, []) if isinstance(t, Tile)]
        self.gc.white_num = sum(1 for tile in tiles if not tile.is_black)
        self.gc.black_num = sum(1 for tile in tiles if tile.is_black)
        if self.gc.white_num > self.gc.black_num:
            self.gc.white_wins = True
            self.gc.black_wins = False
            self.gc.draw = False
        elif self.gc.white_num < self.gc.black_num:
            self.gc.black_wins = True
            self.gc.white_wins = False
            self.gc.draw = False
        else:
            self.gc.draw = True
            self.gc.white_wins = False
            self.gc.black_wins = False
