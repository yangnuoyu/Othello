class Tile:
    def __init__(self, diameter):
        self.DIAMETER = diameter
        self.is_black = True

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def flip(self):
        '''flip the tile'''
        self.is_black = not self.is_black

    def set_black(self):
        self.is_black = True

    def set_white(self):
        self.is_black = False

    def display(self, x, y):
        '''draw the tile'''
        if self.is_black:
            fill(0, 0, 0)
        else:
            fill(255, 255, 255)
        ellipse(x, y, self.DIAMETER, self.DIAMETER)
