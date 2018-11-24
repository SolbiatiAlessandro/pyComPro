class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.columns = [[0, 0] for _ in xrange(n)]
        self.rows = [[0, 0] for _ in xrange(n)]
        self.first_diagonal = [0, 0]
        self.second_diagonal = [0, 0]
        self.total = n

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
        player -= 1
        self.rows[row][player] += 1
        self.columns[col][player] += 1
        if row == col: self.first_diagonal[player] += 1
        if row == self.total - 1 - col: self.second_diagonal[player] += 1
        if max(self.rows[row]) == self.total: return player + 1
        if max(self.columns[col]) == self.total: return player + 1
        if max(self.first_diagonal) == self.total: return player + 1
        if max(self.second_diagonal) == self.total: return player + 1 
        return 0
