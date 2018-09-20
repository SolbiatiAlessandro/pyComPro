class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        #import pdb;pdb.set_trace()
        counter, res = 0, "" 
        generate = ( char.upper() for char in reversed(S) if char is not '-' )
        for char in generate:
            if counter < K:
                res = char + res
                counter+=1
            else: 
                res = char + '-' + res
                counter = 1
        return res
        
                
                
