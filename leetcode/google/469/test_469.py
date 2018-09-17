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


    def test_repeatMoreThanTwoTimes( self ):

        A, B = "kuku", "kukukukukukukuku"
        res = self.s.repeatedStringMatch( A, B ) 
        #import pdb;pdb.set_trace()
        self.assertEqual( res, 4 )

        A, B = "kuku", "kukukukukukukukuk"
        res = self.s.repeatedStringMatch( A, B ) 
        #import pdb;pdb.set_trace()
        self.assertEqual( res, 5 )

    def test_alreadySubstring( self ):

        A, B = "kuku", "kuk"
        res = self.s.repeatedStringMatch( A, B ) 
        #import pdb;pdb.set_trace()
        self.assertEqual( res, 1 )

    def test_tailTouchFront( self ):

        A, B = "kukk", "kkkukk"
        res = self.s.repeatedStringMatch( A, B ) 
        #import pdb;pdb.set_trace()
        self.assertEqual( res, 2 )

if __name__ == "__main__":
    unittest.main()
