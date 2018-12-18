"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def solve(n, k):
    res = ""
    times = n/k
    a = ""
    for i in xrange(k): a+=chr(ord('a')+i)
    for _ in xrange(times): res += a
    for i in xrange(n%k): res += chr(ord('a')+i)
    return res


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    t = int(raw_input())
    for _ in xrange(t):
        n, k = stdin()
        print solve(n ,k)
