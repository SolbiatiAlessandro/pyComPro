class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i,j = 0,len(s)-1
        while i<len(s) and s[i] == ' ':
            i+=1
        while 0<=j<len(s) and s[j] == ' ':
            j-=1
        s = s[i:j+1]
        if len(s) == 0:
            return False
        transitions = {
                ( 0, '.' ) : 2,
                ( 0, 'n' ) : 1,
                ( 0, '+' ) : 1,
                ( 0, '-' ) : 1,
                ( 1, 'n' ) : 1,
                ( 1, 'e' ) : 3,
                ( 1, '.' ) : 2,
                ( 2, 'n' ) : 2,
                ( 2, 'e' ) : 3,
                ( 3, 'n' ) : 4,
                ( 3, '+' ) : 4,
                ( 3, '-' ) : 4,
                ( 4, 'n' ) : 4,
        }
        state = 0
        if not ( '0' <= s[-1] <= '9' or s[1] == '.' ):
            return False
        for c in s:
            if '0' <= c <= '9':
                c = 'n'
            state = transitions.get( (state, c ) )
            if state is None:
                return False
        return True
        
