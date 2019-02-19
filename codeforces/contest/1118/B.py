"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

def solve(a):
    if len(a) == 1: return 1
    even, odd = [0], [0]
    for i, num in enumerate(a):
        if  i % 2 == 0:
            even.append(even[-1] + num)
        else:
            odd.append(odd[-1] + num)
    even, odd = even[1:], odd[1:]
    res = 0
    for i, num in enumerate(a):
        if i % 2 == 0:
            ce = even[i / 2]
            co = None
            pe = even[i / 2 - 1]  if i > 0 else 0
            po = odd[i / 2 - 1] if (i / 2) > 0  else 0
            e = pe + odd[-1] - po 
            o = po + even[-1] - ce
        else:
            co = odd[i / 2]
            ce = None
            pe = even[i / 2]
            po = odd[(i / 2) - 1] if i > 1 else 0
            o = po + even[-1] - pe
            e = pe + odd[-1] - co
        res += e == o
    return res





if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    raw_input()
    a= stdin()
    print solve(a)
