"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))


def solve(s):
    memo = {}
    go = []
    back = []
    prev= "*"
    count = 0
    for c in s[::-1]:
        if c == prev:
            count += 1
            go.append(count + 1)
        else:
            count = 0
            go.append(count + 1)
        prev = c
    prev= "*"
    for c in s:
        if c == prev:
            count += 1
            back.append(count + 1)
        else:
            count = 0
            back.append(count + 1)
        prev = c
    memo = {}
    def ans(start, end, lett):
        if start >= len(go) or end < 0: return 0
        m = memo.get((start, end, lett)) 
        if m is not None:
            return m
        if go[start] >= (end - start):
            memo[(start, end, ord(s[start]))] = 0
            for l in xrange(97, 122):
                if lett != l:
                    memo[(start, end, ord(s[start]))] = 1

        res = 1e9
        lett = s[start]
        for l in xrange(97, 122):
            if ord(lett) != l:
                res = min(res, 1 + ans(start + go[start], end,  l))
            elif ord(lett) == l:
                res = min(res, ans(start + go[start], end, l))

        lett = s[end]
        for l in xrange(97, 122):
            if ord(lett) != l:
                res = min(res, 1 + ans(start, end - back[end],  l))
            elif ord(lett) == l:
                res = min(res, ans(start, end - back[end], l))

        if s[start] == s[end]:
            res = min(res,  ans(start + go[start], end - back[end], l))
        memo[(start, end,lett)] = res
        return res
    r = 1e9
    for l in xrange(97, 122):
        r = min(r, ans(0, len(s) - 1,l))
    return r


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    s = raw_input()
    s = raw_input()
    print solve(s)
