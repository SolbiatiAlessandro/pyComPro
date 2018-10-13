class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        colors, children = {}, {}
        for edge in prerequisites:  # build adj list
            parent, child = edge[0], edge[1]
            if parent not in children:
                children[parent] = [child]
            else:
                children[parent].append(child)

        print children

        for vertex, _ in children.items():  # run dfs
            if vertex not in colors:
                stack = [vertex]
                while stack:
                    parent = stack.pop()
                    colors[parent] = 0
                    _children = children.get(parent)
                    if _children:
                        for child in _children:
                            if colors.get(child) == 0:  # found loop
                                return False
                                #TODO fix: not detecting A->B B->A
                            stack.append(child)
                    colors[parent] = 1
        return True
