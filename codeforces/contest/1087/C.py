"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

def solve(points):
    A, B, C = points
    def dist(X,Y): return abs(Y[0]-X[0]) + abs(Y[1] -X[1])
    def p(X): print(X[0], X[1])
    def r(A,B,C):
        print "point"
        p(A)
        close, far = B, C
        if dist(A,C) < dist(A,B): close, far = C, B
        print "closest"
        p(close)

        down = True
        path1,path2 = (A[0],close[1]), (close[0],A[1])
        path = None
        if dist(path1, far) < dist(path2, far): path = path1
        else: path = path2
        print "path"
        p(path)

        path_points = []
        for i in xrange(A[1],close[1]+1):
            if path == path1:
                path_points += [(A[0],i)]
            else:
                path_points += [(close[0],i)]
        for i in xrange(A[0],close[0]+1):
            if path == path1:
                path_points +=  [(i,close[1])]
            else:
                path_points +=  [(i,A[1])]
        print "path_points"
        print path_points
        for point in path_points: p(point)

        closest2 = None
        mind = 1e9
        print "far"
        print p(far)
        for point in path_points:
            print "point dist"
            print p(point)
            print dist(far, point)
            if dist(far, point) < mind:
                closest2 = point
                mind = dist(far, point)

        print "closest2"
        p(closest2)
        path_points2 = []
        for i in xrange(min(far[1],closest2[1]), max(far[1],closest2[1])+1):
            path_points2 += [(far[0],i)]
        for i in xrange(min(far[0],closest2[0]), max(far[0],closest2[0])+1):
            path_points2 += [(i,far[1])]
        print "path_points2"
        print path_points2
        for point in path_points2: p(point)

        tot_path = set(path_points2 + path_points)
        print "Res------"
        print len(tot_path)
        return tot_path

    res = r(A,B,C)
    """
    t = r(B,C,A)
    if len(t) < len(res):
        res = t
    t = r(C,B,A)
    if len(t) < len(res):
        res = t
        """
    print len(res)
    for point in res: p(point)






if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    x1,y1 = stdin()
    x2,y2 = stdin()
    x3,y3 = stdin()
    print solve([(x1,y1),(x2,y2),(x3,y3)])
