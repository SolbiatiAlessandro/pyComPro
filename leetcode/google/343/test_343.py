import unittest
import l343


class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l343.PeekingIterator((x for x in xrange(10)))

    def test_solution( self ):
        for _ in xrange(10):
            val = self.s.peek()   # Get the next element but not advance the iterator.
            self.assertEqual(self.s.next(), val)         # Should return the same value as [val]
            print val
        


        

if __name__ == "__main__":
    unittest.main()

