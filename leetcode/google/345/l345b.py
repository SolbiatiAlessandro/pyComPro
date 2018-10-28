from collections import defaultdict

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_letters, s_letters = defaultdict(int), defaultdict(int)
        for letter in t: t_letters[letter] += 1
        t_letters = dict(t_letters)

        complete, trail = 0, list()
        i, start, end = 0, -1, int(1e9)

        for index, letter in enumerate(s):
            if t_letters.get(letter) is not None:
                if t_letters[letter] > s_letters[letter]: complete +=1 
                s_letters[letter] += 1
                trail.append(index)
                while i < len(trail) and s_letters[s[trail[i]]] > t_letters[s[trail[i]]]:
                    s_letters[s[trail[i]]] -= 1
                    i += 1
                if complete == len(t) and index - trail[i] < end - start:
                    end, start = index, trail[i]

        return s[start:end + 1] if start != -1 else ""
