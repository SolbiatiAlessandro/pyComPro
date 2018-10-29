from collections import defaultdict

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sources, source_counter = [], 0  # sources = [(x, y, source_index)]
        distances = defaultdict(dict)  # distances[(x, y)][source_index]
        for i, row in enumerate(grid):
            for j, elem in enumerate(row):
                if elem == 1:
                    sources.append((i, j, source_counter))
                    distances[(i, j)][source_counter] = 0
                    source_counter += 1

        res, generation, prev_generation, start_pruning = 1e9, 1, 1e9+1, False
        while sources:
            x, y, index = sources.pop()
            for i, j in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
                query = distances[(i, j)]
                if 0 <= i < len(grid) and\
                   0 <= j < len(grid[0]) and\
                   query.get(index) is None and\
                   grid[i][j] == 0:
                    new_distance = distances[(x, y)][index] + 1
                    if new_distance != generation:
                        generation = new_distance
                        if start_pruning and res >= prev_generation:
                            return res
                        prev_generation = res
                    query[index] = new_distance
                    if len(query) == source_counter:
                        start_pruning = True
                        total_distance = sum([distance for _, distance
                                              in query.items()])
                        res = min(res, total_distance)
                    sources.insert(0, (i, j, index))
        return res if res != 1e9 else -1
