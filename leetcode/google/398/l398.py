class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        res = 0
        if len(s) == len(t):
            for i, c in enumerate(s):
                if c != t[i]:
                    if not res:
                        res = 1
                    else:
                        return bool( 0 )
        elif abs( len(s) - len(t) ) == 1:
            i,j=0,0
            while i<len(s) and j<len(t):
                if s[i]!=t[j]:
                    if not res:
                        res = 1
                        if len(s) > len(t):
                            j-=1
                        else:
                            i-=1
                    else:
                        return bool( 0 )
                i+=1
                j+=1
            return bool( 1 )
        return bool( res )
