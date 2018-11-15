import unittest
import l356


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l356.Solution()

    def test_solution( self ):
        got = self.s.wordsTyping(["hello", "world"], 2, 8)
        self.assertEqual(got, 1)
        got = self.s.wordsTyping(["a","bcd","e"], 3, 6)
        self.assertEqual(got, 2)
        got = self.s.wordsTyping(["I", "had", "apple", "pie"], 4, 5)
        self.assertEqual(got, 1)
        got = self.s.wordsTyping(["I", "had", "apple", "pie"], 1, 1)
        self.assertEqual(got, 0)
        

if __name__ == "__main__":
    unittest.main()

