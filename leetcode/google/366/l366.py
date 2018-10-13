"https://leetcode.com/explore/interview/card/google/61/trees-and-graphs/366/"


COLOR = {}
CHILDREN = {}
PARENT = {}

def clean():
    """clean globals"""
    global CHILDREN
    global COLOR
    global PARENT
    CHILDREN = {}
    COLOR = {}
    PARENT = {}

def dfs(vertex, highest_index):
    """dfs to check for cycles
    Args:
        vertex: to be visited
        highest_index: highest_index of the edges visited so far
    Returns:
        highest_index if detects cycles, None otherwise
    """
    if vertex not in COLOR:
        COLOR[vertex] = 0
        if CHILDREN.get(vertex):
            for children, index in CHILDREN[vertex]:
                got = dfs(children, max(highest_index, index))
                if got:
                    return got
        COLOR[vertex] = 1
    elif COLOR[vertex] == 0:
        if highest_index == -1:
            exit('error: highest_index -1')
        return highest_index
    return None


def last_edge_in_cycle():
    """launch dfs on every vertex
    Returns:
        None: if there is no cycles
        edge: edge in the cycle comparing last in edges list
    """
    for vertex, _ in CHILDREN.items():
        if vertex not in COLOR:
            got = dfs(vertex, -1)
            if got:
                return got
    return None


class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        second, first, res = None, None, None  # candidate edges to remove
        for index, edge in enumerate(edges):
            if edge[1] not in PARENT:  # add edge to PARENT dict
                PARENT[edge[1]] = edge[0]
            else:
                second = edge
                first = [PARENT[edge[1]], edge[1]]
            if edge[0] not in CHILDREN:  # add edge to CHILDREN dict
                CHILDREN[edge[0]] = [[edge[1], index]]
            else:
                CHILDREN[edge[0]].append([edge[1], index])

        if first:  # deleting second candidate and check cycles
            for index, child in enumerate(CHILDREN[second[0]]):
                if child[0] == first[1]:
                    del CHILDREN[second[0]][index]
            if last_edge_in_cycle():  # if there is cycle
                res = first
            else:
                res = second
        else:
            res = edges[last_edge_in_cycle()]  # there must be one cycle
        clean()
        return res
