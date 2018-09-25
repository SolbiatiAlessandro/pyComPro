import unittest
import l398


class testSolution( unittest.TestCase ):

    def setUp( self ):
        self.s = l398.Solution()

    def test_solution(self):

        got = self.s.isOneEditDistance( "acb", "acb" )
        self.assertEqual( got, 0 )

        got = self.s.isOneEditDistance( "b", "b" )
        self.assertEqual( got, 0 )

        got = self.s.isOneEditDistance( "r", "b" )
        self.assertEqual( got, 1 )

        got = self.s.isOneEditDistance( "", "" )
        self.assertEqual( got, 0 )

        got = self.s.isOneEditDistance( "4", "" )
        self.assertEqual( got, 1 )

        got = self.s.isOneEditDistance( "ab", "acb" )
        self.assertEqual( got, 1 )

        got = self.s.isOneEditDistance( "ab", "acb" )
        self.assertEqual( got, 1 )

        got = self.s.isOneEditDistance( "cab", "ad" )
        self.assertEqual( got, 0 )

        got = self.s.isOneEditDistance( "1203", "1213" )
        self.assertEqual( got, 1 )

        got = self.s.isOneEditDistance( "1203", "12034" )
        self.assertEqual( got, 1 )

        got = self.s.isOneEditDistance( "1203", "1203454" )
        self.assertEqual( got, 0 )

        got = self.s.isOneEditDistance( "012034", "12034" )
        self.assertEqual( got, 1 )

        got = self.s.isOneEditDistance( "012034", "120340" )
        self.assertEqual( got, 0 )

        got = self.s.isOneEditDistance( "0120345", "0120340" )
        self.assertEqual( got, 1 )


if __name__ == "__main__":
    unittest.main()
