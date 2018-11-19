class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        prev = {}
        def solve(x, y):
            if x == len(grid) or (grid and y == len(grid[0])): return 1e9
            if x == len(grid) - 1 and y == len(grid[0]) - 1: return grid[x][y]
            prev[(x, y)] = min(solve(x + 1, y), solve(x + 1, y + 1), solve(x, y + 1)) 
            return min(solve(x + 1, y), solve(x + 1, y + 1), solve(x, y + 1)) + grid[x][y]
        import pdb;pdb.set_trace()
        res = solve(0, 0)
        return res
