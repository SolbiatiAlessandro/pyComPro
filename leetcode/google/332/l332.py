class Solution(object):
    def lengthOfLongestSubstringKDistinct(self,  s,  k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        i, j, d, cnt, res, l = 0, 0, {}, 0, 0, len(s)
        while j < l:
            while j < l:
                e = s[j]
                if d.get(e) is None:
                    d[e] = 1
                    cnt += 1
                    if cnt > k:
                        break
                else:
                    d[e] += 1
                j += 1
            res = max(res, j-i)
            j += 1
            while cnt > k:
                if i > j:
                    return 'error i > j'
                e = s[i]
                d[e] -= 1
                if d[e] == 0:
                    del d[e]
                    cnt -= 1
                i += 1
        return res
