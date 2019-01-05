"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))


def solve(n, k):
    a,b=n[0],n[1]
    for kk in k:
        if kk[0] == a: return True
        if kk[1] == b: return True
    return False

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n = raw_input()
    k = raw_input().split()
    if solve(n ,k): print "YES"
    else: print "NO"
