class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        answers = {}
        def solve(x, y):
            if x == len(grid) - 1 and y == len(grid[0]) - 1: return grid[x][y]
            if x == len(grid) or y == len(grid[0]): return 1e9
            if answers.get((x, y)) is None:
                answers[(x, y)] = min(solve(x + 1, y), solve(x, y + 1)) + grid[x][y]
            return answers[(x, y)]
        return solve(0, 0)
