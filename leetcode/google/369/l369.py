from collections import defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        colors = [None] * numCourses
        children = defaultdict(list)
        for first, second in prerequisites:  # build adj list
            children[first].append(second)

        def dfs(vertex):
            if colors[vertex] == 0: return False
            if colors[vertex] == 1: return True
            colors[vertex] = 0
            if any(not dfs(child) for child in children[vertex]): return False
            colors[vertex] = 1
            return True

        return all(dfs(vertex) for vertex in xrange(numCourses))
