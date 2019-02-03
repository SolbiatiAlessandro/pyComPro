"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
from sys import stdin as _stdin
from sys import stdout
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), _stdin.readline().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))


def solve(string, points):
    for i, point in enumerate(points):
        for j in xrange(i):
            points[i] = max(points[i], points[j] + points[i - j - 1])

    ls = len(string)
    memo_ans = [[-1 for _ in xrange(ls)] for _ in xrange(ls)]
    def ans(l, r):
        if l > r: return 0
        if memo_ans[l][r] != -1:
            return memo_ans[l][r]

        c1, c0 = 0, 0
        for char in string:
            if char == '1': c1 += 1
            else: c0 += 1

        res = 0
        for i in xrange(c1):
            try:
                res = max(res, points[i] + dp(1, l, r, i))
            except:
                print dp(1, l, r, i)
                pass
        for i in xrange(c0):
            res = max(res, points[i] + dp(0, l, r, i))

        memo_ans[l][r] = res
        return res

    def shift_index(index, l, r, digit, places):
        """raise OutOfIndex returns -1"""
        cnt = 0
        while cnt < places:
            if index == r: return -1
            if string[index] == digit:
                cnt += 1
            index += 1
        return index

    memo_dp = [[[[-1 for _ in xrange(ls)] for _ in xrange(ls)] for _ in xrange(ls)] for _ in xrange(2)]
    def dp(dig, l, r, cnt):
        if memo_dp[dig][l][r][cnt] != -1:
            return memo_dp[dig][l][r][cnt] 

        i = l 
        j = shift_index(i, l, r, dig, cnt)

        res = 0
        while j != -1 and j < r:
            curr_dp = ans(l, i) + ans(j, r)

            d, nd = str(dig), str(int(not  1))

            prev = d
            block = 0
            for k in xrange(i, j):
                if string[k] == nd: block += 1
                elif string[k] == d and prev == nd:
                    curr_dp += points[block - 1]
                    block = 0

            i = shift_index(i, l, r, dig, 1)
            j = shift_index(j, l, r, dig, 1)
            res = max(res, curr_dp)

        memo_dp[dig][l][r][cnt] = res
        return res

    return ans(0, ls - 1)
 

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    raw_input()
    s = raw_input()
    w = stdin()
    print solve(s, w)
