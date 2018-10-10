"""robot class implementation for test mocking"""


class Robot(object):
    """robot implementation to test solution
    Args:
        x : (int) x position
        y : (int) y position
        orientation : (int) orientation [0,1,2,3] up right down left
        grid : [int][int] original graph
        cleaned : [int][int] to keep track of cleaned
    """
    def __init__(self, x, y, grid):
        self.x = x
        self.y = y
        self.grid = grid
        self.cleaned = grid
        self.orientation = 0

    def _debug(self):
        for d in dir(self):
            print getattr(self, d)

    def clean(self):
        self.cleaned[self.x][self.y] = 'C'

    def turnRight(self):
        self.orientation = (self.orientation + 1) % 4

    def turnLeft(self):
        self.orientation = (self.orientation - 1) % 4

    def move(self):
        to_x = self.x
        to_y = self.y
        if self.orientation == 1:
            to_y += 1
        elif self.orientation == 2:
            to_x += 1
        elif self.orientation == 3:
            to_y -= 1
        elif self.orientation == 0:
            to_x -= 1

        if to_x < 0 or \
           to_x >= len(self.grid) or \
           to_y < 0 or \
           to_y >= len(self.grid[0]) \
           or self.grid[to_x][to_y] == 0:
            return 0
        self.x = to_x
        self.y = to_y
        return 1
