class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        def get_n(x,y):
            res = [(x+i,y+j) for i,j in [[1,0],[-1,0],[0,1],[0,-1]]]
            return filter(lambda p: 0 <= p[0] < len(grid[0]) and 0 <= p[1] < len(grid), res)
        
        land = [(i, j) for j, col in enumerate(grid) for i, _ in enumerate(col) if grid[j][i] == '1']
        visited = set()
        land_index, res = 0, 0
        while land:
            queue = [land[land_index]]
            visited.add(queue[0])
            #print land[land_index]
            while queue:
                node = queue.pop()
                for child in get_n(node[0], node[1]):
                   cx, cy = child[0], child[1]
                   if (cx, cy) not in visited and grid[cy][cx] != '0':
                        visited.add((cx, cy))
                        queue.insert(0, (cx, cy))
            res += 1
            while land[land_index] in visited:
                land_index += 1
                if land_index >= len(land): return res
        return 0
