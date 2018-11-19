class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def ok(x, y): return 0 <= x < len(grid) and 0 <= y < len(grid[0])
        def grid_get(x, y): return grid[x][y] if ok(x, y) else 1e9
        for diagonal in reversed(xrange((len(grid) - 1) + len(grid[0]) - 1)):
            for y in xrange(len(grid[0])):
                x = diagonal - y
                if ok(x, y): grid[x][y] += min(grid_get(x + 1, y), grid_get(x, y + 1))
        return grid[0][0]
