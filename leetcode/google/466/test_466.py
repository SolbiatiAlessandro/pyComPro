import unittest
import l466


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l466.Solution()

    def test_solution( self ):
        got = self.s.rob([2,3,2])
        self.assertEqual(got, 3)
        
        got = self.s.rob([1,2,3,1])
        self.assertEqual(got, 4)
        got = self.s.rob(range(1, 12))
        self.assertEqual(got, 35)
        

if __name__ == "__main__":
    unittest.main()

