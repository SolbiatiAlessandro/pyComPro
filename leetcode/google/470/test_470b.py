import unittest
import l470b

class testLinkedList( unittest.TestCase ):

    def setUp( self ):
        self.l = l470b.LinkedList( 5 )

    def test_inBoundaries(self):
        for x in xrange(2,5):
            self.assertTrue(self.l.checkPlace(x, 0))
        self.l.removePlace( 3 )
        self.assertTrue(self.l.checkPlace(2, 1))
        self.assertTrue(self.l.checkPlace(4, 1))

    def test_doubleLink(self):
        
        self.assertTrue(self.l.checkPlace(2, 0))
        self.l.removePlace( 3 )
        self.assertTrue(self.l.checkPlace(2, 1))
        self.l.removePlace( 4 )
        self.assertTrue(self.l.checkPlace(2, 2))

    def test_outBoundaries(self):
        self.assertTrue(self.l.checkPlace(5,0))
        self.assertFalse(self.l.checkPlace(5,3))
        self.assertFalse(self.l.checkPlace(1,3))
        self.assertTrue(self.l.checkPlace(1,0))
        self.l.removePlace(4)
        self.assertTrue(self.l.checkPlace(3,1))
        self.l.removePlace(5)
        self.assertFalse(self.l.checkPlace(3,1))
        #import pdb;pdb.set_trace()
        self.assertFalse(self.l.checkPlace(3,2))
        self.l.removePlace(1)
        self.assertTrue(self.l.checkPlace(2,0))

    def test_outLowBoundaries(self):
        self.assertTrue(self.l.checkPlace(3,0))
        self.l.removePlace(2)
        self.assertTrue(self.l.checkPlace(3,1))
        self.l.removePlace(1)
        self.assertFalse(self.l.checkPlace(3,2))
        
        
class testSolution( unittest.TestCase ):

    def setUp( self ):
        self.s = l470b.Solution()

    def test_example( self ):

        flowers = [1,3,2]
        k = 1
        got = self.s.kEmptySlots( flowers, k )
        self.assertEqual( got, 2 )

        flowers = [1,2,3]
        got = self.s.kEmptySlots( flowers, k )
        self.assertEqual( got, -1 )

        flowers = [1,3,7,9,5,6]
        got = self.s.kEmptySlots( flowers, 3 )
        self.assertEqual( got, 3 )
        got = self.s.kEmptySlots( flowers, 2 )
        self.assertEqual( got, -1 )
        got = self.s.kEmptySlots( flowers, 1 )
        self.assertEqual( got, 2 )
        got = self.s.kEmptySlots( flowers, 0 )
        self.assertEqual( got, 6 )

        
        got = self.s.kEmptySlots( [], 0 )
        self.assertEqual( got, -1 )

        got = self.s.kEmptySlots( [1], 0 )
        self.assertEqual( got, -1 )

        got = self.s.kEmptySlots( [1,2], 0 )
        self.assertEqual( got, 2 )

if __name__ == "__main__":
    unittest.main()
