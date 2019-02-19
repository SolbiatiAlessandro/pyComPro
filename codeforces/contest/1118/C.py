"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))


def solve(n, a):
    if n == 1:
        return [a]
    from collections import Counter
    c = Counter(a)
    keys = c.keys()
    vals = c.values()
    center = None
    freq = []
    reduced2, reduced4 = [], []
    for k, v in c.items():
        if v % 2 == 1:
            if center is not None: return "NO"
            v -= 1
            center = k
        if v > 0:
            freq.append([v, k])
    freq.sort(reverse=True)
    while freq:
        frequency, number = freq[-1]
        if frequency % 4 == 0:
            reduced4.append(number)
            freq[-1][0] -= 4
        elif frequency % 2 == 0:
            reduced2.append(number)
            freq[-1][0] -= 2
        else: 
            return "NO"
        if freq[-1][0] == 0: freq.pop()
        
    if n % 2 == 0 and reduced2: return "NO"

    m = (n) / 2
    small = [['*' for _ in range(m)]for _ in range(m)]
    for row in xrange(m):
        for col in xrange(m):
            if not reduced4: return "NO"
            small[row][col] = reduced4.pop()
    for num in reduced4:
        reduced2.append(num)
        reduced2.append(num)

    res = []
    if n % 2 == 0:
        for row in small:
            res.append(row + row[::-1])
        res = res + res[::-1]
    else:
        for row in small:
            if not reduced2: return "NO"
            res.append(row + [reduced2.pop()] + row[::-1])
        central_row = reduced2 + [center] + reduced2[::-1]
        res = res + [central_row] + res[::-1]
    return res

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n = int(raw_input())
    a= stdin()
    got =  solve(n ,a)
    if got == "NO": print got
    else:
        print "YES"
        for i, row in enumerate(got):
            s = ""
            for num in row:
                s +=  str(num) + " "
            print s
