# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidates = [x for x in xrange(n)]
        while len(candidates) > 1:
            i = candidates.pop()
            j = candidates.pop()
            val = knows(i, j)
            if val: candidates.append(j)
            else: candidates.append(i)
        candidate = candidates[0]
        for i in xrange(n):
            if not knows(i, candidate): return -1
        for j in xrange(n):
            if knows(candidate, j) and j != candidate: return -1
        return candidate
                    
                
        