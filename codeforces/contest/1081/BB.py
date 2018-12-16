from collections import Counter
def solve():
    n = int(raw_input())
    nums = map(int, raw_input().split())
    c = Counter(nums)
    for k, v in c.items():
        if (n - v) != k:
            print "Impossible"
            return
    print "Possible"
    for x in nums: print x + 1,
    return
solve()
