class Board:
    def __init__(self, width, size):
        self.WIDTH = width
        self.SIZE = size
        self.GRID_WIDTH = self.WIDTH / self.SIZE
        self.grids = [[None] * self.SIZE for _ in range(self.SIZE)]

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def put_on(self, i, j, item):
        '''put an item on the grid which (x, y) is at'''
        if not self.grids[i][j]:
            self.grids[i][j] = item
            return True
        return False

    def take_off(self, i, j):
        self.grids[i][j] = None

    def display(self):
        '''draw the board'''
        fill(0, 100, 0)
        rect(0, 0, self.WIDTH, self.WIDTH)
        for i in range(1, self.SIZE):
            line(i*self.GRID_WIDTH, 0, i*self.GRID_WIDTH, self.WIDTH)
            line(0, i*self.GRID_WIDTH, self.WIDTH, i*self.GRID_WIDTH)

    def up_grid(self, i, j):
        '''return the item on the up grid of grid (i, j)'''
        if i == 0:
            return None
        return self.grids[i - 1][j]

    def down_grid(self, i, j):
        '''return the item on the down grid of grid (i, j)'''
        if i == self.SIZE - 1:
            return None
        return self.grids[i + 1][j]

    def left_grid(self, i, j):
        '''return the item on the left grid of grid (i, j)'''
        if j == 0:
            return None
        return self.grids[i][j - 1]

    def right_grid(self, i, j):
        '''return the item on the right grid of grid (i, j)'''
        if j == self.SIZE - 1:
            return None
        return self.grids[i][j + 1]

    def up_left_grid(self, i, j):
        '''return the item on the up-left grid of grid (i, j)'''
        if i == 0 or j == 0:
            return None
        return self.grids[i - 1][j - 1]

    def up_right_grid(self, i, j):
        '''return the item on the up-right grid of grid (i, j)'''
        if i == 0 or j == self.SIZE - 1:
            return None
        return self.grids[i - 1][j + 1]

    def down_left_grid(self, i, j):
        '''return the item on the down-left grid of grid (i, j)'''
        if i == self.SIZE - 1 or j == 0:
            return None
        return self.grids[i + 1][j - 1]

    def down_right_grid(self, i, j):
        '''return the item on the down-right grid of grid (i, j)'''
        if i == self.SIZE - 1 or j == self.SIZE - 1:
            return None
        return self.grids[i + 1][j + 1]
