"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))
from operator import truediv

def hack00(n, k, m, pows):
    pows = sorted(pows, reverse=True) 

    ans = 0
    temp = 0
    for i in xrange(1, n + 1):
        x = pows[i - 1]
        temp += x

        val = m
        val -= n - i
        if val < 0: break
        val = min(val, i*k)
        y = float(temp + val)
        ans = max(ans, truediv(y, i))
    return ans


def solve(n, k, m, pows):
    pows = sorted(pows, reverse=True) 
    to_delete = len(pows) - 1
    can_increase = min(k, m - to_delete)
    increase = pows[0] + can_increase
    return increase
    """i = 0
    cumsum = 0
    prev_res = 0
    while i < len(pows):
        to_delete = len(pows) - 1 - i
        can_increase = min(k, m - to_delete)
        increase = pows[i] + can_increase
        new_res = truediv(( increase + cumsum ), i + 1)
        if new_res > prev_res:
            m -= can_increase
            prev_res = new_res
            cumsum += increase
            i += 1
        else:
            return prev_res
    return prev_res"""


def generate():
   from random import random as rd 
   k = int(rd()*pow(10, 5)) + 1
   m = int(rd()*pow(10, 7)) + 1
   n = int(rd()*pow(10, 5)) + 1
   pows = [ rd()*pow(10, 6) for _ in xrange(n) ]
   print k,m,n
   try:
       assert solve(n,k,m,pows) == hack00(n,k,m,pows)
   except:
       print solve(n,k,m,pows)
       print hack00(n,k,m,pows)
       print k,m,n, pows
       exit("bug")


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n, k, m = stdin()
    pows = stdin()
    print solve(n ,k, m, pows)
    print hack00(n ,k, m, pows)
    #for _ in xrange(1000):
        #generate()
