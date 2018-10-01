import unittest
import l465b as l465


class testSolution(unittest.TestCase):
    def setUp( self ):
        self.s = l465.Solution()

    #@unittest.skip("wait")
    def test_long(self):
        # import pdb;pdb.set_trace()
        import time
        s = "a"*int(10e4)+"cd"+"a"*int(10e4)
        t = time.time()
        got = self.s.shortestPalindrome(s)
        print "time efficiency: "+str(time.time() - t)

    #@unittest.skip("wait")
    def test_solution( self ):

        got = self.s.shortestPalindrome("abcd")
        self.assertEqual(got, "dcbabcd")
        got = self.s.shortestPalindrome("abcde")
        self.assertEqual(got, "edcbabcde")
        # import pdb;pdb.set_trace()
        got = self.s.shortestPalindrome("aacecaaa")
        self.assertEqual(got, "aaacecaaa")
        got = self.s.shortestPalindrome("aba")
        self.assertEqual(got, "aba")
        got = self.s.shortestPalindrome("aa")
        self.assertEqual(got, "aa")
        got = self.s.shortestPalindrome("aab")
        self.assertEqual(got, "baab")
        got = self.s.shortestPalindrome("baabkk")
        self.assertEqual(got, "kkbaabkk")
        got = self.s.shortestPalindrome("")
        self.assertEqual(got, "")
        got = self.s.shortestPalindrome("aaaakjh")
        self.assertEqual(got, "hjkaaaakjh")
        got = self.s.shortestPalindrome("aabbkkbbbaaa")
        self.assertEqual(got, "aaabbbkkbbaabbkkbbbaaa")
        got = self.s.shortestPalindrome("a")
        self.assertEqual(got, "a")


    def test_longestPalindrome(self):

        string = "ababecebababa"
        got = l465.longestPalindrome(string)
        self.assertEqual(got, 11)
        string = "ababecebaba"
        got = l465.longestPalindrome(string)
        self.assertEqual(got, 11)
        string = "abeceba"
        got = l465.longestPalindrome(string)
        self.assertEqual(got, 7)
        string = "abecebaaaa"
        got = l465.longestPalindrome(string)
        self.assertEqual(got, 7)
        string = "kabecebaaaa"
        got = l465.longestPalindrome(string)
        self.assertEqual(got, 1)
        string = "aaeceaaa"
        got = l465.longestPalindrome(string)
        self.assertEqual(got, 7)
        string = "aaaakjh"
        got = l465.longestPalindrome(string)
        self.assertEqual(got, 4)
        string = "abbakjh"
        got = l465.longestPalindrome(string)
        self.assertEqual(got, 4)

        string = "aabbkkbbbaaa"
        got = l465.longestPalindrome(string)
        self.assertEqual(got, 2)

        string = "aabbkkbbaaa"
        got = l465.longestPalindrome(string)
        self.assertEqual(got, 10)

        string = "abcd"
        got = l465.longestPalindrome(string)
        self.assertEqual(got, 1)

        got = l465.longestPalindrome("abcd")
        self.assertEqual(got, 1)
        got = l465.longestPalindrome("abcde")
        self.assertEqual(got, 1)
        got = l465.longestPalindrome("aacecaaa")
        self.assertEqual(got, 7)
        got = l465.longestPalindrome("aba")
        self.assertEqual(got, 3)
        got = l465.longestPalindrome("aa")
        self.assertEqual(got, 2)
        got = l465.longestPalindrome("aab")
        self.assertEqual(got, 2)
        got = l465.longestPalindrome("baabkk")
        self.assertEqual(got, 4)
        got = l465.longestPalindrome("")
        self.assertEqual(got, 0)
        got = l465.longestPalindrome("aaaakjh")
        self.assertEqual(got, 4)
        got = l465.longestPalindrome("aabbkkbbbaaa")
        self.assertEqual(got, 2)
        got = l465.longestPalindrome("a")
        self.assertEqual(got, 1)



if __name__ == "__main__":
    unittest.main()
