"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))


def solve(n):

    res = []
    cnt = 0
    while True:
        s = bin(n)[2:][::-1]
        #print s
        done = False
        for i, c in enumerate(s[:-1]):
            if not done and s[i + 1] == '1' and c == '0':
                res.append(i + 1)
                n ^= pow(2, i + 1) - 1
                cnt += 1
                s = bin(n)[2:][::-1]
                if '0' not in s:
                    return res, cnt
                n += 1
                cnt += 1
                done = True
                break
        if done == False:
            return res, cnt
        


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n = int(raw_input())
    res, cnt = solve(n)
    print cnt
    for x in res: print x,
    """
    for x in xrange(0, pow(10, 6) + 1):
        if x % 100001 == 0: print "-"
        #print x
        r = solve(x)
        if len(r) > 20:
            print x
            print("##############")
    #"""

