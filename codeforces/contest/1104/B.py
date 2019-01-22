"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))


def solve(string):
    res = 0
    stack = ['*']
    for char in string:
        if stack[-1] == char:
            stack.pop()
            res += 1
        else:
            stack.append(char)
    return res

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    s = raw_input()
    res =  solve(s)
    if res % 2 == 1: print "Yes"
    else: print "No"
