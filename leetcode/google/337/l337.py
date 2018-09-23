def populateHelper( s, dict ):
    #import pdb;pdb.set_trace()
    helper = [-1]*len(s)
    for ss in dict:
        cursor = 0
        while True:  # find all occurences of ss in s
            found = s[cursor:].find(ss)
            if found == -1:
                break
            start, finish = cursor+found, cursor+found+len(ss)
            #import pdb;pdb.set_trace()
            helper[start:finish] = (finish-start)*[1]
            cursor += found+1
    return helper

class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        l,added,helper = len(s),0,populateHelper(s,dict)
        for i in xrange(l):
            if helper[i]==1:
                if ( i==0 or helper[i-1] == -1 ):
                    s=s[:i+added]+"<b>"+s[i+added:]
                    added+=3
                if i==l-1 or helper[i+1] == -1:
                    s=s[:i+added+1]+"</b>"+s[i+added+1:]
                    added+=4
        return s
