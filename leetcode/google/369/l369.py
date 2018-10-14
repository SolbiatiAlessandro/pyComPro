colors, children = {}, {}

def clean():
    global colors
    global children
    global dfs_parent
    colors, children = {}, {}

def dfs(vertex):
    colors[vertex] = 0
    _children = children.get(vertex)
    if _children:
        for child in _children:
            if colors.get(child) == 0:
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
        res = None
        for edge in prerequisites:  # build adj list
            parent, child = edge[0], edge[1]
            if parent not in children:
                children[parent] = [child]
            else:
                children[parent].append(child)

        #import pdb;pdb.set_trace()
        for vertex, _ in children.items():
            if vertex not in colors:
                if not dfs(vertex):
                    clean()
                    return False
        clean()
        return True
