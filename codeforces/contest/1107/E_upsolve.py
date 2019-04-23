"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))

def solve(string, points):
    memo = [[-1 for _ in range(len(string))] for _ in range(len(string))]
    def dp(start, end):
        print(start, end)
        if start == len(string) or start > end: return 0
        if memo[start][end] != -1: return memo[start][end]
        count = 0
        res = points[count] + dp(start + 1, end)
        prev = start
        cumsum = 0
        for i in xrange(start + 1, end + 1):
            if string[i] == string[start]:
                count += 1
                cumsum += dp(prev + 1, i - 1)
                res = max(res, points[count] + cumsum)
                prev = i
        memo[start][end] = res
        return res
    return dp(0, len(string) - 1)

 

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    raw_input()
    s = raw_input()
    w = stdin()
    print solve(s, w)
