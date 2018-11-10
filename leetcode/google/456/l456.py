from collections import defaultdict
from Queue import PriorityQueue


class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        res_list = []
        first_res, second_res = defaultdict(bool), defaultdict(bool)
        order = PriorityQueue()

        for i, row in enumerate(matrix):
            for j, height in enumerate(row):
                order.put((height, (i, j)))

        total = order._qsize()
        for _ in xrange(total):
            first, second = False, False
            visited = defaultdict(int)
            start = order.get()[1] 
            queue = [start]
            while queue and not (first and second):
                i, j = queue.pop()
                height = matrix[i][j]
                visited[(i, j)] = 1
                for x, y in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
                    if x < 0 or y < 0: 
                        first = True
                    elif x == len(matrix) or y == len(matrix[0]):
                        second = True
                    elif not visited[(x, y)] and matrix[x][y] <= height:
                        first, second = max(first_res[(x, y)], first),\
                                        max(second_res[(x, y)], second)
                        queue.insert(0, (x, y))
            first_res[start], second_res[start] = first, second
            if first and second:
                res_list.append(list(start))

        return res_list
