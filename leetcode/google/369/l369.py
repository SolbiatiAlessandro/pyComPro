class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        colors = [None for _ in xrange(numCourses)]
        children = [[] for _ in xrange(numCourses)]
        for first, second in prerequisites:  # build adj list
            children[first].append(second)

        def dfs(vertex):
            if colors[vertex] == 0:
                return False
            if colors[vertex] == 1:
                return True
            colors[vertex] = 0
            for child in children[vertex]:
                if not dfs(child):
                    return False
            colors[vertex] = 1
            return True

        for vertex in xrange(numCourses):
            if not dfs(vertex):
                return False

        return True
