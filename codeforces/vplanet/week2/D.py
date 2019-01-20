"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))
from operator import mul
MOD = pow(10, 9) + 7

def solve(graph, given):
    memo = [[-1 for _ in xrange(4)] for __ in xrange(len(graph))]
    def dfs(parent, node, color):
        if memo[node][color] != -1: return memo[node][color]
        ans = -1
        if not graph[node]: # is leaf
            if given[node]:
                if given[node] == color: ans = 1
                else: ans = 0
            else:
                ans = 1
        else: # is internal node
            if given[node] and given[node] != color: ans = 0
            else:
                ans = 1
                for child in graph[node]:
                    if child != parent:
                        child_ans = 0
                        for other_color in [1,2,3]:
                            if other_color != color:
                                dfs(node, child, other_color)
                                child_ans += memo[child][other_color]
                        ans *= child_ans
        memo[node][color] = ans % MOD
        return ans
    return (dfs(0, 1, 1) + dfs(0, 1, 2) + dfs(0, 1, 3)) % MOD


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    from collections import defaultdict
    f = open("barnpainting.in","r")
    fileread = lambda : map(int, f.readline()[:-1].split())
    N, C = fileread()
    graph = [[] for _ in xrange(N + 1)]
    for _ in xrange(N - 1):
        i, j  = fileread()
        graph[j].append(i)
        graph[i].append(j)
    given = [None for _ in xrange(N + 1)]
    for _ in xrange(C):
        a, b = fileread()
        given[a] = b
    f.close()

    f = open("barnpainting.out","w")
    ans =solve(graph, given )
    f.write(str(ans))
    f.close()
