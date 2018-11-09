import unittest
import l451b


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l451b.Solution()

    def test_solution( self ):
        
        got = self.s.longestPalindrome("abbkcj")
        self.assertEqual(got, "bb")
        got = self.s.longestPalindrome("babad")
        self.assertEqual(got, "bab")
        got = self.s.longestPalindrome("cbbbbd")
        self.assertEqual(got, "bbbb")
        got = self.s.longestPalindrome("kaaakkk")
        self.assertEqual(got, "kaaak")
        got = self.s.longestPalindrome("cbbd")
        self.assertEqual(got, "bb")
        got = self.s.longestPalindrome("cbbd")
        self.assertEqual(got, "bb")
        got = self.s.longestPalindrome("bbb")
        self.assertEqual(got, "bbb")
        got = self.s.longestPalindrome("bb")
        self.assertEqual(got, "bb")
        got = self.s.longestPalindrome("b")
        self.assertEqual(got, "b")
        got = self.s.longestPalindrome("")
        self.assertEqual(got, "")
        got = self.s.longestPalindrome("aacdefcaa")
        self.assertEqual(got, "aa")


if __name__ == "__main__":
    unittest.main()

