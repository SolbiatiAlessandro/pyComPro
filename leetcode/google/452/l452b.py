class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        res = []
        for diagonal_sum in xrange(len(matrix) + len(matrix[0]) - 1):
            for i in xrange(diagonal_sum + 1):
                j = diagonal_sum - i
                if not diagonal_sum % 2: i, j = j, i
                if i >= len(matrix) or j >= len(matrix[0]): continue
                res.append(matrix[i][j])
        return res
