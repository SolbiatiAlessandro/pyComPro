class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        direction, x, y = 1, 0, 0
        res = [matrix[y][x]] if matrix else []
        while matrix and not (x == len(matrix[0]) - 1
                              and y == len(matrix) - 1):
            if direction:
                if x == len(matrix[0]) - 1: y += 1
                elif y == 0: x += 1
                else:
                    x += 1; y -= 1
                    direction = not direction
            else:
                if y == len(matrix[0]) - 1: x += 1
                elif x == 0: y += 1
                else: 
                    y += 1; x -= 1
                    direction = not direction
            direction = not direction
            res.append(matrix[y][x])
        return res
