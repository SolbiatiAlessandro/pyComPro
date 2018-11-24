import unittest
import l460


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l460.Solution()

    def test_solution( self ):
        words = ["abcw","baz","foo","bar","xtfn","abcdef"]
        got = self.s.maxProduct(words)
        self.assertEqual(got, 16 )
        
        words = ["a","ab","abc","d","cd","bcd","abcd"]
        got = self.s.maxProduct(words)
        self.assertEqual(got, 4 )

        words = ["a","aa","aaa","aaaa"]
        got = self.s.maxProduct(words)
        self.assertEqual(got, 0 )


if __name__ == "__main__":
    unittest.main()

