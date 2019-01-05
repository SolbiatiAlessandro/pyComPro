"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

from bisect import bisect, bisect_left
from collections import Counter

def sm(seq):
    s, m = 0, 1e9
    for char in seq:
        if char == ")": s -= 1
        else: s += 1
        m = min(m, s)
    return s, m

def solve(seqs):
    vals=[]
    for seq in seqs:
        s,m=sm(seq)
        if m >= 0 or (m < 0 and m >= s): vals.append(s)
    vals = Counter(vals)
    res = vals[0]/2
    if vals:
        for i in xrange(1, max(max(vals), -min(vals)) + 1):
            res += min(vals[i], vals[-i])
    return res


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    seqs = [raw_input() for _ in iters()]
    print solve(seqs)
