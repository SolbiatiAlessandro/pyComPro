import unittest
import l469

class testSolution( unittest.TestCase ):

    def setUp( self ):
        self.s = l469.Solution()

    def test_example( self ):

        A, B = "abcd", "cdabcdab"
        res = self.s.repeatedStringMatch( A, B ) 
        #import pdb;pdb.set_trace()
        self.assertEqual( res, 3 )

    def test_doesNotContainString( self ):

        A, B = "abac", "acab"
        res = self.s.repeatedStringMatch( A, B ) 
        #import pdb;pdb.set_trace()
        self.assertEqual( res, 2 )

    def test_repeatLetter( self ):

        A, B = "caaa", "aac"
        res = self.s.repeatedStringMatch( A, B ) 
        #import pdb;pdb.set_trace()
        self.assertEqual( res, 2 )

        A, B = "caaa", "aacaaaca"
        res = self.s.repeatedStringMatch( A, B ) 
        #import pdb;pdb.set_trace()
        self.assertEqual( res, 3 )

    def test_notMatching( self ):

        A, B = "caaa", "kacaaaca"
        res = self.s.repeatedStringMatch( A, B ) 
        #import pdb;pdb.set_trace()
        self.assertEqual( res, -1 )

        A, B = "caaa", "aacbaaca"
        res = self.s.repeatedStringMatch( A, B ) 
        #import pdb;pdb.set_trace()
        self.assertEqual( res, -1 )

        A, B = "caaa", "aacaaacb"
        res = self.s.repeatedStringMatch( A, B ) 
        #import pdb;pdb.set_trace()
        self.assertEqual( res, -1 )







if __name__ == "__main__":
    unittest.main()
