from collections import defaultdict

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        table = defaultdict(list)
        for letter in t:
            table[letter].insert(1, -1)
        table = dict(table)

        not_done = len(t)
        window_start, window_end = -1, 1e9
        for index, letter in enumerate(s):
            if table.get(letter) is not None:
                table[letter].insert(0, index)
                if table[letter].pop() == -1: not_done -= 1
                if not not_done:
                    table_min, table_max = 1e9, index
                    for _, stack in table.items():
                        table_min = min(table_min, stack[-1])
                    if table_max - table_min < window_end - window_start:
                        window_end, window_start = table_max, table_min
        if not_done: return ""
        return s[window_start:window_end+1]
