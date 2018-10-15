colors, children = [], []

def init(numCourses):
    global colors
    global children
    colors, children = [None]*numCourses, [[]]*numCourses 

def dfs(vertex):
    colors[vertex] = 0
    for child in children[vertex]:
        if colors[child] == 0:
            return False
        if not dfs(child):
            return False
    colors[vertex] = 1
    return True

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        init(numCourses)
        for edge in prerequisites:  # build adj list
            if not children[edge[0]]:
                children[edge[0]] = [edge[1]]
            else:
                children[edge[0]].append(edge[1])
        for vertex in xrange(numCourses):
            if colors[vertex] is None:
                if not dfs(vertex):
                    return False
        return True
