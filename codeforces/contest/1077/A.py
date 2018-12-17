"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def solve(a, b, k):
    res = 0
    x = k/2
    res += (a - b)*x
    if k % 2 == 1: res += a
    return res

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    t = int(raw_input())
    for _ in xrange(t):
        a,b,k = stdin()
        print solve(a,b,k)
