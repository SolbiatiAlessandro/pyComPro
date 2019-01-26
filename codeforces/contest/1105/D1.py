"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))


def solve(speeds, matrix, queues, remaining, verbose=False):

    def get_n(x,y):
        cand = [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]
        res = []
        for c in cand:
            if 0 <= c[0] < len(matrix[0]) and\
                0 <= c[1] < len(matrix):
                res.append(c)
        return res

    res = map(len, queues)

    while True:
        progress = 0
        for player, speed in enumerate(speeds):
            for _ in xrange(speed):
                new_queue = []
                for y, x in queues[player]:
                    for cx, cy in get_n(x,y):
                        if matrix[cy][cx] == -1:
                            matrix[cy][cx] = player
                            new_queue.append((cy, cx))
                queues[player] = new_queue
                if len(new_queue) == 0: break
                progress += len(new_queue)
                res[player] += len(new_queue)
        if progress == 0: break

    return res


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    from time import time
    t = time()
    cols, rows, p = stdin()
    speeds = stdin()
    matrix = [[-1 for _ in xrange(rows)] for _ in xrange(cols)]
    queues = [[] for _ in xrange(p)]
    remaining = 0
    for col in xrange(cols):
        row = list(raw_input())
        for i, elem in enumerate(row):
            if elem == '#':
                matrix[col][i] = 0
            elif elem != '.':
                matrix[col][i] = int(elem)
                queues[int(elem) - 1].append((col, i))
            else: remaining += 1
    res = solve(speeds, matrix, queues, remaining, verbose=False)
    for x in res: print x,
