import unittest
import l471

class testDifference( unittest.TestCase ):

    def test_baseExample( self ):

        A = "19:34"
        B = "20:44"
        C = "21:24"
        D = "18:44"
        E = "18:24"
        self.assertEqual( l471.timeDifference( A, B ), 70 ) 
        self.assertEqual( l471.timeDifference( A, C ), 110 ) 
        self.assertEqual( l471.timeDifference( A, D ), 1390 ) 
        self.assertEqual( l471.timeDifference( A, E ), 1370 ) 

    def test_integrationWithSolution( self ):
        
        got1 = l471.timeDifference( "19:34", "19:39" )
        got2 = l471.timeDifference( "19:34", "19:49" )
        #import pdb;pdb.set_trace()
        self.assertGreater( got2, got1 )

class testSolution(unittest.TestCase):

    def setUp( self ):
        self.s = l471.Solution()

    def test_baseExample( self ):

        self.assertEqual( self.s.nextClosestTime( "19:34" ), "19:39" )
        self.assertEqual( self.s.nextClosestTime( "23:59" ), "22:22" )


if __name__ == "__main__":
    unittest.main()
