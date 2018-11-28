N = int(raw_input())
from math import ceil
from operator import truediv
for _ in xrange(N):
    n, x, y, d = map(int, raw_input().split())
    def solve():
        if not abs(y - x) % d: return abs(y - x)/d
        res = 1e9
        if not (y - 1) % d: res = int(ceil(truediv(x, d))) + (y - 1)/d
        if not (n - y) % d: res = min(res,int(ceil(truediv(n - x, d))) + (n - y)/d)
        return res if res != 1e9 else -1
    print solve()
