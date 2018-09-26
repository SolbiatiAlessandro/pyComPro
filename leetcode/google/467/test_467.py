import unittest
import l467

class testSolution( unittest.TestCase ):

    def setUp( self ):
        self.s = l467.Solution()

    def test_solution( self ):
        got = self.s.isValid("()")
        self.assertEqual( got, True )
        got = self.s.isValid("()[]{}")
        self.assertEqual( got, True )
        got = self.s.isValid("(]")
        self.assertEqual( got, False )
        got = self.s.isValid("([)]")
        self.assertEqual( got, False )
        got = self.s.isValid("{[]}")
        self.assertEqual( got, True )
        got = self.s.isValid("{[")
        self.assertEqual( got, False)
        got = self.s.isValid("")
        self.assertEqual( got, True )


if __name__ == "__main__":
    unittest.main()
