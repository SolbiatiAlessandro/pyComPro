from collections import defaultdict
from Queue import PriorityQueue


class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        res_list = []
        res = dict()
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
                for x, y in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
                    if x < 0 or y < 0: 
                        first = True
                    elif x == len(matrix) or y == len(matrix[0]):
                        second = True
                    elif res.get((x, y)) is not None:
                        child_first, child_second = res[(x, y)]
                        if child_first == True: first = True
                        if child_second == True: second = True
                    elif res.get((x, y)) is None and \
                            not visited[(x, y)] and\
                            matrix[x][y] <= height:
                        visited[(x, y)] = 1
                        queue.insert(0, (x, y))
            res[start] = first, second 
            if first and second:
                res_list.append(list(start))

        return res_list
