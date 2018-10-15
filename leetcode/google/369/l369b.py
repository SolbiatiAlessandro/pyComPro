parent, rank = [], []

def init(numCourses):
    global parent
    global rank
    parent, rank = [None]*numCourses, [None]*numCourses

def make_set(elem):
    parent[elem] = elem
    rank[elem] = 0

def find_root(elem):
    if elem != parent[elem]:
        parent[elem] = find_root(parent[elem])
    return parent[elem]

def link(first, second):
    if rank[first] > rank[second]:
        parent[second] = first
    else:
        parent[first] = second
        if rank[first] == rank[second]:
            rank[second] += 1

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        init(numCourses)
        for edge in prerequisites:
            first, second = edge[0], edge[1]
            if parent[first] is None:
                make_set(first)
            if parent[second] is None:
                make_set(second)
            first_root = find_root(first)
            second_root = find_root(second)
            if first_root == second_root:
                return False
            link(first_root, second_root)
        return True
