"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

def solve(s):
    try:
        start = s.index('[')
        start += s[start:].index(':')
        p = s[::-1]
        end = p.index(']')
        end += p[end:].index(':')
        end = len(s) - 1 - end
    except ValueError: return -1
    from collections import Counter
    if end <= start: return -1
    t = s[start:end]
    c = Counter(t)
    return 4 + c['|']


if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    s=raw_input()
    print solve(s)
