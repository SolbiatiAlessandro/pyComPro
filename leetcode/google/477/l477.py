class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.original_matrix = [[x for x in row] for row in matrix]
        for i in xrange(1, len(matrix)): matrix[i][0] += matrix[i - 1][0]
        for i in xrange(1, len(matrix[0])): matrix[0][i] += matrix[0][i - 1]
        for i in xrange(1, len(matrix)):
            for j in xrange(1, len(matrix[0])):
                matrix[i][j] += matrix[i-1][j] + matrix[i][j - 1] - matrix[i - 1][j - 1]
        self.matrix = matrix
        self.updates = [[] for _ in xrange(len(matrix))]
        
    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        self.updates[row].insert(col, val - self.original_matrix[row][col])
        print self.updates
        
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        row1 -= 1
        col1 -= 1
        delta = 0
        for row in xrange(row1 + 1, row2 + 1):
            for update in self.updates[row]:
                if col1 < update[0] <= col2: delta += update[1]
        return self.matrix[row2][col2] - self.matrix[row1][col2] - self.matrix[row2][col1] + self.matrix[row1][col1] + delta
