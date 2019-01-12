"""
this is a standard python template for codeforces task, repo: github.com/solbiatialessandro/pyComPro/codeforces
"""
stdin = lambda type_ = "int", sep = " ": list(map(eval(type_), raw_input().split(sep)))
joint = lambda sep = " ", *args: sep.join(str(i) if type(i) != list else sep.join(map(str, i)) for i in args)
def iters(): return xrange(int(raw_input()))


class SegmentTree(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.max_value = {}
        self.sum_value = {}
        self.len_value = {}
        self._init(start, end)

    def add(self, start, end, weight=1):
        start = max(start, self.start)
        end = min(end, self.end)
        self._add(start, end, weight, self.start, self.end)
        return True

    def query_max(self, start, end):
        return self._query_max(start, end, self.start, self.end)

    def query_sum(self, start, end):
        return self._query_sum(start, end, self.start, self.end)

    def query_len(self, start, end):
        return self._query_len(start, end, self.start, self.end)

    """"""
    def _init(self, start, end):
        self.max_value[(start, end)] = 0
        self.sum_value[(start, end)] = 0
        self.len_value[(start, end)] = 0
        if start < end:
            mid = start + int((end - start) / 2)
            self._init(start, mid)
            self._init(mid+1, end)

    def _add(self, start, end, weight, in_start, in_end):
        key = (in_start, in_end)
        if in_start == in_end:
            self.max_value[key] += weight
            self.sum_value[key] += weight
            self.len_value[key] = 1 if self.sum_value[key] > 0 else 0
            return

        mid = in_start + int((in_end - in_start) / 2)
        if mid >= end:
            self._add(start, end, weight, in_start, mid)
        elif mid+1 <= start:
            self._add(start, end, weight, mid+1, in_end)
        else:
            self._add(start, mid, weight, in_start, mid)
            self._add(mid+1, end, weight, mid+1, in_end)
        self.max_value[key] = max(self.max_value[(in_start, mid)], self.max_value[(mid+1, in_end)])
        self.sum_value[key] = self.sum_value[(in_start, mid)] + self.sum_value[(mid+1, in_end)]
        self.len_value[key] = self.len_value[(in_start, mid)] + self.len_value[(mid+1, in_end)]

    def _query_max(self, start, end, in_start, in_end):
        if start == in_start and end == in_end:
            ans = self.max_value[(start, end)]
        else:
            mid = in_start + int((in_end - in_start) / 2)
            if mid >= end:
                ans = self._query_max(start, end, in_start, mid)
            elif mid+1 <= start:
                ans = self._query_max(start, end, mid+1, in_end)
            else:
                ans = max(self._query_max(start, mid, in_start, mid),
                        self._query_max(mid+1, end, mid+1, in_end))
        #print start, end, in_start, in_end, ans
        return ans

    def _query_sum(self, start, end, in_start, in_end):
        if start == in_start and end == in_end:
            ans = self.sum_value[(start, end)]
        else:
            mid = in_start + int((in_end - in_start) / 2)
            if mid >= end:
                ans = self._query_sum(start, end, in_start, mid)
            elif mid+1 <= start:
                ans = self._query_sum(start, end, mid+1, in_end)
            else:
                ans = self._query_sum(start, mid, in_start, mid) + self._query_sum(mid+1, end, mid+1, in_end)
        return ans

    def _query_len(self, start, end, in_start, in_end):
        if start == in_start and end == in_end:
            ans = self.len_value[(start, end)]
        else:
            mid = in_start + int((in_end - in_start) / 2)
            if mid >= end:
                ans = self._query_len(start, end, in_start, mid)
            elif mid+1 <= start:
                ans = self._query_len(start, end, mid+1, in_end)
            else:
                ans = self._query_len(start, mid, in_start, mid) + self._query_len(mid+1, end, mid+1, in_end)

        #print start, end, in_start, in_end, ans
        return ans

from collections import Counter
def solve(s):
    c  = Counter(s)
    char = '('
    more, less = c['('], c[')']
    if (more - less) != 2: return 0
    counts = []
    count = 0
    st = SegmentTree(0, len(s) - 1)
    for i,cc in enumerate(s):
        if cc == char: count += 1
        else: count -= 1
        if count == -1: return 0
        st.add(i,i,-count)
        counts.append(count)
    if counts[-1] != 2: return 0
    res = 0
    #import pdb;pdb.set_trace()
    for i,cc in enumerate(s):
        if cc == char:
            st.add(i, len(s), 2)
            lowest = st.query_max(i, len(s) - 1)
            if lowest == 0: res += 1
            st.add(i, len(s) - 1, -2)
    return res

if __name__ == "__main__":
    """the solve(*args) structure is needed for testing purporses"""
    s=raw_input()
    s = raw_input()
    print solve(s)
