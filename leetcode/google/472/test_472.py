import unittest
import l472

class testSolution( unittest.TestCase ):

    def setUp( self ):
        self.s = l472.Solution()

    def test_base( self ):

        got = self.s.licenseKeyFormatting( "5F3Z-2e-9-w", 4 )
        self.assertEqual( got,"5F3Z-2E9W" )

        got = self.s.licenseKeyFormatting( "2-5g-3-j", 2 )
        self.assertEqual( got,"2-5G-3J" )


if __name__ == "__main__":
    unittest.main()
