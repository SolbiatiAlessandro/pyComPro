import unittest
import l455

class testSolution(unittest.TestCase):
    
    def setUp( self ):
        self.s = l455.Solution()

    def test_solution( self ):
        
        got = self.s.findMaxConsecutiveOnes( [1,0,1,1,0] )
        self.assertEqual( got, 4 )

        got = self.s.findMaxConsecutiveOnes( [0,0,0,1,0,0,1,1,0,0,0,1,1,1,0,1] )
        self.assertEqual( got, 5 )

        got = self.s.findMaxConsecutiveOnes( [1,1,0,1,1,1,0,0,1] )
        self.assertEqual( got, 6 )

        got = self.s.findMaxConsecutiveOnes( [0] )
        self.assertEqual( got, 1 )

        got = self.s.findMaxConsecutiveOnes( [] )
        self.assertEqual( got, 0 )

        got = self.s.findMaxConsecutiveOnes( [0,1] )
        self.assertEqual( got, 2 )

        got = self.s.findMaxConsecutiveOnes( [0,0,0] )
        self.assertEqual( got, 1 )

        got = self.s.findMaxConsecutiveOnes( [1,0,1] )
        self.assertEqual( got, 3 )

        print "ok"

if __name__ == "__main__":
    unittest.main()

