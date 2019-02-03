"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))


def solve(s1, s2):
    vowels = set(['a','e','i','o','u'])
    c1, c2 = "", ""
    for char in s1:
        if char in vowels: c1 += 'a'
        else: c1 += 'b'
    for char in s2:
        if char in vowels: c2 += 'a'
        else: c2 += 'b'
    return c1 == c2
    

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    s1, s2 = raw_input(), raw_input()
    res= solve(s1, s2)
    if res: print "Yes"
    else: print "No"
