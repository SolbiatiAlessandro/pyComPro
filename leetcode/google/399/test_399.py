import unittest
import l399


class testSolution( unittest.TestCase ):

    def setUp( self ):
        self.s = l399.Solution()
    
    def test_solution(self):
        got = self.s.findStrobogrammatic(1)
        print got
        got = self.s.findStrobogrammatic(2)
        print got
        got = self.s.findStrobogrammatic(2)
        self.assertItemsEqual(got, ["11","69","88","96"])
        got = self.s.findStrobogrammatic(3)
        print got
        got = self.s.findStrobogrammatic(4)
        print got




if __name__ == "__main__":
    unittest.main()
