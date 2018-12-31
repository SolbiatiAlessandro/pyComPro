"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

def solve(n):
    p = 998244353
    left, right = [-1 for _ in xrange(n + 1)],[-1 for _ in xrange(n + 1)]
    curr = 1
    for i in xrange(n):
        left[i] = curr * (n - i) % p
        curr = left[i]
    curr = 1
    for i in xrange(1, n + 1):
        right[i] = curr * (i) % p
        curr = right[i]
    res = 0
    #print left, right
    for i in xrange(n-1):
        #print i, left[i], right[n-i-1]
        num = left[i] * (right[n - i-1] - 1)
        #print num
        res += num
    return res + right[-1]  % p

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n = int(raw_input())
    print solve(n)
