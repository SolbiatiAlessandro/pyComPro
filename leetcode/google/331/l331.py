def updateDict( a, b, val, tree ):
    """
    update the dict structure for the tree with 
    :a (char)first node
    :b (char)second node
    :val (float) of the weight
    :tree (dict)
    """
    if tree.get(a) is None:
        tree[a] = {b:val}
    else:
        tree[a][b] = val


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        tree, visited = {}, {}
        for index, equation in enumerate(equations):
            updateDict(equation[0], equation[1], values[index], tree)
            updateDict(equation[1], equation[0], 1/values[index], tree)
            visited[equation[0]], visited[equation[1]] = False, False

        res = []
        for query in queries:
            start, end, val = query[0], query[1], -1.0
            for k in visited.keys():
                visited[k] = False

            queue = [(start, 1)]
            while queue and val == -1.0:
                elem = queue.pop()
                archs = tree.get(elem[0])
                if archs is not None:
                    val = 1.0 if elem[0] == end else -1.0
                    for k, v in archs.items():
                        if k == end:
                            val = elem[1]*v
                        elif not visited[k]:
                            visited[k] = True
                            queue.insert(0, (k, elem[1]*v))
            res.append(round(val,5))

        return res


