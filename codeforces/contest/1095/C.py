"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

from collections import Counter
def solve(n, k):
    lower_bound = Counter(bin(n)[2:])['1']
    possible = lower_bound <= k <= n
    if not possible: return []
    res = []
    bb = bin(n)[2:]
    bb = bb[::-1]
    for index, i in enumerate(bb):
        if i == '1': res.append(pow(2, index))
    i = 0
    while len(res) != k:
        while res[i] == 1: i+=1
        res.append(res[i]/2)
        res[i] = res[i]/2
    return res

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n, k = stdin()
    got = solve(n ,k)
    if got:
        print "YES"
        print joint(" ",got)
    else:
        print "NO"
