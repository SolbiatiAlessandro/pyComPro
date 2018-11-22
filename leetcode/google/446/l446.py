class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.table = [[[0] for _ in xrange(n)] for _ in xrange(n)]
        self.n = n

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        self.table[row][col] = player
        win = [player] * self.n
        if [self.table[i][col] for i in xrange(self.n)] == win: return player
        if self.table[row] == win: return player
        if [self.table[i][i] for i in xrange(self.n)] == win: return player
        if [self.table[self.n - 1 - i][i] for i in xrange(self.n)] == win: return player
        return 0
