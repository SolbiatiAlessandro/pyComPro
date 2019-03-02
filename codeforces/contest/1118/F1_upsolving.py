"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

def solve(colors, edge_list):
    br = []
    for color in colors:
        triple = [0, 0, 0]
        triple[color] += 1
        br.append(triple)

    def traverse(node, parent):
        for child in edge_list[node]:
            if child != parent:
                traverse(child, node)
                br[node][1] += br[child][1]
                br[node][2] += br[child][2]
    traverse(0, -1)

    res = 0
    for node in xrange(1, len(colors)):
        first_subtree = (br[0][1] - br[node][1], br[0][2] - br[node][2])
        second_subtree = (br[node][1], br[node][2])
        if not(0 not in first_subtree or 0 not in second_subtree):
            res += 1

    return res
    

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n = int(raw_input())
    colors = stdin()
    edge_list = [[] for _ in xrange(n)]
    for _ in xrange(n - 1):
        a, b = stdin()
        edge_list[a-1].append(b-1)
        edge_list[b-1].append(a-1)
    print solve(colors, edge_list)
