class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        """
        this first iteration checks the first substring of B
        matching the ending string A, it set first as the index
        of the next substring in B
        """
        first = -1
        for cntB in xrange( 0, min( len(A), len(B) ) ):
            matched, cntA, temp = 1, len(A) - 1, cntB
            while( temp>=0 and matched == 1 ):
                if A[cntA] != B[temp]:
                    matched = 0
                cntA-=1
                temp-=1
            if matched:
                first = cntB + 1
        if first==-1:
            return -1

        """
        here we start couting the progressive number of substrings
        starting from first
        """
        res, cntA = 1, len(A) 
        for cntB in xrange( first, len(B) ):
            if cntA >= len(A):
                res+=1
                cntA=0
            if A[cntA]!=B[cntB]:
                return -1
            cntA+=1
        return res
            
