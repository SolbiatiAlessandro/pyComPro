"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))


def different(char):
    if char == 'G': return 'B'
    if char == 'B': return 'G'
    if char == 'R': return 'G'
def other(c1, c2):
    s=set([c1, c2])
    for c in ['G','B','R']:
        if c not in s: return c

def solve(string):
    i = 0
    original = string
    string = list(string)
    res = 0
    while i < len(string):
        k = i + 1
        while  k < len(original) and original[k] == original[i]: k+=1
        l = k - i
        if l % 2 != 0:
            q = i + 1
            while q < len(string) and q < k:
                string[q] = different(string[q])
                res += 1
                q += 2
        else:
            prev = original[i - 1] if i >= 0 else 'K'
            c = other(original[i], prev)
            q = i
            while q < len(string) and q < k:
                string[q] = c
                res += 1
                q += 2
        i = k
    print res
    return ''.join(string)



if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    n = raw_input()
    n = raw_input()
    print solve(n)
