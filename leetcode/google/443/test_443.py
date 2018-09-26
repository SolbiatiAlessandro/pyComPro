import unittest
import l443


class testSolution( unittest.TestCase ):

    def setUp( self ):
        self.s = l443.Solution()
    
    def test_solution( self ):
        got = self.s.isNumber( "0" )
        self.assertEqual( got, True )

        got = self.s.isNumber( " 0.1 " )
        self.assertEqual( got, True )

        got = self.s.isNumber( "abc" )
        self.assertEqual( got, False )

        got = self.s.isNumber( "1 a" )
        self.assertEqual( got, False )

        got = self.s.isNumber( "2e10" )
        self.assertEqual( got, True )

        got = self.s.isNumber( " -90e3   " )
        self.assertEqual( got, True )

        got = self.s.isNumber( " 1e" )
        self.assertEqual( got, False )

        got = self.s.isNumber( "e3" )
        self.assertEqual( got, False )

        got = self.s.isNumber( " 6e-1" )
        self.assertEqual( got, True )

        got = self.s.isNumber( " 99e2.5 " )
        self.assertEqual( got, False )

        got = self.s.isNumber( "53.5e93" )
        self.assertEqual( got, True )

        got = self.s.isNumber( " --6 " )
        self.assertEqual( got, False )

        got = self.s.isNumber( "-+3" )
        self.assertEqual( got, False )

        got = self.s.isNumber( "95a54e53" )
        self.assertEqual( got, False )

        got = self.s.isNumber( "" )
        self.assertEqual( got, False )

        got = self.s.isNumber( ".1" )
        self.assertEqual( got, True )

        got = self.s.isNumber( "1." )
        self.assertEqual( got, True )

        got = self.s.isNumber( " " )
        self.assertEqual( got, False )


if __name__ == "__main__":
    unittest.main()
