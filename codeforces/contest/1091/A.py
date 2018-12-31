"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

def solve(y,b,r):
    yy = 0
    if b >= y + 1 and r >= y + 2: yy = y + y + 1 + y + 2
    bb = 0
    if y >= b - 1 and r >= b + 1: bb = b - 1 + b + b + 1
    rr = 0
    if y >= r - 2  and b >= r - 1: rr = r - 2+  r-1 + r
    return max(yy,bb,rr)
    

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n, k, j = stdin()
    print solve(n ,k,j)
