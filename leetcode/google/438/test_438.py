import unittest
import l438


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l438.Solution()

    def test_solution( self ):
        word1 = "horse"
        word2 = "ros"
        self.assertEqual(self.s.minDistance(word1, word2), 3)
        
        word1 = "intention"
        word2 = "execution"
        self.assertEqual(self.s.minDistance(word1, word2), 5)
        

if __name__ == "__main__":
    unittest.main()

