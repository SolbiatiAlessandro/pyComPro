def populate_dp(s, wordDict):
    dp = dict()
    for word in wordDict:
        offset = 0
        while True:
            start = offset + s[offset:].find(word)
            end = start + len(word) - 1
            if start == offset - 1: break
            dp[(start, end)] = True
            offset = start + 1
    return dp



class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp, wordDict = [True], set(wordDict)
        for i in range(1, len(s) + 1):
            print i,"\n"
            for j in xrange(i):
                if s[j:i] in wordDict:
                    import pdb;pdb.set_trace()
            dp.append(any(dp[j] and s[j:i] in wordDict for j in xrange(i)))
        print dp
        return dp[-1]

        
def test_populate():
    s = "leetcode"
    wordDict = ["leet","code"]
    got = populate_dp(s, wordDict)
    assert len(got) == 2
    assert got[(4, 7)] == True
    assert got[(0, 3)] == True
    s = "leetcodeleet"
    wordDict = ["leet","code"]
    got = populate_dp(s, wordDict)
    assert len(got) == 3
    assert got[(4, 7)] == True
    assert got[(8, 11)] == True
    assert got[(0, 3)] == True
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    got = populate_dp(s, wordDict)
    assert len(got) == 3
    assert got[(0, 4)] == True
    assert got[(8, 12)] == True
    assert got[(5, 7)] == True
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    got = populate_dp(s, wordDict)
    assert len(got) == 5
    assert got[(0, 3)] == True
    assert got[(6, 8)] == True
    assert got[(3, 6)] == True
    assert got[(4, 6)] == True
    assert got[(0, 2)] == True
    s = "c"
    wordDict = ["c"]
    got = populate_dp(s, wordDict)
    assert len(got) == 1
    assert got[(0, 0)] == True
    print "Test_populate OK"

if __name__ == "__main__":
    ss=Solution()

    #test_populate()

    s = "leetcode"
    wordDict = ["leet","code"]
    assert ss.wordBreak(s, wordDict) 

    s = "applepenapple"
    wordDict = ["apple", "pen"]
    assert ss.wordBreak(s, wordDict) 

    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    assert not ss.wordBreak(s, wordDict) 

    s = "c"
    wordDict = ["c"]
    assert ss.wordBreak(s, wordDict) 

    import pickle as pk
    d = pk.load(open("tle.pkl",'rb'))
    wordDict=d['wordDict']
    s=d['s']
    from time import time
    t=time()
    ss.wordBreak(s, wordDict) 
    print(time()-t)
