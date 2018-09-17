class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        #import pdb;pdb.set_trace() 
        lowerBound = len(B)/len(A)
        for i in xrange(0,3):
            if B in A*(lowerBound+i):
                return lowerBound+i
        return -1
