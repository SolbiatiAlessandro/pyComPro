from pprint import pprint as pp 
from collections import Counter
from operator import __add__
from copy import deepcopy

class ufds(object):
    """class for union find disjoint set
    
    ufds(grid) grid is list[list[str]] with '1' or '0'
    according to problem statement
    """
    def __init__(self, grid, debug=True):
        self.grid = deepcopy(grid)
        self.rank = deepcopy(grid)
        for j, col in enumerate(grid):
            for i, row in enumerate(col):
                if row == "1":
                    self.grid[j][i] = (j, i)
                    self.rank[j][i] = 0
                else:
                    self.grid[j][i] = None
                    self.rank[j][i] = -1

    def join_set(self, x, y, xx, yy, debug=True):
        """given two pairs of x, y join set"""
        if debug:
            pp(locals())
        if x == 0 and xx == 0 and y == 1 and yy == 0:
            #import pdb;pdb.set_trace()
            pass
        self.grid[yy][xx] = self.grid[y][x]

    def find_set(self, x, y, debug=True):
        """find set given a pairs of x, y"""
        if self.grid[y][x] != (y, x):
            return self.find_set(self.grid[y][x][1], self.grid[y][x][0], debug=debug)
        return (y, x)

    def count_set(self, debug=True):
        """returns how many different sets are in grid"""
        counter = Counter(reduce(__add__, self.grid))
        del counter[None]
        return len(counter)


if __name__ == "__main__":
    inp = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    sets = ufds(inp)
    for j, col in enumerate(inp):
        for i, row in enumerate(col[1:]):
            if row == "1" and col[i] == "1":
                sets.join_set(i, j, i + 1, j, debug=False)

    for i in xrange(len(inp[0])): 
        for j  in xrange(1, len(inp)):
            if inp[j - 1][i] == "1" and inp[j][i] == "1":
                sets.join_set(i, j - 1, i, j, debug=False)
    pp(sets.grid)
    assert sets.count_set(debug=False) == 1
