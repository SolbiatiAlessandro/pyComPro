"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))


def solve(speeds, matrix, sources, verbose=False):

    res = [0 for _ in speeds]

    def get_n(x,y):
        #TODO:test
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
    high_queue = sources[::-1] #player, (x,y)
    while high_queue:
        source = high_queue.pop()
        player = source[0]
        res[player - 1] += 1
        #print player, source
        x, y = source[1][0], source[1][1]
        speed = speeds[player - 1]
        high_children = []

        low_queue = [(0, (x,y))] #dist, (x,y) 
        if verbose: print "start low_queue for player {}, speed {}, in {}".format(player, speed, (x,y))
        while low_queue: # expand speed
            elem = low_queue.pop()
            #res[player - 1] += 1
            #print "- [{}] {}".format(player, elem)
            dist = elem[0]
            x, y = elem[1][0], elem[1][1]
            if verbose: print "-low queue"
            if verbose: print (x,y)
            children = get_n(x,y)
            if verbose: print "get_n({})".format((x,y))
            if verbose: print ">>>"
            if verbose: print children
            for child in children:
                cx, cy = child[0], child[1]
                if matrix[cy][cx] == -1:
                    matrix[cy][cx] = player
                    if dist + 1 < speed:
                        low_queue.insert(0, [dist + 1, child]) 
                    else: # border
                        high_queue.insert(0, [player, (cx,cy)])
        if verbose: print "got high_children "
        if verbose: print high_children


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
                sources.append([int(elem), (i,col)])
    sources.sort()
    res = solve(speeds, matrix, sources, verbose=False)
    for x in res: print x,
    print time() - t
