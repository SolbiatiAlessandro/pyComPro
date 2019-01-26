"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))


def solve(seq):
    if len(seq) > 2:
        return [seq[0], seq[1:]]
    if len(seq) == 2:
        if int(seq[0]) < int(seq[1]): return [seq[0], seq[1]]
        else: return None
    return None


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    for _ in iters():
        raw_input()
        s = raw_input()
        res = solve(s)
        if not res:print "NO"
        else:
            print "YES"
            print 2
            s = ""
            for x in res: s += str(x)+" "
            print s
