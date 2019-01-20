"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))
from collections import deque, defaultdict


def solve(speeds, matrix, sources, verbose=False):

    res = [0 for _ in speeds]

    def get_children(x,y):
        cand = [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]
        res = []
        for c in cand:
            if 0 <= c[0] < len(matrix[0]) and\
                0 <= c[1] < len(matrix):
                res.append(c)
        return res

    if verbose: print speeds, matrix, 
    if verbose: print "sources"
    if verbose: print sources

    queue = deque()
    for source in sources[::-1]:
        queue.append(source)

    for player, _, _, _ in sources:
        res[player - 1] += 1

    while queue:
        player, x, y, distance = queue.pop()
        if verbose: print player, x, y, distance
        for child in get_children(x,y):
            cy,cx=child[1],child[0]
            if matrix[cy][cx] == -1:
                matrix[cy][cx] = player
                res[player - 1] += 1
                if verbose: print player
                if distance == speeds[player - 1]:
                    queue.appendleft((player, cx, cy, 1))
                elif distance < speeds[player - 1]:
                    queue.append((player,cx,cy,distance + 1))


    return res
    
                

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    from time import time
    t = time()
    cols, rows, p = stdin()
    speeds = stdin()
    matrix = [[-1 for _ in xrange(rows)] for _ in xrange(cols)]
    sources = []
    for col in xrange(cols):
        row = list(raw_input())
        for i, elem in enumerate(row):
            if elem == '#':
                matrix[col][i] = 0
            elif elem != '.':
                matrix[col][i] = int(elem)
                sources.append([int(elem), i, col, 1])
    sources.sort()
    res = solve(speeds, matrix, sources, verbose=False)
    for x in res: print x,
    #print time() - t
