class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix: return []
        def bfs(queue, visited):
            while queue:
                i, j = queue.pop()
                height = matrix[i][j]
                for x, y in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
                    if 0 <= x < len(matrix) \
                       and 0 <= y < len(matrix[0]) \
                       and matrix[x][y] >= height \
                       and visited.get((x, y)) is None:
                        visited[(x, y)] = 1
                        queue.append((x, y))

        first, second = dict(), dict()
        
        first_queue, second_queue = [], []
        for y in xrange(len(matrix[0])):
            first[(0, y)] = 1
            second[(len(matrix) - 1, y)] = 1
            first_queue.append((0, y))
            second_queue.append((len(matrix) - 1, y))
        for x in xrange(len(matrix)):
            first[(x, 0)] = 1
            second[(x, len(matrix[0]) - 1)] = 1
            first_queue.append((x, 0))
            second_queue.append((x, len(matrix[0]) - 1))
        bfs(first_queue, first)
        bfs(second_queue, second)
        
        return [list(key) for key in first.keys() if key in second]
