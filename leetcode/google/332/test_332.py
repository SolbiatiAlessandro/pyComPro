import unittest
import l332

class testSolution( unittest.TestCase ):

    def setUp( self ):
        self.s = l332.Solution()

    def test_solution(self):

        got = self.s.lengthOfLongestSubstringKDistinct( "eceba", 2 )
        self.assertEqual( got, 3 )

        got = self.s.lengthOfLongestSubstringKDistinct( "eceba"[::-1], 2 )
        self.assertEqual( got, 3 )

        got = self.s.lengthOfLongestSubstringKDistinct( "aa", 1 )
        self.assertEqual( got, 2 )
        
        got = self.s.lengthOfLongestSubstringKDistinct( "aa"[::-1], 1 )
        self.assertEqual( got, 2 )
        
        got = self.s.lengthOfLongestSubstringKDistinct( "ecceeba", 2 )
        self.assertEqual( got, 5 )

        got = self.s.lengthOfLongestSubstringKDistinct( "ecceeba"[::-1], 2 )
        self.assertEqual( got, 5 )

        got = self.s.lengthOfLongestSubstringKDistinct( "ececeba", 2 )
        self.assertEqual( got, 5 )

        got = self.s.lengthOfLongestSubstringKDistinct( "ececeba"[::-1], 2 )
        self.assertEqual( got, 5 )

        got = self.s.lengthOfLongestSubstringKDistinct( "ecceeceba", 2 )
        self.assertEqual( got, 7 )

        got = self.s.lengthOfLongestSubstringKDistinct( "ecceeceba"[::-1], 2 )
        self.assertEqual( got, 7 )

        got = self.s.lengthOfLongestSubstringKDistinct( "ecebeea", 2 )
        self.assertEqual( got, 4 )

        got = self.s.lengthOfLongestSubstringKDistinct( "ecebeea"[::-1], 2 )
        self.assertEqual( got, 4 )

        got = self.s.lengthOfLongestSubstringKDistinct( "ecebeae", 3 )
        self.assertEqual( got, 5 )

        got = self.s.lengthOfLongestSubstringKDistinct( "ecebeae"[::-1], 3 )
        self.assertEqual( got, 5 )

        got = self.s.lengthOfLongestSubstringKDistinct( "abbacckkk", 3 )
        self.assertEqual( got, 6 )

        got = self.s.lengthOfLongestSubstringKDistinct( "abbacckkk"[::-1], 3 )
        self.assertEqual( got, 6 )

        got = self.s.lengthOfLongestSubstringKDistinct( "ccceveeeea", 2 )
        self.assertEqual( got, 6 )

        got = self.s.lengthOfLongestSubstringKDistinct( "ccceveeeea"[::-1], 2 )
        self.assertEqual( got, 6 )

        got = self.s.lengthOfLongestSubstringKDistinct( "aaabc", 2 )
        self.assertEqual( got, 4 )

        got = self.s.lengthOfLongestSubstringKDistinct( "aaabc"[::-1], 2 )
        self.assertEqual( got, 4 )

        got = self.s.lengthOfLongestSubstringKDistinct( "aaabbbccc", 3 )
        self.assertEqual( got, 9 )

        got = self.s.lengthOfLongestSubstringKDistinct( "aaabbbccc"[::-1], 3 )
        self.assertEqual( got, 9 )

        got = self.s.lengthOfLongestSubstringKDistinct( "aaabbbccc", 2 )
        self.assertEqual( got, 6 )

        got = self.s.lengthOfLongestSubstringKDistinct( "aaabbbccc"[::-1], 2 )
        self.assertEqual( got, 6 )

        got = self.s.lengthOfLongestSubstringKDistinct( "aaaaaaaaa", 3 )
        self.assertEqual( got, 9 )

        got = self.s.lengthOfLongestSubstringKDistinct( "aaaaaaaaa", 1 )
        self.assertEqual( got, 9 )

        got = self.s.lengthOfLongestSubstringKDistinct( "aaaaaaaaa", 2 )
        self.assertEqual( got, 9 )

        got = self.s.lengthOfLongestSubstringKDistinct( "aaaaaaaaa"[::-1], 3 )
        self.assertEqual( got, 9 )

        got = self.s.lengthOfLongestSubstringKDistinct( "aakaaaaaa", 3 )
        self.assertEqual( got, 9 )

        got = self.s.lengthOfLongestSubstringKDistinct( "aakaaaaaa"[::-1], 3 )
        self.assertEqual( got, 9 )

        got = self.s.lengthOfLongestSubstringKDistinct( "aakaaaaaa", 2 )
        self.assertEqual( got, 9 )

        got = self.s.lengthOfLongestSubstringKDistinct( "aakaaaaaa"[::-1], 2 )
        self.assertEqual( got, 9 )

        got = self.s.lengthOfLongestSubstringKDistinct( "aakaaaaaa", 1 )
        self.assertEqual( got, 6 )

        got = self.s.lengthOfLongestSubstringKDistinct( "aakaaaaaa"[::-1], 1 )
        self.assertEqual( got, 6 )




if __name__ == "__main__":
    unittest.main()
