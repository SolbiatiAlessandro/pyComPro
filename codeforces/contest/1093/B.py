"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
from collections import Counter
def solve(s):
    c = Counter(s)
    if len(c) == 1: return -1
    res = ""
    for k,v in c.items():
        res += v*k
    return res

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n = int(raw_input())
    for _ in xrange(n):
        s = raw_input()
        print solve(s)
