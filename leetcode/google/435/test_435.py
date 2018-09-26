import unittest
import l435

class testSolution( unittest.TestCase ):

    def setUp( self ):
        self.s = l435.Solution()

    def test_solution(self):
        got = self.s.isPalindrome( "A man, a plan, a canal: Panama" )
        self.assertEqual( got, True )

        #import pdb;pdb.set_trace()
        got = self.s.isPalindrome( "race a car" )
        self.assertEqual( got, False )

        got = self.s.isPalindrome( "" )
        self.assertEqual( got, True )


if __name__ == "__main__":
    unittest.main()
