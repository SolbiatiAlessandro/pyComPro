"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

def solve(A, B):
    xB = sorted(B, key=lambda x: -x[0])
    xA = sorted(A, key=lambda x: x[0])
    resx = xB[0][0] + xA[0][0]
    yB = sorted(B, key=lambda x: -x[1])
    yA = sorted(A, key=lambda x: x[1])
    resy = yB[0][1] + yA[0][1]
    return resx, resy

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n = int(raw_input())
    A, B = [], []
    for _ in xrange(n):
        x,y=stdin()
        A.append((x,y))
    for _ in xrange(n):
        x,y=stdin()
        B.append((x,y))
    res = solve(A, B)
    for x in res: print x,
